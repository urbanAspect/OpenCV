import cv2
import numpy as np

img1 = cv2.imread("Resources/Elon Musk.jpg")
img2 = cv2.imread("Resources/Will Smith.jpg")

print(img1)
print(img2)


img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow('vertical', ver)
cv2.imshow('horizontal', hor)

cv2.waitKey(0)