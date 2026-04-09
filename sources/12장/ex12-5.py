import cv2

img = cv2.imread("images/shapes1.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binImg = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 가장 바깥쪽 외곽선에 대해 모든 좌표를 저장
ctours, hier = cv2.findContours(binImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 도형의 외곽선에 대한 둘레 길이와 면적 출력
for con in ctours:
    length = cv2.arcLength(con, True)     # 영역 둘레 길이
    area = cv2.contourArea(con, False)    # 영역 넓이
    # 둘레 길이와 넓이 출력
    print("length = %.2f, area = %.2f" % (length, area))

cv2.imshow('images', img)
cv2.waitKey()
cv2.destroyAllWindows()
