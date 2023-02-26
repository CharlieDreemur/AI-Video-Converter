import cv2
import os
import datetime
from os.path import isfile, join
def outputfolder(pathIn):
    foldername = "outputfolder"
    path=os.path.join(pathIn,foldername)
    if not os.path.isdir(path):
        os.mkdir(path)
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
    temp=0
    for i in range(int(len(files))):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        print(filename)
        #inserting the frames into an image array
        cv2.imwrite(os.path.join(path,f"frame{temp}.png"),img)
        temp+=1
if __name__=="__main__":
    import sys
    pathin=sys.argv[1]
    outputfolder(pathin)