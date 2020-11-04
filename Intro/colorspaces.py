import cv2

# Read the image file (defaults to bgr)
bgr = cv2.imread("messi.jpg")

# Convert to various colorspaces
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

# Display the images
cv2.imshow("Original", bgr)
cv2.imshow("RGB", rgb)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)

# End the program after exited
cv2.waitKey(0)
cv2.destroyAllWindows()
