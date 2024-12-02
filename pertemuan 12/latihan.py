import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('unpam.png', cv.IMREAD_COLOR)

plt.subplot(1, 3, 1), plt.hist(img[:, :, 0].ravel(), 256, [0, 256], color='b')
plt.subplot(1, 3, 2), plt.hist(img[:, :, 1].ravel(), 256, [0, 256], color='g')
plt.subplot(1, 3, 3), plt.hist(img[:, :, 2].ravel(), 256, [0, 256], color='r')

plt.show()
