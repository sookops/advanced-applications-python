import cv2
import numpy as np

img1 = cv2.imread('images/robot_arm1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/robot_arm2.jpg', cv2.IMREAD_GRAYSCALE)

# 절대값 차 연산
diff = cv2.absdiff(img1, img2) 
 
# 차 영상의 결과를 빨간색으로 표시
spot = cv2.imread('images/robot_arm1.jpg')
spot[diff > 0] = [0,0,255]

# 결과 영상 출력
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('spot', spot)
cv2.waitKey()
cv2.destroyAllWindows()
