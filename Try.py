import numpy
import cv2


#saff = cv2.imread("southafricaflagface.png")
saff = cv2.imread("fruit.png")


cv2.imshow('original',saff)
cv2.waitKey(0)



blue_channel = saff[:,:,0] 
green_channel = saff[:,:,1] 
red_channel = saff[:,:,2]

saff_gs = cv2.cvtColor(saff, cv2.COLOR_BGR2GRAY)

cv2.imshow('blue_channel',blue_channel)
cv2.imshow('green_channel',green_channel)
cv2.imshow('red_channel',red_channel)
cv2.imshow('grayscale',saff_gs)

print(saff_gs)
print(red_channel)
print(green_channel)
print(blue_channel)

cv2.waitKey(0)









