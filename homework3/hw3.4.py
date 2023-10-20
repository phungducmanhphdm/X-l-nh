import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

filePath = current_script_dir + "johnnybin.sec"
# Load the "johnny.bin" image
image = np.fromfile(filePath, dtype=np.uint8).reshape(256,256)

# Plot the histogram of the original image
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Plot the histogram of the equalized image
plt.subplot(2, 2, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Show the original and equalized images
plt.subplot(2, 2, 3)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
