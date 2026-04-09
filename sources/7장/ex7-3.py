import cv2

img = cv2.imread("images/bufs.jpg") 
cv2.imshow("BUFS", img)


# 색상 변수 
BLACK, BLUE, GREEN, RED = (0,0,0), (255,0,0), (0,255,0), (0,0,255)

def onMouse(event, x, y, flags, param): 	# 마우스 콜백 함수 
    color = BLACK
    if event == cv2.EVENT_LBUTTONDOWN:  	# 왼쪽 버튼 누름 
        print(x, y)		                # 마우스 좌표 출력						# 마우스 좌표  출력
        if flags & cv2.EVENT_FLAG_CTRLKEY : 	# Ctrl키 누른 상태
            color = RED
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : 	# Shift키 누른 상태
            color = BLUE
        elif flags & cv2.EVENT_FLAG_RBUTTON:
            color = (0, 255, 255)

        if flags & cv2.EVENT_FLAG_CTRLKEY and \
        flags & cv2.EVENT_FLAG_SHIFTKEY : 	# 둘 다 누른 상태
            color = GREEN

        cv2.circle(img, (x,y), 30, color, -1) 	# 원 그리기
        cv2.imshow("BUFS", img)          	# 그려진 이미지를 다시 표시

cv2.setMouseCallback("BUFS", onMouse)    	# 마우스 콜백 함수 등록
cv2.waitKey() 
cv2.destroyAllWindows()

