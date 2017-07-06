#!/usr/bin/python

import imageio
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

import time
import sys
from optparse import OptionParser

from nyanbar import NyanBar

def NameEcho():
    return "ColorPixel"

def AppendTitleToFilename(InFilename, AppendStr):
    InFilename = InFilename.split(".")
    OrigName = ".".join(InFilename[:-1])
    return OrigName+AppendStr

def GenerateFirstFrame(outfile, Filename):
    return GenerateFrameN(outfile, Filename, 1)

def GenerateFrameN(outfile, Filename, frameNumber):
    video = imageio.get_reader(Filename, 'ffmpeg')
    frame = video.get_data(frameNumber)
    plt.imshow(frame)
    plt.savefig(AppendTitleToFilename(outfile, "Frame"+str(frameNumber)))
    plt.clf()
    return

def GeneratePlot(outfile, Filename, xpixel, ypixel, nyanFlag=0):

    video = imageio.get_reader(Filename, 'ffmpeg')
    colorArr = []
    maxLen = int(len(video))
    gradient = np.linspace(0,1,256)
    gradient = np.vstack((gradient, gradient))
    index = range(maxLen)

    #outfile = AppendTitleToFilename(outfile, "Trace")

    RGB = [[],[],[]] #0 - Red, 1 - Green, 2 - Blue

    progress = ""
    if(1 == nyanFlag):
       progress = NyanBar() 

    try:
        print "Starting Collection" + outfile
        for i in index:
            try:
                frame = video.get_data(i)
                pass

            except KeyboardInterrupt:
                print "\nEnding Collection" 
                break

            tempArr = frame[xpixel,ypixel] #Get the Frame at X=xpixel and Y=ypixel

            for j in range(3):
                RGB[j].append(float(tempArr[j])/256.0) #Normalizing the RGB values to 256 to get RGB value less than 1 for Matplotlib cmap
            colorArr.append([x[i] for x in RGB]) #Get the RGB values of the most recent entry and appent to colorArr

            if(nyanFlag):
                progress.update(int(float(i)/float(maxLen) * 100))

            #sys.stdout.write("\rFrame %i of %i" % (i, maxLen))
            #sys.stdout.flush()
          
        if(nyanFlag):
            progress.finish()
        #RGB Plots for Rates
        plt.plot(RGB[0], 'r')
        plt.plot(RGB[1], 'g')
        plt.plot(RGB[2], 'b')
        plt.savefig(AppendTitleToFilename(outfile, "RGB"))
        plt.clf()

        #Making Colorbar
        cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0) #Need normalized RGB to 256 therefore from 0 to 1
        gradient = np.linspace(0,1,256)
        gradient = np.vstack((gradient, gradient))
        plt.imshow(gradient, aspect='auto', cmap=cmap1)
        plt.savefig(outfile)
        plt.clf()
        return

    except KeyboardInterrupt:
        print "\nEnding Plot" 

parser = OptionParser()
parser.add_option('-f', "--FrameN", help="Generate frame N to look for pixel of interest", action="store")
parser.add_option('-o', "--outfile", help="Filename of output file for Gradient Image", action="store")
parser.add_option('-i', "--filename", help="Filename of file for processing", action="store")
parser.add_option('-x', "--xpixel", help="Location of X pixel", action="store")
parser.add_option('-y', "--ypixel", help="Location of Y pixel", action="store")
parser.add_option('-n', "--nyanFlag", help="Flag to set if use nyanbar", action="store_true", default=False)
options, args = parser.parse_args()

outfile=options.outfile
Filename=options.filename
xpixel=int(options.xpixel or 0)
ypixel=int(options.ypixel or 0)
FrameN=int(options.FrameN or 0)
nyanFlag=options.nyanFlag

##MAIN##
if FrameN != 0:
    GenerateFrameN(outfile, Filename, FrameN)
else:
    #GenerateRGBArray
    #GenerateColorPlot(RGBArr)
    #GenerateRGBPlot(RGBArr)
    GeneratePlot(outfile, Filename, xpixel, ypixel, nyanFlag)
