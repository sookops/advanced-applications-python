import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')

blur1 = cv2.GaussianBlur(img, (5,5), 0)
blur2 = cv2.GaussianBlur(img, (5,5), 0.3)
blur3 = cv2.GaussianBlur(img, (5,5), 2)

# 결과 출력
img1 = np.hstack((img, blur1))	   # 수평 병합		
img2 = np.hstack((blur2, blur3))
out_img = np.vstack((img1, img2))  # 수직 병합
cv2.imshow('gaussian', out_img)

cv2.waitKey()
cv2.destroyAllWindows()


