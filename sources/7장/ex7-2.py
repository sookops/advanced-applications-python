import cv2

img = cv2.imread("images/bufs.jpg")     
cv2.imshow("BUFS", img)         

def onMouse(event, x, y, flags, param):     # 마우스 콜백 함수 구현
    if event == cv2.EVENT_LBUTTONDOWN:      # 왼쪽 버튼 누름
        print(x, y)                         # 마우스 좌표 출력
        cv2.circle(img, (x,y), 30, (0,0,255), 5) # 원 그리기
        cv2.imshow("BUFS", img)             # 그려진 이미지를 다시 표시

cv2.setMouseCallback("BUFS", onMouse)       # 마우스 콜백 함수 등록
cv2.waitKey()
cv2.destroyAllWindows()
