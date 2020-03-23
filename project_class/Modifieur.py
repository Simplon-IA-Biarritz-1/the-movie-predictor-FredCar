#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:45:17 2020

@author: fred
"""
import pprint


class Modifieur:
    """
    Classe permettant de modifier les données
    avant de les insérer dans la base
    """
    
    def __init__(self):
        pass
    
    def spliter(self, data, key):
        """
        Splite les données
        """
        data[key] = data[key].split(",")
        return data
        
    
    def integer(self, data, key):
        """
        Passe les chiffres de str -> int
        """
        if data[key] != "\\N":
            data[key] = int(data[key])
        return data
                        
