import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

def getImage256(filePath):
    image_data = np.fromfile(filePath, dtype=np.uint8)
    image_data = image_data.reshape(512, 512)
    odd_rows_and_cols = image_data[::2, ::2]
    return odd_rows_and_cols

def binaryImage(imageArr):
    threshold_value = 128
    _, binary_image = cv2.threshold(imageArr, threshold_value, 255, cv2.THRESH_BINARY)
    binary_image[binary_image == 0] = 0x00
    binary_image[binary_image == 255] = 0xff
    return binary_image


if __name__ == "__main__":
    filePath = current_script_dir + "mammogrambin.sec"
    binary_image = binaryImage(getImage256(filePath))
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')
    plt.show()


