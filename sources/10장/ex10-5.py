import cv2
import numpy as np

img = cv2.imread("images/sudoku.jpg")

# 마스크 생성
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# 필터 적용
img1 = cv2.filter2D(img, -1, prewitt_x)
img2 = cv2.filter2D(img, -1, prewitt_y)

# 결과 출력
out_img = np.hstack((img, img1, img2, img1+img2)) 	
cv2.imshow('prewitt filter', out_img)

cv2.waitKey()
cv2.destroyAllWindows()





