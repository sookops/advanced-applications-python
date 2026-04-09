import cv2

img = cv2.imread("images/shapes1.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binImg = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 가장 바깥쪽 외곽선에 대해 모든 좌표를 저장
ctours, hier = cv2.findContours(binImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 도형의 외곽선에 대한 무게 중심 표시
for con in ctours:
     M = cv2.moments(con)	   # 모멘트 계산
     cx = int(M['m10']/M['m00'])   # 무게 중심 좌표 (cx, cy)
     cy = int(M['m01']/M['m00'])
     cv2.circle(img, (cx, cy), 5, (0,0,255), -1)

cv2.imshow('images', img)
cv2.waitKey()
cv2.destroyAllWindows()
