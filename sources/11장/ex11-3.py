import cv2
import numpy as np

img = cv2.imread('images/small_lenna.jpg')

# 크기 지정으로 축소
rows, cols = img.shape[0:2]  # 영상의 크기
outSize = int(cols*0.5), int(rows*0.5)	# 출력 영상의 크기 (width, height)
dst1 = cv2.resize(img, outSize, None, 0, 0, cv2.INTER_AREA)

# 배율 지정으로 확대
dst2 = cv2.resize(img, None, None, 2, 2, cv2.INTER_CUBIC)
	
# 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

