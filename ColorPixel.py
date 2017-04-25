#!/usr/bin/python

import cv2
try:
    Filename = "VID_20170208_144233.avi"
    video = cv2.VideoCapture(-1)
    print video.grab()
except:
    print "No such file"

success,frame = video.read()
count = 0
success = True
while success:
    success,frame = video.read()
    #cv2.rectangle(frame, )
    print int(frame[300,300])
