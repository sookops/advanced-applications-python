import cv2
import numpy as np

img = cv2.imread('images/fish.jpg')
yMax, xMax = img.shape[:2]

# 변환 전, 후 각 3개의 점 좌표 설정
pts1 = np.float32([[50, 50], [200, 100], [100, 200]])
pts2 = np.float32([[80, 80], [180, 50], [110, 180]])

# 짝지은 3개의 점 좌표로 변환 행렬 계산
mtrx = cv2.getAffineTransform(pts1, pts2)

# 어파인 변환 행렬로 이미지 변환
dst = cv2.warpAffine(img, mtrx, (xMax, yMax))

# 이미지에 점 좌표 표시
pts1 = pts1.astype(np.uint8)       # 정수 좌표로 변환
pts2 = pts2.astype(np.uint8)

cv2.circle(img, pts1[0], 5, (255,0,0), -1)
cv2.circle(img, pts1[1], 5, (0,255,0), -1)
cv2.circle(img, pts1[2], 5, (0,0,255), -1)
cv2.circle(dst, pts2[0], 5, (255,0,0), -1)
cv2.circle(dst, pts2[1], 5, (0,255,0), -1)
cv2.circle(dst, pts2[2], 5, (0,0,255), -1)

# 결과 출력
cv2.imshow('origin',img)
cv2.imshow('affin', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

