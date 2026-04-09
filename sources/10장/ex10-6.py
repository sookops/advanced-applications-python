import cv2
import numpy as np

img = cv2.imread("images/sudoku.jpg")

# 소벨 필터 적용
img1 = cv2.Sobel(img, -1, 1, 0, ksize=3)
img2 = cv2.Sobel(img, -1, 0, 1, ksize=3)

# 샤르 필터 적용
img3 = cv2.Scharr(img, -1, 1, 0)
img4 = cv2.Scharr(img, -1, 0, 1)

# 라플라시안 필터 적용
img5 = cv2.Laplacian(img, -1)

# 결과 출력
out_img = np.hstack((img, img1, img2, img1+img2)) 	
cv2.imshow('sobel filter', out_img)
out_img = np.hstack((img, img3, img4, img3+img4)) 	
cv2.imshow('scharr filter', out_img)
out_img = np.hstack((img, img5)) 	
cv2.imshow('Laplacian filter', out_img)
cv2.waitKey()
cv2.destroyAllWindows()


