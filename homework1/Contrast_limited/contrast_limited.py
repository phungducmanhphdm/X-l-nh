#Phùng Đức Mạnh
#N20DCCN040
import cv2
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

#read image
image = cv2.imread(current_script_dir + 'moon.jpg', cv2.IMREAD_GRAYSCALE)
#hình ảnh đã cân bằng sáng
equalized_image = cv2.equalizeHist(image)
#Biểu đồ sáng
image_histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
#Biểu đồ cân bằng sáng
equalized_image_histogram = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

plt.subplot(3, 3, 1)
plt.title('Histogram')
plt.xlabel('gray')
plt.ylabel('pixel')
plt.plot(image_histogram)
plt.xlim([0, 256])

plt.subplot(3, 3, 3)
plt.title('Equalized Histogram')
plt.xlabel('gray')
plt.ylabel('pixel')
plt.plot(equalized_image_histogram)
plt.xlim([0, 256])

plt.subplot(3, 3, 7)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')

plt.show()