import cv2

img = cv2.imread("images/bufs.jpg")
cv2.imshow("BUFS", img)
start = end = (0,0)     # 관심 영역의 시작과 끝 좌표
isDone = False          # 작업 완료 여부

def onMouse(event, x, y, flags, param):     # 마우스 콜백 함수
    global start, end, isDone               # 전역 변수 선언
    if not isDone and event == cv2.EVENT_LBUTTONDOWN:  	# 왼쪽 버튼 누름
        start = (x, y)                      # 관심 영역 시작 위치 설정
    elif not isDone and event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:  # 마우스 드래그
            end = (x, y)	            # 관심 영역의 끝 위치 설정
            img2 = img.copy()               # 이미지 복사
            cv2.rectangle(img2, start, end, (0,0,255), 5)   # 사각형 설정
            cv2.imshow("BUFS", img2)    		    # 이미지 표시
    elif not isDone and event == cv2.EVENT_LBUTTONUP:       # 버튼 뗌
            print(start, end)		    # 좌표 출력
            isDone = True	            # 작업 완료

cv2.setMouseCallback("BUFS", onMouse)       # 마우스 콜백 함수 등록
cv2.waitKey()
cv2.destroyAllWindows()

