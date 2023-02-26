import cv2
import os
import datetime
import webuiAPI.client
from PIL import Image, PngImagePlugin
from os.path import isfile, join
def outputfolder(pathIn):
    foldername = "D:\StudyLife\Github\HackIllinois\output"
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
        img = Image.open(filename)
        print(filename)
        output = webuiAPI.client.controlNetImg2img(img)
        #inserting the frames into an image array
        webuiAPI.client.saveimg((path+f"frame{temp}.png"), output)
        temp+=1
        
if __name__=="__main__":
    import sys
    pathin=sys.argv[1]
    outputfolder(pathin)