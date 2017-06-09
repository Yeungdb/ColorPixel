#!/usr/bin/python

import imageio
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

import time
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-o', "--outfile", help="Filename of output file for Gradient Image", action="store")
parser.add_option('-f', "--filename", help="Filename of file for processing", action="store")
parser.add_option('-x', "--xpixel", help="Location of X pixel", action="store")
parser.add_option('-y', "--ypixel", help="Location of Y pixel", action="store")
options, args = parser.parse_args()

outfile=options.outfile
Filename=options.filename
xpixel=int(options.xpixel)
ypixel=int(options.ypixel)

video = imageio.get_reader(Filename, 'ffmpeg')

colorArr = []

maxLen = int(len(video))

gradient = np.linspace(0,1,256)
gradient = np.vstack((gradient, gradient))

index = range(maxLen)

Red = []
Blue = []
Green = []

try:
    print "Starting Collection"
    for i in index:
        try:
            frame = video.get_data(i)
            if i == 1:
                plt.imshow(frame)
                plt.savefig('Frame1'+outfile)
                plt.clf()
            pass

        except KeyboardInterrupt:
            print "\nEnding Collection" 
            break

        except: 
            continue
        #tempArr = frame[len(frame)/2,len(frame[0])/2]
        tempArr = frame[xpixel,ypixel]

        temp2 = []
        for j in range(3):
            temp2.append(float(tempArr[j])/256.0)
        colorArr.append(temp2)

        sys.stdout.write("\rFrame %i of %i" % (i, maxLen))
        sys.stdout.flush()

        Red.append(temp2[0])
        Blue.append(temp2[1])
        Green.append(temp2[2])
     
        #if Red:
        #    plt.plot(Red, 'r')
        #    plt.plot(Blue, 'b')
        #    plt.plot(Green, 'g')
        #    plt.ion()
        #    plt.show(block=False)
        #    plt.pause(0.001)

        #cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0)
        #plt.imshow(gradient, aspect='auto', cmap=cmap1)
        #plt.gcf().show()
          
    #Red = colorArr[:,0]
    #Blue = colorArr[:,1]
    #Green = colorArr[:,2]
except KeyboardInterrupt:
    print "\nEnding Collection" 


plt.plot(Red, 'r')
plt.plot(Blue, 'b')
plt.plot(Green, 'g')
plt.savefig('RGB'+outfile)
plt.clf()

cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0)
gradient = np.linspace(0,1,256)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap=cmap1)
plt.savefig(outfile)
plt.clf()
