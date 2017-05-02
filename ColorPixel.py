#!/usr/bin/python

import imageio
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

import sys

Filename = "/home/darien/LolRoflCopter/ColorPixel/Data/VID2.mp4"
video = imageio.get_reader(Filename, 'ffmpeg')
colorArr = []

maxLen = int(len(video))

try:
    print "Starting Collection"
    for i, frame in enumerate(video):
        #tempArr = frame[len(frame)/2,len(frame[0])/2]
        tempArr = frame[900,366]
        temp2 = []
        temp2.append(float(tempArr[0])/256.0)
        temp2.append(float(tempArr[1])/256.0)
        temp2.append(float(tempArr[2])/256.0)
        colorArr.append(temp2)

        sys.stdout.write("\rFrame %i of %i" % (i, maxLen))
        sys.stdout.flush()
except KeyboardInterrupt:
    print "\nEnding Collection" 

cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0)
gradient = np.linspace(0,1,256)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap=cmap1)
plt.savefig("GRAD")

