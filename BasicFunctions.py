import cv2
print("cv2 imported")
import numpy as np
print("Numpy imported")

print('All packages imported succesfuly')

img = cv2.imread("Resources\Elon Musk.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErodet = cv2.erode(imgCanny, kernel, iterations=1)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blurred Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Image', imgDialation)
cv2.imshow('Eroded Image', imgErodet)

cv2.waitKey(0)