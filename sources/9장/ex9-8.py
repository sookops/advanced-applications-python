import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/cat.bmp')
cv2.imshow('img', img)
color = ('b', 'g', 'r')

for i in range(3):
    hist = cv2.calcHist([img], [i], None, [100], [0, 256])
    plt.plot(hist, color = color[i])
    print(hist.max(), hist.min(), hist.mean())

plt.show()

