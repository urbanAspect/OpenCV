import cv2
print("cv2 imported")
import numpy as np
print("Numpy imported")


img1 = cv2.imread("Resources\Elon Musk.jpg")
img2 = cv2.imread("Resources\Will Smith.jpg")
print(img1.shape)
print(img2.shape)

img1 = img1[150:870, 100:820]
img2 = cv2.resize(img2, (720, 720))

hor = np.hstack((img2, img1))
ver = np.vstack((img1, img2))



cv2.imshow('Horizontal', hor)
cv2.imshow('Vertical', ver)


cv2.waitKey(0)