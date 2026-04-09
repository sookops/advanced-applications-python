import cv2

img = cv2.imread('images/shapes3.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 검은 배경에 흰색 전경의 이진화 이미지 생성
ret, binImg = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 외곽선 검출
ctours, hier = cv2.findContours(binImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("외곽선 개수: EXTERNAL =", len(ctours))

# 외곽선 크기 출력
for i in range(len(ctours)):
     print(i, ":", len(ctours[i]))

# 외곽선 개별 표시
COLOR = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]
for i in range(len(ctours)):
     cv2.drawContours(img, ctours, i, COLOR[i%len(COLOR)], 3)

# 결과 출력
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()

# shapes1~3.jpg
# EXTERNA:/LIST
