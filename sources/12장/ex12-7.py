import cv2

img = cv2.imread("images/lightning.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binImg = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('aa', binImg)
ctours, hier = cv2.findContours(binImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for con in ctours:
    # 외접 직사각형 표시(빨간색)
    x,y,w,h = cv2.boundingRect(con)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

    # 외접원 표시(파랑색)
    (x,y), radius = cv2.minEnclosingCircle(con)
    cv2.circle(img, (int(x), int(y)), int(radius), (255,0,0), 2)

    # 볼록 외피 표시(초록색)
    hull = cv2.convexHull(con)
    cv2.drawContours(img, [hull], 0, (0,255,0), 2)

# 결과 출력
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()
