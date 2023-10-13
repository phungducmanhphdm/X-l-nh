#Phùng Đức Mạnh
#N20DCCN040
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

# Đọc hình ảnh Lena và Peppers
lena = np.fromfile(current_script_dir + "lenabin.sec", dtype=np.uint8).reshape(256, 256)
peppers = np.fromfile(current_script_dir + "peppersbin.sec", dtype=np.uint8).reshape(256, 256)
# (a) Hiển thị hình ảnh Lena và Peppers
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(lena, cmap='gray')
plt.title('Hình ảnh Lena')
plt.subplot(1, 2, 2)
plt.imshow(peppers, cmap='gray')
plt.title('Hình ảnh Peppers')

# (b) Tạo hình ảnh mới J
J = np.zeros((256, 256), dtype=np.uint8)
J[:, :128] = lena[:, :128]
J[:, 128:] = peppers[:, 128:]
# (c) Tạo hình ảnh mới K bằng cách hoán đổi nửa trái và nửa phải của J
K = J.copy()
K[:, :128] = J[:, 128:]
K[:, 128:] = J[:, :128]
# Hiển thị hình ảnh J và K
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(J, cmap='gray')
plt.title('Hình ảnh J')

plt.subplot(1, 2, 2)
plt.imshow(K, cmap='gray')
plt.title('Hình ảnh K')

plt.show()


