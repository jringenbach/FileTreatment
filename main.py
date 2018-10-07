# -*- coding : utf-8 -*-

import lectureMenu, sys

#initializing userAction
userAction = 0

while userAction != "3":
    #We ask to user if he wants to read or edit the file
    userAction = lectureMenu.readOrWrite()

    if userAction != "3":
        #We get the name of the file chosen by the user
        fileChosen = lectureMenu.writeFileName()

        #We check which type of file the user has chosen
        fileType = lectureMenu.whichFileType(fileChosen)

        if userAction == "1":
            #We read the file
            fileList = lectureMenu.readFile(fileChosen, fileType)
            #We display the read file
            print(str(fileList))
            
        elif userAction == "2":
            #editing the file
            pass

        else:
            print("Votre demande n'a pas été comprise!")

    else:
        sys.exit(0)


