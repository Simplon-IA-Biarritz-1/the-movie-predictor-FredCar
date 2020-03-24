import project_class.TsvReader as tsv
import project_class.DBInteract as dbi
import os
import time

debut = time.time()

# Lecture du nom des fichiers
fichiers = os.listdir("../data")
fichiers.reverse() # Pour ne pas commencer par le plus volumineux

# Boucle pour traiter tous les fichiers
nb_ligne_tot = 0
for nom in fichiers:

    debut_tour = time.time()

    # Chemin et nom du fichier
    fichier = "../data/" + nom

    # Lecture du fichier TSV
    obj_tsv = tsv.TsvReader(fichier) # Instanciation
    
    # Variables de connection
    host = "localhost"
    port = 27017
    base = "imdb_movies"
    nom = nom.replace(".", "_") # Modif du titre du fichier
    collec = nom[:-4]

    # Connection à la base      
    ma_base = dbi.DBInteract(host, port, base, collec)

    nb_ligne = 0
    liste = []
    while True:
        lines = obj_tsv.read_seq(1000) # Lecture séquentielle

        # Si fin de séquence
        if lines == None: 
            break
        if lines == "":
            break

        for line in lines:
            nb_ligne += 1
            nb_ligne_tot += 1
            for key in line:
                # Split str -> list
                if line[key] == None:
                    line[key] = "\\N"
                elif "," in line[key]:
                    line[key] = line[key].split(",")
                

                # Traite str -> int
                try:
                    line[key] = int(line[key])
                except:
                    pass

                # Traite str -> float
                try:
                    line[key] = float(line[key])
                except:
                    pass

            liste.append(line)
            
            if len(liste) >= 10:
                # Insertion par lots dans la base
                ma_base.insert(liste, method="many")

                # Réinitialisation de la liste
                liste = []


    temps = time.time() - debut_tour
    minutes = int(temps / 60)
    secondes = temps % 60
    print("=================")
    print(f"{collec} a été bien traité en {minutes} min et {round(secondes)} s, pour {nb_ligne} lignes.")
    print("=================")


temps = time.time() - debut
minutes = int(temps / 60)
secondes = temps % 60
print(f"Temps total : {minutes} min et {round(secondes)} s.")
print(f"Nombre total de lignes : {nb_ligne_tot}.")
