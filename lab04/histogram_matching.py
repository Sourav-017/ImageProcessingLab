import cv2
import numpy as np

def calculate_histogram(image):
    histogram = [0] * 256
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram

def calculate_cdf(histogram):
    cdf = np.cumsum(histogram)
    cdf_normalized = cdf * (255 / cdf[-1])
    return cdf_normalized


def apply_histogram_matching(source_image, reference_image):
    source_histogram = calculate_histogram(source_image)
    reference_histogram = calculate_histogram(reference_image)

    source_cdf = calculate_cdf(source_histogram)
    reference_cdf = calculate_cdf(reference_histogram)

    mapping = np.zeros(256, dtype=np.uint8)

    for i in range(256):

        min_diff = float('inf')
        closest_value = 0


        for j in range(256):
            diff = abs(reference_cdf[j] - source_cdf[i])
            if diff < min_diff:
                min_diff = diff
                closest_value = j

        mapping[i] = closest_value

    matched_image = cv2.LUT(source_image, mapping)
    return matched_image

def histogram_matching(source_image_path, reference_image_path, output_image_path):
    source_image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)
    reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)

    matched_image = apply_histogram_matching(source_image, reference_image)

    cv2.imwrite(output_image_path, matched_image)

    cv2.imshow("Source Image", source_image)
    cv2.imshow("Reference Image", reference_image)
    cv2.imshow("Matched Image", matched_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
histogram_matching('img_1.png', 'rose.jpg', 'matched_image.png')
