#Phùng Đức Mạnh
#N20DCCN040
import cv2
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

# Đọc hình ảnh màu "lena512color.jpg"
J1 = cv2.imread(current_script_dir + "lena512color.jpg")

# Tạo hình ảnh màu mới J2 bằng cách hoán đổi các băng màu
J2 = J1.copy()
J2[:, :, 0] = J1[:, :, 2]  # Red band 2 = Blue band 1
J2[:, :, 1] = J1[:, :, 0]  # Green band 2 = Red band 1
J2[:, :, 2] = J1[:, :, 1]  # Blue band 2 = Green band 1

# Hiển thị hình ảnh J2
cv2.imshow("Hình ảnh J2", J2)
cv2.waitKey(0)

# Sử dụng imwrite để lưu J2 dưới dạng tệp JPEG
cv2.imwrite("J2_color.jpg", J2)
