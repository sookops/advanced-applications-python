import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')

x = 1.5	# 곱셈 연산에 사용할 값 (양수)
img3 = img.copy()
rows, cols = img3.shape[:2]

for i in range(rows):		# 곱셈의 수행
     for j in range(cols):
          for k in range(3):
               val = int(img3[i][j][k]*x)
               img3[i][j][k] = 255 if val > 255 else val

#img3 = cv2.multiply(img3, x)

cv2.imshow('original', img)
cv2.imshow('multiply', img3)

cv2.waitKey()
cv2.destroyAllWindows()
