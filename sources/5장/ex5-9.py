import cv2, sys

cap = cv2.VideoCapture(0)	     	# 0번 카메라 장치 연결

if not cap.isOpened():		     	# 카메라 장치와 연결할 수 없으면 종료
     print("Can't open camera");
     sys.exit()

while True:
     ret, frame = cap.read() 		# 카메라 프레임 읽기
     if not ret: break             	# 프레임을 읽을 수 없으면 종료
     cv2.imshow("Camera", frame)	# 화면에 표시
     if cv2.waitKey(1) == 27:     	# 1ms 대기, ESC 키를 누르면 종료
          break

cap.release() 
cv2.destroyAllWindows()	






