import cv2, sys

cap = cv2.VideoCapture(0)	     	# 0번 카메라 장치 연결

print('원래 너비 =', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('원래 높이 =', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
     ret, frame = cap.read()		# 다음 프레임 읽기
     if not ret: break 		     	# 프레임을 읽을 수 없으면 종료
     cv2.imshow("Camera", frame)	# 프레임 영상을 화면에 표시
     if cv2.waitKey(1) == 27:  break	# ESC키를 누르면 종료

cap.release()        
cv2.destroyAllWindows()






