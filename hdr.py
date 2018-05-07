import cv2
import numpy as np
from matplotlib import pyplot as plt

import get_hist
import get_CDF
import gamma_correction as gam
import multiply_factor as mulfac

#potentially helpful
#https://www.learnopencv.com/high-dynamic-range-hdr-imaging-using-opencv-cpp-python/

img_hi = cv2.imread('2_hi.jpg',cv2.IMREAD_COLOR)   #image with higher brightness, more exposed
img_lo = cv2.imread('2_lo.jpg', cv2.IMREAD_COLOR)   #image with lower brightness, less exposed

#current limitations: grayscale, two images, not merged
    #grayscale = 3rd channel (HSV/HSL)
    #OR (preferred), inverse gamma correction (2.2) to get linear image, apply multiplying factor to RGB
        #then apply gamma correction back to get nonlinear image

gamma = 1.7
#get inv transform to get linear image
img_hi_inv_gamma = gam.inv_gamma_corr(img_hi, gamma)
img_lo_inv_gamma = gam.inv_gamma_corr(img_lo, gamma)



#do some stuff to linear image apply multiplying factor
img_hi_hist = get_hist.get_hist(img_hi_inv_gamma)
img_lo_hist = get_hist.get_hist(img_lo_inv_gamma)
img_hi_cdf = get_CDF.get_CDF(img_hi_hist)
img_lo_cdf = get_CDF.get_CDF(img_lo_hist)
img_hi_cdf_half = 128 #set to some arbitrary value
img_lo_cdf_half = 128

for i in range(0, 255):
    if img_hi_cdf[i] > .8:
        img_hi_cdf_half = i
        break
for i in range(0, 255):
    if img_lo_cdf[i] > .8:
        img_lo_cdf_half = i
        break
#get middle range where we just average the images
middle_min = min(img_hi_cdf_half, img_lo_cdf_half)
middle_max = max(img_hi_cdf_half, img_lo_cdf_half)

print(middle_min)
print(middle_max)


#low color intensity pick high exposure, higher intensity pick low exposure
#use interpolation for the in-betweens
img_new = img_hi_inv_gamma   #initialize temporary copy
img_lo_inv_gamma_gray = cv2.cvtColor(img_lo_inv_gamma, cv2.COLOR_BGR2GRAY)
img_hi_inv_gamma_gray = cv2.cvtColor(img_hi_inv_gamma, cv2.COLOR_BGR2GRAY)
h, w, d = img_new.shape
for y in range(0, h):
    for x in range(0, w):
        g_hi = img_hi_inv_gamma_gray[y,x]
        g_lo = img_lo_inv_gamma_gray[y,x]
        b_hi, g_hi, r_hi = img_hi_inv_gamma[y,x]
        b_lo, g_lo, r_lo = img_lo_inv_gamma[y,x]
        if (g_hi/2 + g_lo/2) >= middle_min: #select low exposure
            img_new[y,x] = [b_lo, g_lo, r_lo]
        elif (g_hi/2 + g_lo/2) > middle_min and (g_hi/2 + g_lo/2) < middle_max:   #average
            img_new[y,x] = [(b_hi/2 + b_lo/2) ,(g_hi/2 + g_lo/2),(r_hi/2 + r_lo/2)]
        else: #if (g_hi/2 + g_lo/2) <= middle_max: #select high exposure
            img_new[y,x] = [b_hi, g_hi, r_hi]


#gamma transform back to nonlinear
img_new = gam.gamma_corr(img_new, gamma)


cv2.imshow('new', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
