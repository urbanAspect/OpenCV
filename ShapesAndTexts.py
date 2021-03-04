import cv2
import numpy as np
print('all packages imported')

img = np.zeros((512, 512, 3), np.uint8)
img[100:412, 100:412] = 182, 252, 3

cv2.line(img, (100, 100), (412, 412), (0, 0, 0), 3)
cv2.line(img, (412, 100), (100, 412), (0, 0, 0), 3)
cv2.rectangle(img, (0, 0), (200,100), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (256,256), 50, (255, 255, 0), cv2.FILLED)
cv2.putText(img, 'OPENCV', (100, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 1)
cv2.imshow('image', img)

cv2.waitKey(0)