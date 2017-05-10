#!/usr/bin/python

import imageio
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-o', "--outfile", help="Filename of output file for Gradient Image", action="store")
parser.add_option('-f', "--filename", help="Filename of file for processing", action="store")
outfile=options.outfile
Filename=options.filename

video = imageio.get_reader(Filename, 'ffmpeg')
colorArr = []

maxLen = int(len(video))

try:
    print "Starting Collection"
    for i, frame in enumerate(video):
        #tempArr = frame[len(frame)/2,len(frame[0])/2]
        tempArr = frame[900,366]
        temp2 = []
        for i in range(3):
            temp2.append(float(tempArr[i])/256.0)
        colorArr.append(temp2)

        sys.stdout.write("\rFrame %i of %i" % (i, maxLen))
        sys.stdout.flush()
except KeyboardInterrupt:
    print "\nEnding Collection" 

cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0)
gradient = np.linspace(0,1,256)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap=cmap1)
plt.savefig(outfile)

plt.clf()
plt.plot(colorArr[])
