import numpy as np
import matplotlib as Plt

import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('unpam.png', 0)

hist_full = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist_full)
plt.xlim(0, 256)

plt.show()
