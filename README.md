![](https://raw.githubusercontent.com/Yeungdb/ColorPixel/blob/master/ColorPixel.png)

# ColorPixel 

## Darien Yeung (@Yeungdb)
University of Victoria, McIndoe Group

## Background

ColorPixel is a lightweight Python application for making colorbars from collecting single pixel from an input video. Leveraging imageio's capabilities for video frame extraction and obtaining the RGB values from the individual frame, the colors are stitched together via matplotlib to construct a colorbar plot. 

Developed for the original intent of monitoring the color change in a chemical reaction with a smart phone camera, ColorPixel is able to plot the color change over time as a colormetric chronograph (or colorbar) as per discussed in this paper: 

   {INSERT LINK TO TITANOCENE PAPER}

## Quickstart
For Linux Users:

`pip install requirements.txt`

`python ColorPixel.py -f [InputVideoFile]`

## Dependencies

 - Imageio
 - Matplotlib

## Contact

Twitter: https://twitter.com/Yeungdb


