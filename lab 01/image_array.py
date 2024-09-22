import cv2
import numpy as np
from pprint import pprint

image = cv2.imread('signature.jpeg')

image_array = np.array(image)

pprint(image_array.tolist())
