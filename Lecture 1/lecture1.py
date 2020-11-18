#!/usr/bin/env python3

import cv2
import numpy as np

def wTMP( img ):
	cv2.imwrite( "t.png", img )

l = cv2.imread( "left.png" )
r = cv2.imread( "right.png" )

wTMP( cv2.bitwise_not( l ) )
wTMP( cv2.bitwise_or( l, r ) )
wTMP( cv2.bitwise_and( l, r ) )
wTMP( cv2.bitwise_xor( l, r ) )

ocv = cv2.imread( "opencv.png" )
ocvm = cv2.imread( "opencv_mask.png" )

wTMP( cv2.bitwise_not( ocv ) )
wTMP( cv2.bitwise_or( ocv, r ) )
wTMP( cv2.bitwise_and( ocv, r ) )
wTMP( cv2.bitwise_xor( ocv, r ) )

# Now complete the following task: recreate