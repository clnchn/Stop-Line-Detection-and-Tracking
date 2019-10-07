import cv2
import numpy as np
import math


#def selectROI(edges):
#	height, width = edges.shape
#	mask = np.zeros_like(edges)

	#We shall only focus on the bottom half of the screen which are the lane and stop lane 
#	polygon = np.array([[
#        (0, height * 1 / 2),
#        (width, height * 1 / 2),
#        (width, height),
#        (0, height),
#    ]], np.int32)

#    cv2.fillPoly(mask, polygon, 255)
#    cropped_edges = cv2.bitwise_and(edges, mask)

#return croppededges


frame = cv2.imread('/home/celene/python_environment/stop-junction2.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([0, 0, 10])
upper_blue = np.array([200, 200, 150])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)


lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

# Eliminate roadlines that are not inside the drivable surface based on segmentation. Separate into stop lines and lane lines.

cv2.imshow('image', edges)
cv2.waitKey(2000)
cv2.imshow('image', frame)
cv2.waitKey(5000)


print("Hello World")


