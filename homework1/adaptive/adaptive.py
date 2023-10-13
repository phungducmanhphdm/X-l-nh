#Phùng Đức Mạnh
#N20DCCN040
import cv2
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

filePaths = ['dental.jpg', 'parrot.jpg', 'skull.jpg']
l = len(filePaths)

for i in range(l):
    filePath = filePaths[i]
    # Load an image
    image = cv2.imread(current_script_dir + filePath, cv2.IMREAD_GRAYSCALE)
    #histigram image
    equalized_image = cv2.equalizeHist(image)
    # Apply adaptive histogram image 8x8
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized_image_8x8 = clahe.apply(image)
    # Apply adaptive histogram image 16x16
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))
    equalized_image_16x16 = clahe.apply(image)
    #show hình lên
    plt.subplot(3, 3, l*i+1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(3, 3, l*i+2)
    plt.title('8x8')
    plt.imshow(equalized_image_8x8, cmap='gray')
    plt.axis('off')

    plt.subplot(3, 3, l*i+3)
    plt.title('16x16')
    plt.imshow(equalized_image_16x16, cmap='gray')
    plt.axis('off')

plt.show()
