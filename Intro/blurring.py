import cv2

# Read the image file (defaults to rgb)
image = cv2.imread("messi.jpg")

# Blur the image
kernel = (5,5)
blurred = cv2.blur(image, kernel)
gaussian_blurred = cv2.GaussianBlur(image, kernel, 0)

# Thresholding
gray_blurred = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
THRESHOLD_VALUE = 127
ret, thresh = cv2.threshold(gray_blurred, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Gaussian Blurred", gaussian_blurred)
cv2.imshow("Blurred Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
