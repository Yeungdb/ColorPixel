#!/usr/bin/python

import skvideo.io
import skvideo.datasets

Filename = ""
#Filename = skvideo.datasets.bigbuckbunny()
video = skvideo.io.vread(Filename)

colorArr = []
for frame in video:
    tempArr = frame[300,300]
    temp2 = []
    temp2.append(float(tempArr[0])/256.0)
    temp2.append(float(tempArr[1])/256.0)
    temp2.append(float(tempArr[2])/256.0)
    colorArr.append(temp2)


import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

cmap1 = LinearSegmentedColormap.from_list("cmap", colorArr, N=256, gamma=1.0)
gradient = np.linspace(0,1,256)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap=cmap1)
plt.savefig("GRAD")



