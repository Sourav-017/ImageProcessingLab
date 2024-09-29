import cv2
import numpy as np
from pprint import pprint

image = cv2.imread('R.jpeg')

img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('output.jpg', img_grey)

image_array = np.array(img_grey)

image_array2 = np.array(image)

negative = 255 - image_array2

cv2.imwrite("colorneg_flower.jpeg", negative)

cv2.imwrite('gray_neg.jpeg', 255 - image_array2)