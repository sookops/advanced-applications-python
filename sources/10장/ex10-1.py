import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')

#kernel1 = np.ones((3,3))/9		# 커널 생성
kernel1 = np.ones((3,3))/15
img1 = cv2.filter2D(img, -1, kernel1)	# 필터링 수행

#kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # 커널 생성
kernel2 = np.array([[0, -2, 0], [-2, 10, -2], [0, -2, 0]])
img2 = cv2.filter2D(img, -1, kernel2)			   # 필터링 수행

out_img = np.hstack((img, img1, img2))	# 이미지 수평 병합
cv2.imshow('blur and sharpen', out_img)
cv2.waitKey()
cv2.destroyAllWindows()

