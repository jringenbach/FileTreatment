# -*- coding: utf-8 -*-

import random

def fileTXTToList(fichier):
    with open(fichier, "r") as elements:
        return elements.read().split()
        

   
