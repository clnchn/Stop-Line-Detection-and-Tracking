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

'''

import cv2
import numpy as np
import math

#======= Helper Functions =======

def selectROI(edges):
	height, width = edges.shape
	mask = np.zeros_like(edges)

	#We shall only focus on the bottom half of the screen which are 	the lane and stop lane 
	polygon = np.array([[
        (0, height * 3 / 16),  #(0, height * 9 / 16), 
        (width, height * 6 / 16), #(width, height * 9 / 16),
        (width, height),
        (0, height),
    	]], np.int32)

    	cv2.fillPoly(mask, polygon, 255)
    	cropped_edges = cv2.bitwise_and(edges, mask)

	return cropped_edges



#======= Main =======

# Loads an image
#cv.samples.findFile(filename)<----Change Path otherwise stuff wont work

frame = cv2.imread('/home/celene/git_workspace/Stop-Line-Detection-and-Tracking/Test1.jpg')
scale_percent = 25 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)

frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

#Check if image is loaded fine
#if frame is None: 
#	print ('Unable to load image.')
#	return -1

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_lane = np.array([0, 0, 160])
upper_lane = np.array([40, 40, 230])
mask = cv2.inRange(hsv, lower_lane, upper_lane)
edges = cv2.Canny(mask, 200, 400)

#Parameters for Junction#2:
#lower_lane = np.array([0, 0, 160])
#upper_lane = np.array([40, 40, 230])

# Eliminate roadlines that are not inside the drivable surface based on segmentation. 

focus_edges = selectROI(edges)
lines = cv2.HoughLinesP(focus_edges,1,np.pi/180,80,minLineLength=100,maxLineGap=30)
#http://opencvexamples.blogspot.com/2013/10/line-detection-by-hough-line-transform.html
try:#for real time in case no lines detected
	for line in lines:
		x1,y1,x2,y2 = line[0]
		theta = line[0][1]-360
		print(theta)
		if theta > 170 or theta < 10:
		#if theta > np.pi/180 * 170 or theta < np.pi/180 * 10: #vertical lines
			cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
		elif theta > 10 and theta < 170: 
		#elif theta > np.pi/180 * 20 and theta < np.pi/180 * 160: #horizontal lines
			cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)
except: 
	pass
# Separate into stop lines and lane lines.



# Dashed Lines 

cv2.imwrite('/home/celene/git_workspace/Stop-Line-Detection-and-Tracking/result.jpg',frame)

cv2.imshow('hsv', hsv)
cv2.imshow('edges', focus_edges)
cv2.imshow('output', frame)
cv2.waitKey(50000)
cv2.imwrite('/home/celene/git_workspace/Stop-Line-Detection-and-Tracking/output.jpg',frame)


print("Program Ends")


