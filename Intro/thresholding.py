import cv2

# Read the image file (defaults to rgb)
image = cv2.imread("messi.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
THRESHOLD_VALUE = 127
ret, thresh = cv2.threshold(gray, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)

# Display the image
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
