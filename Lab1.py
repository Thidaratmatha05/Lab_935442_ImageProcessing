import cv2
import matplotlib.pyplot as plt

#รับภาพเข้ามา
img = cv2.imread("/content/1.jpg") #BGR
#แปลงสีให้เป็นเทา
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#แปลงสีให้เป็นดำ
_,bw = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

#มี3 คือภาพสี
print(img.shape)
print(bw.shape)

#คอลัม 2*2 ตำแหน่งภาพ
plt.subplot(221),plt.imshow(img)
plt.subplot(222),plt.imshow(rgb)
plt.subplot(223),plt.imshow(gray, cmap='gray')
plt.subplot(224),plt.imshow(bw, cmap='gray')

plt.show()