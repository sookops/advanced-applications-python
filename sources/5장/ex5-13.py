import cv2, sys

cap = cv2.VideoCapture("images/sample.avi")	# 비디오 파일 불러오기
fps = cap.get(cv2.CAP_PROP_FPS)         # 초당 프레임 수 
#delay = round(1000/fps * 0.5)           # 2배속 재생을 위한 지연 시간
delay = round(25)


while True:
     ret, frame = cap.read()		# 다음 프레임 읽기
     if not ret: break 		     	# 프레임을 읽을 수 없으면 종료
     cv2.imshow("Camera", frame)	# 프레임 영상을 화면에 표시
     if cv2.waitKey(delay) == 27:  	# delay 시간 대기, ESC키를 누르면 종료
     #if cv2.waitKey(1) == 27:
          break
     
cap.release()  
cv2.destroyAllWindows()






