import frameconverter
import cutnsec
import cv2
import numpy as np
import os
from os.path import isfile, join
import webuiAPI.generator
from PIL import Image, PngImagePlugin
import logging
import compress
import extractaudio

def total(video_file,fps,cut_seconds):
    filename, _ = os.path.splitext(video_file)
    filename += "total"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    
    cutnsec_path=os.path.join(filename, 'cutnsec.mp4')
    cutnsec.cut_video(video_file, cutnsec_path, cut_seconds)
    frameconverter.video2frame(cutnsec_path,fps)
    video2frame_path=frameconverter.video2frame(cutnsec_path,fps)
    print(video2frame_path)
    audio_path=os.path.join(filename, 'my_audio.mp3')
    extractaudio.extract_audio(cutnsec_path, audio_path)

    processframes_path=os.path.join(filename, 'processframes')
    converterinput_path=video2frame_path+"/"
    frameconverter.processframes(converterinput_path, processframes_path)
    frame2videoinput_path=processframes_path+"/" 
    frame2video_path=os.path.join(filename, 'frame2video.mp4')
    frameconverter.convert_frames_to_video(frame2videoinput_path,frame2video_path,fps)
    combined_path=os.path.join(filename, 'combined.mp4')
    extractaudio.add_audio_to_video(frame2video_path, audio_path,combined_path)

    


if __name__ == '__main__':

    video_file='D:\StudyLife\Github\HackIllinois\input\8 HOURS of Fascinating Sunset over the Tropical Beach with Calming Waves Sounds (4K UHD) - YouTube - Google Chrome 2023-02-26 01-58-51.mp4'
    total(video_file,1,5)