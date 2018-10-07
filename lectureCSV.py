# -*- coding : utf-8 -*-

import csv

def fileCSVToList(fichier):
    with open(fichier, "r") as elements:
        return elements.read().split()
