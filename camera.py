from time import time
import numpy as np
import cv2

#cap = cv2.VideoCapture(0)

#while(True):
    # Capture frame-by-frame
#    ret, frame = cap.read()



class Camera(object):
	def __init__(self):
		cap = cv2.VideoCapture(0)
		#self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
		self.frames = cap.read()

	def get_frame(self):
        	return self.frames #[int(time()) % 3]
