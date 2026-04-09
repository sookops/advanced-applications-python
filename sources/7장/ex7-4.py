import cv2

img = cv2.imread("images/bufs.jpg")
org = img.copy()
cv2.imshow("BUFS", img)
color = (255, 0, 0)     # 파란색

def onMouse(event, x, y, flags, param):     # 마우스 콜백 함수 정의
    global prev, img                            # 전역 변수 선언
    if event == cv2.EVENT_LBUTTONDOWN:      # 왼쪽 버튼 누름
        prev = (x, y)                       # 그리기 시작 위치 저장
    elif event == cv2.EVENT_MOUSEMOVE:      # 마우스 이동
        if flags & cv2.EVENT_FLAG_LBUTTON:  # 왼쪽 버튼 누른 상태
            cv2.line(img, prev, (x,y), color, 2)    # 선 그리기
            prev = (x, y)                           # 현재 위치 저장
            cv2.imshow("BUFS", img)                 # 이미지 다시 표시
    elif event == cv2.EVENT_RBUTTONDOWN:
        img = org.copy()
        cv2.imshow("BUFS", img) 

cv2.setMouseCallback("BUFS", onMouse)        # 마우스 콜백 함수 등록
cv2.waitKey()
cv2.destroyAllWindows()



