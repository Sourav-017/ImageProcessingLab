import cv2
import numpy as np

gray_image = cv2.imread("snake.jpeg", cv2.IMREAD_GRAYSCALE)

gamma = 1.5

c = 1

im_array = np.array(gray_image)

new_image = []

for i in im_array:
    list1 = []
    for j in i:
        val = int(j)

        gamma_transformed = c * ((val / 255.0) ** gamma) * 255

        mv = int(gamma_transformed)
        list1.append(mv)

    new_image.append(list1)

img_array = np.array(new_image, dtype=np.uint8)

cv2.imwrite("GammaTransform.jpeg", img_array)

image = cv2.imread("GammaTransform.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gamma Transformed Image1", gray_image)
cv2.imshow("Gamma Transformed Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
