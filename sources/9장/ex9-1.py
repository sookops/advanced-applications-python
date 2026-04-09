import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')
arr1 = np.full(img.shape, (0, 0, 50), dtype=np.uint8)	# 덧셈/뺄셈에 사용
arr2 = np.full(img.shape, (1, 1, 2), dtype=np.uint8)	# 곱셈/나눗셈에 사용

img1 = cv2.add(img, arr1)
img2 = cv2.subtract(img, arr1)
img3 = cv2.multiply(img, arr2)
img4 = cv2.divide(img, arr2)

cv2.imshow('original', img)
cv2.imshow('add', img1)
cv2.imshow('subtract', img2)
cv2.imshow('multiply', img3)
cv2.imshow('divide', img4)

cv2.waitKey()
cv2.destroyAllWindows()
