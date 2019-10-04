This is another short project for Watonomous. 

An autonomous vehicle should be able to recognize a stop-line and stop at the detected stop-line

The successful completion of these tasks begins by the recognition of stoplines.
The objective of this project is to try to develop a computer vision algorithm to detect the stop lines and track them over time. 

A report available at: https://www.ri.cmu.edu/pub_files/2014/6/tech-report-ri-tr-14-09.pdf examines the method for autonomous vehicle to detect stoplines. 


It is important to note that lateral and longitudinal lane-markings for stop-lines and lane boundaries are not always visible because of occlusions by neighboring vehicles and other urban structures, and painting qualities.

Pipeline for stop-line recognition algorithm begins with lane-marking detection. 
Stop line is defined to be painted on roads that are orthogonal to the vehicle's travel direction. 
The width might vary but the colour and material are mostly identical to longitudinal lane-marking. 

In particular, we seek for the lateral lane-marking that has the strongest orthogonal layout to longitudinal lane-markings, to detect a stop-line. 


turn the color space used by the image, which is RGB (Red/Green/Blue) into the HSV (Hue/Saturation/Value) color space. (Read this for more details on the HSV color space.) The main idea behind this is that in an RGB image, different parts of the blue tape may be lit with different light, resulting them appears as darker blue or lighter blue.

However, in HSV color space, the Hue component will render the entire blue tape as one color regardless of its shading. It is best to illustrate with the following image. 

import cv2
frame = cv2.imread('/home/pi/DeepPiCar/driver/data/road1_240x320.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
https://towardsdatascience.com/deeppicar-part-4-lane-following-via-opencv-737dd9e47c96

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # only focus bottom half of the screen
    polygon = np.array([[
        (0, height * 1 / 2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges
    
    
    
    
    
