import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')

# NumPy 브로드캐스팅 연산
img1 = img + 50		# 덧셈 수행
img2 = img - 50		# 뺄셈 수행
img3 = img * 2		# 곱셈 수행
img4 = img // 2		# 나눗셈 수행

cv2.imshow('original', img)
cv2.imshow('add', img1)
cv2.imshow('subtract', img2)
cv2.imshow('multiply', img3)
cv2.imshow('divide', img4)

cv2.waitKey()
cv2.destroyAllWindows()
