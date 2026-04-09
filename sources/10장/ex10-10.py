import cv2
import numpy as np

img = cv2.imread("images/bad_rect.png", cv2.IMREAD_GRAYSCALE)

# 구조화 요소 커널 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# 열림과 닫힘 연산 적용
opening = cv2.dilate(cv2.erode(img, k), k)
closing = cv2.erode(cv2.dilate(img, k), k) 

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

cv2.waitKey()
cv2.destroyAllWindows()


