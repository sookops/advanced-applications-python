import cv2
    
cap = cv2.VideoCapture("images/sample.avi")
print('너비 =', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('높이 =', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('초당 프레임 수 =', cap.get(cv2.CAP_PROP_FPS))
print('총 프레임 수 =', cap.get(cv2.CAP_PROP_FRAME_COUNT))
      
cap.release()                 		# 캡처 자원 반납
cv2.destroyAllWindows()




