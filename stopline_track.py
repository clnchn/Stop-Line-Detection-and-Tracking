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
        (0, height * 5 / 8), 
        (width, height * 4 / 8),
        (width, height),
        (0, height),
    	]], np.int32)

    	cv2.fillPoly(mask, polygon, 255)
    	cropped_edges = cv2.bitwise_and(edges, mask)

	return cropped_edges


def average_slope_intercept(frame, line_segments):
    """
    This function combines line segments into one or two lane lines
    If all line slopes are < 0: then we only have detected left lane
    If all line slopes are > 0: then we only have detected right lane
    """
    lane_lines = []
    if line_segments is None:
        logging.info('No line_segment segments detected')
        return lane_lines

    height, width, _ = frame.shape
    left_fit = []
    right_fit = []


#These might need to be height for horizotal lines 
    boundary = 1/3
    left_region_boundary = width * (1 - boundary)  # left lane line segment should be on left 2/3 of the screen
    right_region_boundary = width * boundary # right lane line segment should be on left 2/3 of the screen


    for line_segment in line_segments:
        for x1, y1, x2, y2 in line_segment:
            if x1 == x2:
                logging.info('skipping vertical line segment (slope=inf): %s' % line_segment)
                continue
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                if x1 < left_region_boundary and x2 < left_region_boundary:
                    left_fit.append((slope, intercept))
            else:
                if x1 > right_region_boundary and x2 > right_region_boundary:
                    right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis=0)
    if len(left_fit) > 0:
        lane_lines.append(make_points(frame, left_fit_average))

    right_fit_average = np.average(right_fit, axis=0)
    if len(right_fit) > 0:
        lane_lines.append(make_points(frame, right_fit_average))

    logging.debug('lane lines: %s' % lane_lines)  # [[[316, 720, 484, 432]], [[1009, 720, 718, 432]]]

    return lane_lines

#======= Main =======

# Loads an image
#cv.samples.findFile(filename)<----Change Path otherwise stuff wont work

frame = cv2.imread('/home/celene/python_environment/stop-junction2.jpg')

#Check if image is loaded fine
#if frame is None: 
#	print ('Unable to load image.')
#return -1

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_lane = np.array([0, 0, 160])
upper_lane = np.array([40, 40, 230])
mask = cv2.inRange(hsv, lower_lane, upper_lane)
edges = cv2.Canny(mask, 200, 400)

#Parameters for Junction#2:
#lower_lane = np.array([0, 0, 160])
#upper_lane = np.array([40, 40, 230])

# Eliminate roadlines that are not inside the drivable surface based on segmentation. 

#focus_edges = selectROI(edges)

lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

# Separate into stop lines and lane lines.



cv2.imshow('image', edges)
cv2.imshow('image2', frame)
cv2.waitKey(50000)


print("Program Ends")


