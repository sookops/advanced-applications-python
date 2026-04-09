import cv2

img = cv2.imread("images/shapes5.jpg")
img2 = img.copy()

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, binImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)

ctours, hier = cv2.findContours(binImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for con in ctours:
    # 전체 둘레의 0.05로 오차 범위 지정
    epsilon = 0.05 * cv2.arcLength(con, True)
    # 단순화된 외곽선 계산
    appr = cv2.approxPolyDP(con, epsilon, True)
    # 이미지에 외곽선 표시
    cv2.drawContours(img, [con], -1, (0,255,0), 3)
    cv2.drawContours(img2, [appr], -1, (0,255,0), 3)
    # 볼록 여부 판별
    print("외곽선 형태 :", "볼록" if cv2.isContourConvex(appr) else "오목")
  
# 결과 출력
cv2.imshow('contour', img)
cv2.imshow('approx', img2)
cv2.waitKey()
cv2.destroyAllWindows()
