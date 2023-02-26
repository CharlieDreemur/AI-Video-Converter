from datetime import timedelta
import cv2
import numpy as np
import os

if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    video2frame(video_file)
    framepersec= float(sys.argv[2])

