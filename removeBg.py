# /Users/a23135334/Downloads/abcx.jpg

import cv2
import numpy as np

# Load the image
img = cv2.imread('a12a.jpg')

img = img + np.array([255, 255, 255])

for i in reversed(range(255, 510)):
    img[img>i] = 510-i
    

# img[img > 480] = 0
# img[img > 450] = 60
# img[img > 420] = 90d
# img[img > 390] = 120
# img[img > 360] = 150
# img[img > 300] = 210
# img[img > 280] = 230
# img[img > 255] = 255




# Clip the pixel values to [0, 255] to avoid overflow
img = np.clip(img, 0, 255).astype('uint8')
cv2.imwrite('a12a-modified_image.jpg', img)
# Display the image
# cv2.imshow('Modified Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()