import cv2
import numpy as np

img = cv2.imread('alphabet.jpg',0)
og = cv2.imread('alphabet.jpg')
retval, threshold = cv2.threshold(img, 237, 255, cv2.THRESH_BINARY) # anything greater than 12 1 "white" anything below 12 will be black
cv2.imshow('original',og)
cv2.imshow('threshold',threshold)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
