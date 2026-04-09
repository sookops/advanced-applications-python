import cv2
import numpy as np

img = cv2.imread("images/morph_test.jpg", cv2.IMREAD_GRAYSCALE)

# 구조화 요소 커널 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# 팽창 연산 적용
dilation = cv2.dilate(img, k)

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('dilation', dilation)
cv2.waitKey()
cv2.destroyAllWindows()



