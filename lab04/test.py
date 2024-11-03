import cv2
import numpy as np

def calculate_histogram(image):
    """Calculate the histogram of a grayscale image."""
    histogram = [0] * 256 
    for row in image:
        for pixel in row:
            histogram[pixel] += 1  
    return histogram

def calculate_cdf(histogram, image_pixel_count):
    """Calculate a normalized cumulative distribution function (CDF) for histogram equalization."""
    cdf = [0] * len(histogram)
    cdf[0] = 255 * (histogram[0] / image_pixel_count)  # Initialize with the first intensity level

    # Calculate cumulative distribution with normalization at each step
    for i in range(1, len(histogram)):
        cdf[i] = cdf[i - 1] + 255 * (histogram[i] / image_pixel_count)

    # Round each CDF value to fit within valid pixel intensities
    cdf_normalized = [round(val) for val in cdf]
    return cdf_normalized

def equalize_image(image, cdf):
    """Map the original image pixels to equalized values using the CDF."""
    equalized_image = [[0] * len(image[0]) for _ in range(len(image))]  

    for i in range(len(image)):
        for j in range(len(image[0])):
            equalized_image[i][j] = cdf[image[i][j]]
    
    return equalized_image

def histogram_equalization(image_path):
    """Perform histogram equalization on a grayscale image using OpenCV to load the image."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    histogram = calculate_histogram(image)

    cdf = calculate_cdf(histogram)

    equalized_image = equalize_image(image, cdf)

    equalized_image_np = cv2.merge((cv2.UMat(np.array(equalized_image, dtype='uint8')).get(),))

    cv2.imshow("Original Image", image)
    cv2.imshow("Equalized Image", equalized_image_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
histogram_equalization('eagle.jpeg')
