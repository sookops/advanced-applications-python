import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')

x = 50			 # 산술 연산에 사용할 값
img1 = img.copy()	

if x >= 0:
     img1[img1 > 255-x] = 255-x	# 덧셈의 보정
else:
     img1[img1 < -x] = -x

img1 = img1 + x 		# 산술 연산 수행

cv2.imshow('original', img)
cv2.imshow('add', img1)

cv2.waitKey()
cv2.destroyAllWindows()
