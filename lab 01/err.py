import cv2
import numpy as np
from pprint import pprint

from color_to_grayscale import negative

image = cv2.imread('R.jpeg')

image_array = np.array(image)
neg = []


for col1 in image_array:
    neg2 = []
    for col2 in col1:
        r = int(col2[2])
        g = int(col2[1])
        b = int(col2[0])
        neg2.append((int)(r * .3 + g *.59 + b * .11))

    neg.append(neg2)

neg_array = np.array(neg)
print(neg_array)
cv2.imwrite("man_convert_neg.jpeg", neg_array)