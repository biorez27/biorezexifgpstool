import os
import time

def stopper():
    animation = "|/-\\"
    idx = 0
    while idx<=30: #change this to adjust slow mode pace
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)

print("""


______ _                      _____     _  __   _____ ______  _____   _____           _
| ___ (_)                    |  ___|   (_)/ _| |  __ \| ___ \/  ___| |_   _|         | |
| |_/ /_  ___  _ __ ___ ____ | |____  ___| |_  | |  \/| |_/ /\ `--.    | | ___   ___ | |
| ___ \ |/ _ \| '__/ _ \_  / |  __\ \/ / |  _| | | __ |  __/  `--. \   | |/ _ \ / _ \| |
| |_/ / | (_) | | |  __// /  | |___>  <| | |   | |_\ \| |    /\__/ /   | | (_) | (_) | |
\____/|_|\___/|_|  \___/___| \____/_/\_\_|_|    \____/\_|    \____/    \_/\___/ \___/|_|


Use can choose between fast or slow mode.
Use slow mode to add 3 second between each picture to double check whats going on.
Defaults to slow mode.
""")

speed=input("Type 'f' for fast mode, defaults to slow mode.: ")

while True:
    pictures = input("\nSearch for picture(s): ")
    if " " in pictures:
        pictures = pictures.replace(" ","\ ")

    stream = os.popen('find . -name *'+pictures+'*') #change path if needed
    pictures = stream.read()

    print("\nPicture(s) found: \n"+pictures)
    pictures = pictures.splitlines()

    choice = input("WARNING! Pictures will be overwritten! Continue? y/n: ")
    if choice=="y":
        new_coordinates = input("New coordinates for all pictures: ")
        if " " in new_coordinates:
            new_coordinates=new_coordinates.replace(" ","")
        new_coordinates = new_coordinates.split(",")
        for picture in pictures:
            print("\nNext picture in queue: "+picture+"\n")
            picture=("'"+picture+"'")
            stream = os.popen('exiftool -m -gpslatitude -gpslongitude '+picture)
            output = stream.read()
            if not speed=="f":
                 print("*********************\nCurrent coordinates\n*********************\n"+output)

            stream = os.popen('exiftool '+picture+' -overwrite_original -m -gpslatitude='+new_coordinates[0]+' -gpslongitude='+new_coordinates[1])
            output = stream.read()

            stream = os.popen('exiftool -m -gpslatitude -gpslongitude '+picture)
            output = stream.read()
            if not speed=="f":
                print("\n*********************\nNew coordinates\n*********************\n"+output)
                picture=picture.replace("'","")
                print("\n=================================================================================================\nFinished with picture "+picture+"\n=================================================================================================\n")
                stopper()
                print("\n")
        restart=input("Continue with more pictures? y/n: ")
        if not restart=="y":
            break
    else:
        print("Canceled, no changes were made.")
        break
