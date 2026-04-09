import cv2
    
cap = cv2.VideoCapture("images/sample.avi")  # 비디오 파일 불러오기

if not cap.isOpened():			# 파일을 불러올 수 없으면 종료
     print("Can't open video");
     sys.exit()

while True:
     ret, img = cap.read()		# 다음 프레임 읽기
     if not ret: break 		        # 프레임을 읽을 수 없으면 종료
     cv2.imshow("Sample", img)	        # 프레임 영상을 화면에 표시
     if cv2.waitKey(25) == 27:     	# 25ms 대기, ESC키를 누르면 종료
          print('현재 재생 시간(초) :', round(cap.get(cv2.CAP_PROP_POS_MSEC)/1000,2))
          print('현재 프레임 번호 :', cap.get(cv2.CAP_PROP_POS_FRAMES))
          break

cap.release()                 	   
cv2.destroyAllWindows()





