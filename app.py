#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import Camera
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(Camera):
    cap = cv2.VideoCapture(0)
    width = cap.get(3)  # float
    height = cap.get(4) # float
    while True:
        #frame = Camera.get_frame()
        ret,frame = cap.read()
        #imwrite("temp.jpg",frame

       # frame = np.asarray(frame, dtype=np.uint8).reshape(height, width, 4)
        #cv2.imwrite("temp.jpg",frame)       
        #frame=cv2.imread("temp.jpg")       
	
        ret,frame=cv2.imencode('.jpg', frame)
        frame = frame.tostring()#base64.b64encode(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/veena')
def veena():
	return 'its working'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000 ,debug=True)
