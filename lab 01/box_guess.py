import cv2

image = cv2.imread('R.jpeg')


rowl, coll = 0, 0
rowr, colr = 60, 60


#image[rowl:rowr, coll:colr] = [0, 0, 255]

cv2.imwrite("man_with_red_box.jpeg", image)

for item in image:
    for it in item:
        print(it)