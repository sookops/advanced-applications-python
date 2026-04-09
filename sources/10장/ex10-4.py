import cv2
import numpy as np

img = cv2.imread('images/noise.jpg')

dst1 = cv2.medianBlur(img, 3)
dst2 = cv2.medianBlur(img, 5)
dst3 = cv2.medianBlur(img, 7)

# 결과 출력
img1 = np.hstack((img, dst1))			
img2 = np.hstack((dst2, dst3))
out_img = np.vstack((img1, img2))	
cv2.imshow('median', out_img)

cv2.waitKey()
cv2.destroyAllWindows()



