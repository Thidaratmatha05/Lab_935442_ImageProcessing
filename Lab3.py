# พื้นฐาน
vai = input("Can you input name : ")
print("You are name : ",vai)
####
str = "numwan"
oid = 20
print("I am name : ",str)
print("I am age : ",oid)
####
age = 18
if (age>18):
  print("I am age: ",age)
elif(age<18):
  print("I age: ",age)
else:
  print("I am not age: ",age)
####
for x in range(1,10):
  print("In = ",x)
####
name = ["apple", "banana", "cherry"]
for x in name:
  print("Name = ",x)

# ----------------------------------------
import cv2
import matplotlib.pyplot as plt

#ทำให้ดำ ////ขาวสุด ลบ ด้วยรูปภาพ
image = cv2.imread('/content/1.jpg', 0)
neg = 255 - image

plt.imshow(neg, cmap='gray')
plt.show()

# -------------------------------------------------
import cv2
import matplotlib.pyplot as plt

#ทำให้ขาวขึ้น
image = cv2.imread('/content/1.jpg', 0)
neg = image + 64  #ทำให้ขาวขึ้นจนถึง255 //// 255คือขาวที่สุด

plt.imshow(neg, cmap='gray')
plt.show()

# ---------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)
log = 1 * np.log(image + 1)
log = np.array(log, dtype=np.uint8) 

plt.subplot(121),plt.imshow(image , cmap='gray')
plt.subplot(122),plt.imshow(log , cmap='gray')
plt.show()

# -------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/content/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# คำสั่งเปลี่ยนสี แค่บรรทัดเดียว มีเท่ากันกับสองบรรทัดบนนี้
# gray = cv2.imread('/content/1.jpg',0)
neg = 255 - gray

plt.subplot(121),plt.imshow(gray , cmap='gray')
plt.subplot(122),plt.imshow(neg , cmap='gray')
plt.show()

# -----------------------------------------------------
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/content/1.jpg')

plt.imshow(image)
plt.show()

# ---------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)

# ** ยิ่งใกล้0.0 ยิ่งขาว
gamma = 255*(image/255) **0.1
gamma = np.array(gamma, dtype=np.uint8)

plt.subplot(121),plt.imshow(image , cmap='gray')
plt.subplot(122),plt.imshow(gamma , cmap='gray')
plt.show()
# ----------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)
log = 1 * np.log(image + 1)
log = np.array(log, dtype=np.uint8) 

plt.subplot(121),plt.imshow(image , cmap='gray')
plt.subplot(122),plt.imshow(log , cmap='gray')
plt.show()
# ---------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/content/1.jpg', 0)
hist = cv2.calcHist([image], [0], None, [256],[0, 256])

eq = cv2.equalizeHist(image)
histeq = cv2.calcHist([eq], [0], None, [256], [0, 256])


plt.subplot(331), plt.imshow(image, cmap='gray')
plt.subplot(332), plt.hist(hist)
plt.subplot(333), plt.hist(image, bins = 10)

# plt.subplot(334), plt.imshow(image, cmap='gray')
plt.subplot(335), plt.imshow(eq, cmap='gray')
plt.subplot(336), plt.hist(histeq, bins = 10)
plt.show()
# -------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

gray = cv2.imread('/content/1.jpg', 0)
_,bw = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)

t = 20
gray2 = gray + t

plt.subplot(221),plt.imshow(gray , cmap='gray')
plt.subplot(222),plt.imshow(gray2 , cmap='gray')
plt.show()
# --------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/content/1.jpg', 0)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
eq = cv2.equalizeHist(image)
para = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
aeq = para.apply(image)

plt.subplot(121),plt.imshow(aeq, cmap='gray')
plt.subplot(122),plt.hist(aeq, bins = 10)
plt.show()
# ----------------------------------------------------