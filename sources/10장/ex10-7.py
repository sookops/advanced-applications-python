import cv2
import numpy as np

img = cv2.imread("images/sudoku.jpg")

# 케니 에지 검출기 적용 
canny = cv2.Canny(img, 100, 200)

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny', canny)

cv2.waitKey()
cv2.destroyAllWindows()
