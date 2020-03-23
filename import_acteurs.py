import project_class.TsvReader as tsv
import project_class.DBInteract as dbi
import project_class.Modifieur as mod
import pprint


# Lecture du fichier TSV
tsv = tsv.TsvReader('../data/name.basics.tsv') # Chemin du fichier à traiter
  
# Connection à la base      
host = "localhost"
port = 27017
base = "test_movies"
collec = "acteurs"

ma_base = dbi.DBInteract(host, port, base, collec)

# Instanciation de la classe de modification
mod = mod.Modifieur()

liste = []
while True:
    lines = tsv.read_seq(1000) # Lecture séquentielle

    if lines == "": # Si fin de séquence
        break

    for x in lines:
        # Split str -> list
        x = mod.spliter(x, key="primaryProfession")
        x = mod.spliter(x, key="knownForTitles")

        # Traite str -> int
        x = mod.integer(x, key="birthYear")
        x = mod.integer(x, key="deathYear")

        liste.append(x)
        
        if len(liste) >= 10:
            # Insertion par lots dans la base
            ma_base.insert(liste, method="many")

            # Réinitialisation de la liste
            liste = []

    
 
    
    
