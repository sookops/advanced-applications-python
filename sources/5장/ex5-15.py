import cv2

cap = cv2.VideoCapture(0)	# 0번 카메라 장치 연결

fps = cap.get(cv2.CAP_PROP_FPS)		     # 초당 프레임 수
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 너비 	
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 높이
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')	# 인코딩 포맷 설정

out = cv2.VideoWriter("myvideo.avi", fourcc, fps, (w, h)) # 출력 객체

while True:
     ret, img = cap.read()
     if not ret: break 
     cv2.imshow("Camera-recording", img)
     out.write(img)			      # 파일에 프레임 이미지 저장
     if cv2.waitKey(int(1000/fps)) == 27:     # ESC 키를 누르면 종료
          break
     
cap.release()
out.release()
cv2.destroyAllWindows() 




