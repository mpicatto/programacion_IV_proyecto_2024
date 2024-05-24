import cv2
import tkinter as tk
from PIL import Image, ImageTk

def accesocam():
    #abre la camara, archivo: accederWebcam
    capture = cv2.VideoCapture(0)
    video_on = True
    while (video_on == True):
        ret, frame = capture.read()
        cv2.imshow('webCam',frame)
        
        if (cv2.waitKey(1) == ord('s')):
            break

    capture.release()
    cv2.destroyAllWindows()