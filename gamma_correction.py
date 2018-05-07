import cv2
import numpy as np
import multiply_factor as mulfac

#pseudocode:
#img_in = img_in/255.0
#img_in = cv2.pow(img_in, 1.0/gamma_factor)
#img_in = img_in*255.0

def gamma_corr(img_in, gamma_factor):
    h, w, d = img_in.shape
    for j in range(0,h):
        for i in range(0,w):
            b, g, r = img_in[j,i]
            b_scaled, g_scaled, r_scaled = mulfac.scale_linear(float(b), float(g), float(r), 1/255.0) #get values between [0,1]
            b_scaled, g_scaled, r_scaled = mulfac.scale_exponential(float(b_scaled), float(g_scaled), float(r_scaled), gamma_factor) #apply exp scaling
            b, g, r = mulfac.scale_linear(float(b_scaled), float(g_scaled), float(r_scaled), 255.0)      #convert back to [0,255]
            img_in[j, i] = [int(b), int(g), int(r)]
    #cv2.imshow('gamma corrected', img_in)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return img_in



def inv_gamma_corr(img_in, gamma_factor):
    inv_gamma_factor = 1/gamma_factor
    h, w, d = img_in.shape
    for j in range(0,h):
        for i in range(0,w):
            b, g, r = img_in[j,i]
            b_scaled, g_scaled, r_scaled = mulfac.scale_linear(float(b), float(g), float(r), 1/255.0) #get values between [0,1]
            b_scaled, g_scaled, r_scaled = mulfac.scale_exponential(float(b_scaled), float(g_scaled), float(r_scaled), inv_gamma_factor) #apply exp scaling
            b, g, r = mulfac.scale_linear(float(b_scaled), float(g_scaled), float(r_scaled), 255.0)      #convert back to [0,255]
            img_in[j, i] = [int(b), int(g), int(r)]
    #cv2.imshow('inverse gamma corrected', img_in)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return img_in
