#Phùng Đức Mạnh
#N20DCCN040
import cv2
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

# Đọc hình ảnh "lenagray.jpg"
J1 = cv2.imread(current_script_dir + "lenagray.jpg", cv2.IMREAD_GRAYSCALE)

# Tạo hình ảnh mới J2 là bản âm của J1
J2 = 255 - J1

# Hiển thị hình ảnh J2
cv2.imshow("Hình ảnh J2", J2)
cv2.waitKey(0)

# Sử dụng imwrite để lưu J2 dưới dạng tệp JPEG
cv2.imwrite("J2.jpg", J2)