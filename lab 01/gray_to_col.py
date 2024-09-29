import cv2

image = cv2.imread('eagle.jpeg')


rowl, coll = 0, 0
rowr, colr = 100, 100

image[rowl:rowr, coll:colr] = [0, 0, 255]

cv2.imwrite("man_with_red_box.jpeg", image)
