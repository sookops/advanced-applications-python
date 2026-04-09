import cv2
import numpy as np

img = cv2.imread('images/cat.bmp')

# 마스크 만들기
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.circle(mask, (370,230), 120, 255, -1)

# 마스킹
masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey()
cv2.destroyAllWindows()
