import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/tunes/Aandom/MintM/Album/Album/ff80818164db4c1f0164e08ab50d399d_31390_large.jpg',0)
edges = cv2.Canny(img,100,200)
plt.figure(figsize=(100,100))

plt.subplot(121),plt.imshow(img,cmap = 'gray', aspect='equal')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.figure(figsize=(300,400))

plt.show()