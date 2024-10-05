import cv2
import numpy as np


gray_image = cv2.imread("graylevel6.jpeg", cv2.IMREAD_GRAYSCALE)

c = 80

im_array = gray_image

new_image1 = []
new_image2 = []

for i in im_array:
    list1 = []
    list2 = []
    for j in i:
        val = int(j)
        log_transformed = c * np.log(1 + val)
        # print(log_transformed)
        # Scaling
        mv = int((255 * log_transformed) / (8 * c))
        # print(mv)
        list1.append(log_transformed)
        list2.append(mv)

    new_image1.append(list1)
    new_image2.append(list2)

img_array1 = np.array(new_image1)
img_array2 = np.array(new_image2)

cv2.imwrite("LogTransform.jpeg", img_array1)
cv2.imwrite("ScaledLogTransform.jpeg", img_array2)

image1 = cv2.imread("LogTransform.jpeg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("ScaledLogTransform.jpeg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("main ", gray_image)
cv2.imshow("abc ", image1)
cv2.imshow(" def", image2)


cv2.waitKey(0)
cv2.destroyAllWindows()
