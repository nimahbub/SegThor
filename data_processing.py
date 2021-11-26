# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:33:10 2021
@author: NI Mahbub
"""


# importing libries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import measure, io, img_as_ubyte
from skimage.color import rgb2gray
from skimage.morphology import (erosion, dilation, closing, opening,
                                area_closing, area_opening)
from skimage.measure import label, regionprops, regionprops_table
from scipy import ndimage as ndi
from skimage.filters import threshold_otsu


# loading 3D image of one patient
m_img = io.imread('Patient_01.nii')
print(f'Shape of the main image : {m_img.shape}')



#taking only one slice from the 3D image
slice = m_img[75]
print(f'Main Image shape: {slice.shape}')
plt.imshow(slice, cmap='gray')
plt.show()




#ploting one slice image after converting binary
image = m_img
thresh = -1000
print(thresh)
binary = image > thresh
print(f'Image shape after converting binary{binary[75].shape}')
plt.imshow(binary[75],cmap='gray')
plt.show()



# finding connected components 
label_im = label(binary[75])
regions = regionprops(label_im)



areas = [x.area for x in regions]
sort_area = sorted(areas, reverse=True)
print(sort_area[0])

for num, x in enumerate(regions):
  area = x.area
  if area <sort_area[0]:
    slice[x.coords]=-1000
  else:
      continue
    

plt.imshow(slice, cmap='gray')
plt.show()

        

