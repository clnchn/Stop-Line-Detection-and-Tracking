'''
#======= DESCRIPTION =======

This is only a test program for stop and lane line detection so a local image will be used as the input.
Normal method for extracting lane lines using canny edge detection and hough transform is used. 
The roadlines that are not inside the drivable surface based on segmentation are removed from the ROI. 
The stop lines and lane lines are then separated into different colours. 

To Use:
1) Set fileName to the name of the image being transformed.
2) Ensure the image and this file are in the same folder.
3) Run the program.
4) A Select ROI box will appear. Select a point or rectangular region that
    captures the top left marker on the ground. Press space.
5) Another Select ROI box will appear. Do the same thing, but for the top right
    marker. Repeat twice more for the bottom right and bottom left markers, in
    that order.
6) A final Select ROI box will appear. Select the rectangular region which will
    define the 4 corners of the dst points. When this region is selected, press
    space again.
7) Two images will be output. First, "fileName_transformed.png" will contain
    the transformed image. Second, "fileName_pts_shown.png" will show the src
    and dst points you selected in red and green, respectively.
'''

import cv2
import numpy as np
import math

#======= Helper Functions =======

def selectROI(edges):
	height, width = edges.shape
	mask = np.zeros_like(edges)

	#We shall only focus on the bottom half of the screen which are the lane and stop lane 
	polygon = np.array([[
        (0, height * 1 / 2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)

return croppededges

#======= Main =======

frame = cv2.imread('/home/celene/python_environment/stop-junction3.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([0, 0, 10])
upper_blue = np.array([200, 200, 100])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)


lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

# Eliminate roadlines that are not inside the drivable surface based on segmentation. 


# Separate into stop lines and lane lines.

cv2.imshow('image', edges)
#cv2.imshow('image', frame)
cv2.waitKey()


print("Hello World")


