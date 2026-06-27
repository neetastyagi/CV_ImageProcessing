import cv2
import numpy as np

# Load image, create mask, and draw white circle on mask
image = cv2.imread("ps1-1-a-1.png")
image2 = cv2.imread("ps1-1-a-2.png")
center = (75,100)
radius = 50
mask = np.zeros(image.shape, dtype=np.uint8)
mask = cv2.circle(mask, (100, 75), 50, (255,255,255), -1)



# Mask input image with binary mask
result = cv2.bitwise_and(image, mask)
# Color background white
#result[mask==0] = 255 # Optional

result = result[center[0]-50:center[0]+50,center[1]-50:center[1]+50]

mask = np.zeros(image2.shape, dtype=np.uint8)
mask = cv2.circle(mask, (75, 100), 50, (255,255,255), -1)
#image2 = cv2.bitwise_or(image2,mask)

mask1 = cv2.bitwise_not(mask)

cv2.imshow('mask1', mask1)

image2 = cv2.bitwise_and(image2,mask1)



mask[50:150,25:125] = result

result = cv2.bitwise_or(image2,mask)

result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

#result = cv2.add(image2,mask)

cv2.imshow('image', image2)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()
