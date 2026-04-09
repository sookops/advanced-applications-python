import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread("images/lenna.png")
bgr = cv2.split(imgBGR)

# 두 개의 영상을 함께 출력
# plt.subplot(행크기, 열크기, 첨자), 첨자는 1부터 행우선으로 지정
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.subplot(2, 2, 1)
plt.imshow(imgRGB)
plt.subplot(2, 2, 2)
plt.imshow(bgr[0], cmap='gray')
plt.subplot(2, 2, 3)
plt.imshow(bgr[1], cmap='gray')
plt.subplot(2, 2, 4)
plt.imshow(bgr[2], cmap='gray')
plt.show()


