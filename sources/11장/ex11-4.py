import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')
yMax, xMax = img.shape[0:2]  # 영상의 크기 (행크기, 열크기)

# 회전 변환 행렬 생성1 (회전축: 중앙, 각도: 45, 배율: 0.5)
m45 = cv2.getRotationMatrix2D((xMax/2, yMax/2), 45, 0.5)

# 회전 변환 행렬 생성2 (회전축: 중앙, 각도: 90, 배율: 1.5)
m90 = cv2.getRotationMatrix2D((xMax/2, yMax/2), 90, 1.5)

# 변환 행렬 적용
img1 = cv2.warpAffine(img, m45, (xMax+50, yMax+50), borderValue=(255,255,255))
img2 = cv2.warpAffine(img, m90, (yMax+50, xMax+250))

cv2.imshow('origin', img)
cv2.imshow("45", img1)
cv2.imshow("90", img2)
cv2.waitKey()
cv2.destroyAllWindows()

