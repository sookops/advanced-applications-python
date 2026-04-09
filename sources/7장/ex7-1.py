import cv2

img = cv2.imread('images/cat.bmp')

x, y = 100, 100      # 출력창의 최초 좌표

while True:
    cv2.imshow("Cat", img)
    cv2.moveWindow("Cat", x, y )    # (x, y) 좌표로 창 이동
    
    key = cv2.waitKeyEx()   # 키보드 입력을 무한 대기
    
    if key == 0x250000: x -= 10     # 왼쪽 방향키
    elif key == 0x270000: x += 10   # 오른쪽 방향키
    elif key == 0x260000: y -= 10   # 위쪽 방향키
    elif key == 0x280000: y += 10   # 아래쪽 방향키
    elif key == 27:                 # Esc키 - 종료
        cv2.destroyAllWindows()
        break
        
    
  
 
