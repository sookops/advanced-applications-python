import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')

blur_img1 = cv2.blur(img, (3, 3))	# 커널 자동 생성
blur_img2 = cv2.blur(img, (5, 5))	# 커널 자동 생성

out_img = np.hstack((img, blur_img1, blur_img2))		
cv2.imshow('blur', out_img)
cv2.waitKey()
cv2.destroyAllWindows()

