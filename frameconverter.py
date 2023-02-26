import cv2
import numpy as np
import os
from os.path import isfile, join
import webuiAPI.generator
from PIL import Image, PngImagePlugin
import logging
import compress

setup={
    'width': 512,
    'height': 512,
}
def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")
def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s
def video2frame(video_file,framepersec=60):
    SAVING_FRAMES_PER_SECOND = framepersec
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file
    cap = cv2.VideoCapture(video_file)
    if cap.isOpened() == False:
        cap.open(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    temp=0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration, 
            # then save the frame
            cv2.imwrite(os.path.join(filename, f"frame{temp}.png"), frame) 
            compress.resize_png(os.path.join(filename, f"frame{temp}.png"))
            temp=temp+1
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1
    return filename

'''def frame2video(pathIn,pathOut,fps):
    logging.info(f"pathIn: {pathIn}")
    logging.info(f"pathOut: {pathOut}")
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
    for i in range(int(len(files))):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, (setup["width"],  setup["height"]))
    logging.info("HERE TO OUT")
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()'''

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
    for i in range(int(len(files))):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
    
def processframes(pathIn, pathOut):
    if not os.path.isdir(pathIn):
        os.mkdir(pathIn)
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
    temp=0
    for i in range(int(len(files))):
        logging.info("DEAILING WITH FRAME "+str(i))
        filename=pathIn+files[i]
        #reading each files
        img = Image.open(filename)
        height, width = img.width, img.height
        setup["width"]=512
        setup["height"]=512
        print(filename)
        output = webuiAPI.generator.controlNetImg2img(img, setup)
        #inserting the frames into an image array
        webuiAPI.generator.saveimg(path=pathOut, img=output, fileName=f"frame{temp}")
        temp+=1
    logging.info("DEAL FRAME FINISH")
'''
if __name__=="__main__":
    import sys
    #pathin=sys.argv[1]
    #pathout=sys.argv[2]
    processframes('D:\StudyLife\Github\HackIllinois\input\girl-44686_4-opencv/', 'output/')
'''