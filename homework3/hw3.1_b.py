import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

#kernal làm nét hình ảnh
kernel_0 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

#kernal lấy viền
kernel_1 = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])


#đọc hình ảnh từ file kích thước gốc 512x512 chuyền thành 256x256
def getImage256(filePath):
    image_data = np.fromfile(filePath, dtype=np.uint8)
    image_data = image_data.reshape(512, 512)
    odd_rows_and_cols = image_data[::2, ::2]
    return odd_rows_and_cols

if __name__ == "__main__":
    filePath = current_script_dir + "mammogrambin.sec"
    image = getImage256(filePath)
    filtered_image = cv2.filter2D(image, -1, kernel_0)
    filtered_image = cv2.filter2D(filtered_image, -1, kernel_1)
    print(filtered_image)
    cv2.imwrite('output_image.png', filtered_image)
    plt.imshow(filtered_image, cmap='gray')
    plt.axis('off')
    plt.show()


