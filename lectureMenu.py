# -*- coding: utf-8 -*-

import lectureTXT
import lectureCSV

def readOrWrite():
    """Menu that asks the user if he wants to read a file or edit one """
    print("Souhaitez-vous ouvrir ou éditer un fichier?")
    print("1. Ouvrir")
    print("2. Editer")
    return input("\nChoix : ")

def writeFileName():
    """Get the file chosen by the user to be opened """
    print("Tapez le nom du fichier que vous souhaitez ouvrir")
    return input("\nNom du fichier : ")


def whichFileType(fileName):
    """Search which type of file has been selected by the user """
    typeList = ["csv", "txt", "pdf"]
    lowerFileName = fileName.lower()
    
    for fileType in typeList:
        if lowerFileName.find(fileType) != -1:
            return fileType


def readFile(fileChosen, fileType):
    """Return a list of the elements read in a specific type of file """
    fileChosen = fileChosen.lower()
    print(fileChosen)
    
    if fileType == "csv":
        return lectureCSV.fileCSVToList(fileChosen)

    elif fileType == "txt":
        return lectureTXT.fileTXTToList(fileChosen)

    else:
        print("Le fichier n'a pu être trouvé")
        
        
    
    
