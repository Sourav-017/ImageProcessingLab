import cv2
import numpy as np


def calculate_histogram(image):

    histogram = [0] * 256
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram


def calculate_cdf(histogram, image_pixel_count):

    cdf = [0] * len(histogram)
    cdf[0] = histogram[0] / image_pixel_count
    for i in range(1, len(histogram)):
        cdf[i] = cdf[i - 1] + (255 * (histogram[i] / image_pixel_count))


    cdf_normalized = [round(value) for value in cdf]

    return cdf_normalized


def equalize_image(image, cdf):

    equalized_image = np.zeros_like(image)

    for i in range(len(image)):
        for j in range(len(image[0])):
            equalized_image[i][j] = cdf[image[i][j]]

    return equalized_image


def histogram_equalization(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    histogram = calculate_histogram(image)
    image_pixel_count = image.size
    cdf = calculate_cdf(histogram, image_pixel_count)
    equalized_image = equalize_image(image, cdf)


    cv2.imshow("Original Image", image)
    cv2.imshow("Equalized Image", equalized_image.astype(np.uint8))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


histogram_equalization('img_1.png')
