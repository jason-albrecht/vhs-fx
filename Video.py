import numpy as np
import cv2 as cv
from dataclasses import dataclass

@dataclass
class Video:

    def play(path: str):    
        cap = cv.VideoCapture(path)
        
        if (cap.isOpened()==False):
            print("Error opening video stream or file")

        while (cap.isOpened()):
            #capture frame by frame
            ret, frame = cap.read()
            if ret == True:
                cv.imshow('Frame', frame)
                if cv.waitKey(25) & 0xFF == ord('q'):
                    break
            
            else:
                break

        cap.release()

        cv.destroyAllWindows()