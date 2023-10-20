import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Lấy đường dẫn đến thư mục chứa file Python đang thực thi
current_script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '\\'

if __name__ == "__main__":
    filePath = current_script_dir + "actontBinbin.sec"

    # Load the binary image
    image = np.fromfile(filePath, dtype=np.uint8).reshape(256,256)
    image2 = cv2.imread("t.png")
    image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
    # Define the template (you can adjust this to match your desired template)
    template = image2

    height, width = image2.shape

    # Use matchTemplate with method CV_TM_SQDIFF (Squared Difference)
    # 2 method nhận diện 2 chữ t ở 2 vị trí khác nhau
    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF_NORMED']
    posOfDectect = []

    # dùng 2 method để tìm vị trí của 2 chữ t trong hình với template là hình t.png
    for method in methods:
        method = eval(method)
        result = cv2.matchTemplate(image, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + width, top_left[1] + height)
        posOfDectect.append([top_left, bottom_right])

    # Chuyển đổi hình qua rgb để khoanh vùng hai chữ t vừa nhận diện bằng màu đỏ
    result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # khoanh vùng cho 2 chữ t vừa nhận diện được
    for pos in posOfDectect:
        cv2.rectangle(result, pos[0], pos[1], (255,0,0),1)

    # show hình ảnh lên
    plt.subplot(1,3,1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1,3,2)
    plt.imshow(image2, cmap='gray')
    plt.axis('off')

    plt.subplot(1,3,3)
    plt.imshow(result, cmap='gray')
    plt.axis('off')
    plt.show()