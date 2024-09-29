import cv2
import numpy as np


image = cv2.imread('man_convert_grey.jpeg')


image_array = np.array(image)
neg = []


for row in image_array:
    neg_row = []
    for pixel in row:
        r = int(pixel[2])
        g = int(pixel[1])
        b = int(pixel[0])

        gray = int(r * 0.3 + g * 0.59 + b * 0.11)
        neg_row.append(gray)


    neg.append(neg_row)

neg_array = np.array(neg)


cv2.imwrite("man_convert_grey.jpeg", neg_array)


