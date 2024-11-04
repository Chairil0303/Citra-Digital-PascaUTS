import numpy as np
import cv2 as cv

imgRgb = cv.imread('gambar/logoC.png')
imgGrayscale = cv.cvtColor(imgRgb, cv.COLOR_BGR2GRAY)

imgHSV = cv.cvtColor(imgRgb, cv.COLOR_BGR2HSV)

imgYCrCb = cv.cvtColor(imgRgb,  cv.COLOR_BGR2YCrCb)

imgY = imgYCrCb[:, :, 0]
imgCr = imgYCrCb[:, :, 1]
imgCb = imgYCrCb[:, :, 2]
print('Shape RGB: '+str(imgRgb.shape))
print('Shape Grayscale: '+str(imgGrayscale.shape))
print('Shape HSV:'+str(imgHSV.shape))
print('Shape YCbCr: '+str(imgYCrCb.shape))

cv.imwrite('Grayscale.jpg', imgGrayscale)
cv.imwrite('HSV.jpg', imgHSV)
cv.imwrite('YCbCr.jpg', imgYCrCb)
cv.imshow('RGB', imgCr)
cv.imshow('Grayscale', imgGrayscale)
cv.imshow('HSV', imgHSV)
cv.imshow('YCbCr', imgYCrCb)
cv.imshow('Y', imgY)
cv.imshow('Cb', imgCb)
cv.imshow('Cr', imgCr)
cv.waitKey(0)
cv.destroyAllWindows()
