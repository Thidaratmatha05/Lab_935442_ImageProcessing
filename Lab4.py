# การกรองภาพแบบค่าเฉลี่ย
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)
##ฟิวเตอร์ ขนาดn*n=4*4 โดยมีค่าเป็น1 หารด้วยn*n=5*5=25 กล้ายเป็น1/n*n
##ฟิวเตอร์ ภาพ -1ภาพต้นฉบับคล้ายละสีกับภาพที่ออกมา
f = np.ones((4,4),np.float32)/25
fi = cv2.filter2D(image,-1,f)

plt.subplot(121), plt.imshow(image, cmap='gray')
plt.subplot(122), plt.imshow(fi, cmap='gray')
plt.show()
#-----------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('/content/1.jpg', 0)
noise = random_noise(image, mode = 's&p', amount = 0.3)
fimg = cv2.medianBlur(image,5)

f = np.ones((4,4),np.float32)/25
fi = cv2.filter2D(noise,-1,f)

plt.subplot(221), plt.imshow(image, cmap='gray')
plt.subplot(222), plt.imshow(noise, cmap='gray')
plt.subplot(223), plt.imshow(fi, cmap='gray')
plt.subplot(224), plt.imshow(fimg, cmap='gray')
plt.show()
# -----------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)
#fimg= cv2.medinaBlur(image,3)
plt.imshow(image, cmap='gray')
plt.show()
#size 5*5 = 25
f = np.ones((5,5), np.float32)/25
smoothing = cv2.filter2D(image,-1,f)

plt.imshow(smoothing, cmap='gray')
plt.show()
# ------------------------------------------------------------------
#ค่ามัธฐาน (Median)
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('/content/1.jpg', 0)
#apply median filter to image
fimg= cv2.medianBlur(image,3)
plt.imshow(fimg, cmap='gray')

plt.show()
# -------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('/content/1.jpg', 0)
#apply noise
noise = random_noise(image, mode = 'gaussian')
plt.imshow(noise, cmap='gray')
plt.show()

noise2 = random_noise(image, mode = 's&p', amount = 0.3)
plt.imshow(noise2, cmap='gray')
plt.show()

noise3 = random_noise(image, mode = 'poisson')
plt.imshow(noise3, cmap='gray')
plt.show()
# ----------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('/content/1.jpg', 0)
#apply noise
noise = random_noise(image, mode = 'gaussian')
plt.imshow(noise, cmap='gray')
plt.show()

f = np.ones((5,5), np.float32)/25
smoothing = cv2.filter2D(image,-1,f)
medianBlur= cv2.medianBlur(image,5)

plt.imshow(smoothing, cmap='gray')
plt.show()
plt.imshow(medianBlur, cmap='gray')
plt.show()
# -------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

image = cv2.imread('/content/1.jpg', 0)
#apply noise
noise = random_noise(image, mode = 'gaussian')
plt.imshow(noise, cmap='gray')
plt.show()

f = np.ones((5,5), np.float32)/25
smoothing = cv2.filter2D(noise,-1,f)
#medianBlur= cv2.medianBlur(noise,5)

plt.imshow(smoothing, cmap='gray')
plt.show()
#plt.imshow(medianBlur, cmap='gray')
#plt.show()
# ------------------------------------------------