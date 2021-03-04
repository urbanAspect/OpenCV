import cv2
print('all packages imported')

img = cv2.imread('Resources/Will Smith.jpg')
print(img.shape)

#resize
imgResize = cv2.resize(img, (300, 300))
cv2.imshow('Resized image', imgResize)


#cropping
imgCropped = img[150:900, 100:900]
cv2.imshow('Cropped image', imgCropped)


cv2.waitKey(0)