import cv2

# Read the image file
image = cv2.imread("messi.jpg")

# Resize
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the image file
cv2.imwrite("new_image.jpg", gray)

