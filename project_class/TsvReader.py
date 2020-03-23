#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:52:58 2020

@author: fred
"""

import pandas as pd
import csv

class TsvReader:
    """
    Classe permettant de lire un fichier .tsv de façon séquentielle
    """
    
    def __init__(self, path=""):
        """
        Initialisation des variables
        """
        self.path = path
        self.file = open(path, "rt")
        self.header = self.file.readline()
    
    
    def read_to_df(self):
        """
        Lecture du fichier en DataFrame
        """
        df = pd.read_csv(self.path, sep="\t")
        return df
    
    
    def read_seq(self, number_of_lines=100):
        """
        Lecture séquentielle de fichiers volumineux
        """
        lines = []
        counter = 0
        line = self.file.readline()
        while line and counter < number_of_lines:
            lines.append(line)
            counter += 1
            line = self.file.readline()

        if len(lines) == 0:
            return None

        lines.insert(0, self.header)
        lines_as_dict = csv.DictReader(lines, delimiter='\t')

        return lines_as_dict
            
            
            
# =============================================================================
# Compteur de lignes en commande terminal
# =============================================================================
# import subprocess as sp
# file = "../data/title.akas.tsv"
# a = sp.check_output(["wc", "-l", file.split(" ")[0]])
# a = a.split()[0]
# print(int(a))
# =============================================================================
# 
# =============================================================================
