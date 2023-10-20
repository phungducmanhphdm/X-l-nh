import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

if __name__ == "__main__":
    filePath = current_script_dir + "ladybin.sec"
    image = np.fromfile(filePath, dtype=np.uint8).reshape(256,256)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Minimum and maximum pixel values
    min_value = image.min()
    max_value = image.max()

    # Full-scale contrast stretching
    stretched_image = ((image - min_value) / (max_value - min_value) * 255).astype('uint8')

    # Plot the histogram of the stretched image
    plt.subplot(3,2,1)
    plt.hist(image.ravel(), 256, [0, 256])
    plt.axis('off')
    

    plt.title('Histogram of Original Image')
    plt.subplot(3,2,2)
    plt.imshow(image, cmap='gray')
    plt.axis('off')


    plt.subplot(3,2,5)
    plt.hist(stretched_image.ravel(), 256, [0, 256])
    plt.axis('off')

    plt.title('Histogram of Stretched Image')

    plt.subplot(3,2,6)
    plt.imshow(stretched_image, cmap='gray')
    plt.axis('off')

    plt.show()
    exit(0)