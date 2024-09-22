import cv2
import numpy as np
from pprint import pprint

image = cv2.imread('eagle.jpeg')

img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("window", img_grey)
cv2.waitKey(0)

image_array = np.array(img_grey)

pprint(image_array.tolist())