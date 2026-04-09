import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')
rows, cols = img.shape[0:2]  # 영상의 크기

dx, dy = 100, 100            # 이동할 픽셀 거리

# 변환 행렬 생성 - (dx, dy)만큼 평행 이동 
mtrx = np.float32([[1, 0, dx], [0, 1, dy]])

# 변환 수행, 변환 후 여백을 기본값(검은색)으로 채움
dst1 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))   

# 변환 후 여백 부분을 녹색으로 채움
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), borderValue=(0,255,0))

# 변환 후 여백 부분을 이미지의 반복으로 채움
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), \
       borderMode=cv2.BORDER_WRAP)

cv2.imshow('original', img); cv2.imshow('dst1', dst1);
cv2.imshow('dst2', dst2); cv2.imshow('dst3', dst3);
cv2.waitKey(); cv2.destroyAllWindows()
