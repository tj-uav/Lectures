import cv2
import numpy as np

bg = cv2.imread( "4season.png" )
fg = cv2.imread( "opencv.png" )
fgmask = cv2.imread( "opencv_mask.png" )

# YOUR CODE HERE. EXPECTED OUTPUT: OPENCV LOGO PLACED ON TOP OF BACKGROUND
