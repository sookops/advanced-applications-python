import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')
rows, cols = img.shape[0:2]  # 영상의 크기

sx, sy = 1.5, 1.5            # 확대/축소 비율

# 변환 행렬 생성 - (sx, sy)만큼 확대 또는 축소 
mtrx = np.float32([[sx, 0, 0],	[0, sy, 0]])	

# 변환 수행, 다양한 보간법 알고리즘 적용 
dst1 = cv2.warpAffine(img, mtrx, (int(cols*sx), int(rows*sy)))  # LINEAR 
dst2 = cv2.warpAffine(img, mtrx, (int(cols*sx), int(rows*sy)), \
       flags=cv2.INTER_NEAREST)    # NEAREST
dst3 = cv2.warpAffine(img, mtrx, (int(cols*sx), int(rows*sy)), \
       flags=cv2.INTER_AREA)       # AREA
dst4 = cv2.warpAffine(img, mtrx, (int(cols*sx), int(rows*sy)), \
       flags=cv2.INTER_CUBIC)      # CUBIC
dst5 = cv2.warpAffine(img, mtrx, (int(cols*sx), int(rows*sy)), \
       flags=cv2.INTER_LANCZOS4)   # LANCZOS4

cv2.imshow('original', img); cv2.imshow('linear', dst1);
cv2.imshow('nearest', dst2); cv2.imshow('area', dst3);
cv2.imshow('cubic', dst4); cv2.imshow('lanczos4', dst5);
cv2.waitKey(); cv2.destroyAllWindows()
