Project for Watonomous: An autonomous vehicle should be able to recognize a stop-line and stop at the detected stop-line. 

# Task Overview:

- Extracting lane lines using canny edge detection and hough transform
- Eliminate roadlines that are not inside the drivable surface based on segmentation.
- Separate into stop lines and lane lines.

The objective of this project is to try to develop a computer vision algorithm to detect the stop lines and track them over time. The successful completion of these tasks begins by the recognition of stoplines. It is important to note that lateral and longitudinal lane-markings for stop-lines and lane boundaries are not always visible because of occlusions by neighboring vehicles and other urban structures, and painting qualities.

Pipeline for stop-line recognition algorithm begins with lane-marking detection. Stop line is defined to be painted on roads that are orthogonal to the vehicle's travel direction. The width might vary but the colour and material are mostly identical to longitudinal lane-marking. 

In particular, we should seek for the lateral lane-marking that has the strongest orthogonal layout to longitudinal lane-markings, to detect a stop-line. 

A report available at: https://www.ri.cmu.edu/pub_files/2014/6/tech-report-ri-tr-14-09.pdf examines the method for autonomous vehicle to detect stoplines. 

Read this: https://towardsdatascience.com/deeppicar-part-4-lane-following-via-opencv-737dd9e47c96


  
