import matplotlib.pyplot as plt
import cv2
imgBGR = cv2.imread("images/cat.bmp")
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

# 두 개의 영상을 함께 출력
# plt.subplot(행크기, 열크기, 첨자), 첨자는 1부터 행우선으로 지정
plt.subplot(2, 1, 1)
plt.axis('off')
plt.imshow(imgRGB)
plt.subplot(2, 1, 2)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

