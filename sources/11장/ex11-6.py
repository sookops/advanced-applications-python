import cv2
import numpy as np

img = cv2.imread('images/small_cat.jpg')
yMax, xMax = img.shape[0:2]	   # 영상의 크기

# 투시 변환 전 후 4개 좌표
pts1 = np.float32([[0, 0], [0, yMax], [xMax, yMax], [xMax, 0]])
pts2 = np.float32([[0, 0], [100, yMax], [xMax-50, yMax], [xMax, 0]])

# 투시 변환 행렬 계산과 투시 변환 수행
mtrx = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, mtrx, (xMax, yMax))

# 결과 출력
cv2.imshow("origin", img)
cv2.imshow('perspective', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
