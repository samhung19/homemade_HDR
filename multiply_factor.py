import cv2
import numpy as np


#this function takes img (w/ coordinates) and gets 3 channels and scales them by factor of 'factor'
#returns the respective scaled pixel

def scale_linear(b, g, r, factor):
    b_scaled = b*factor
    g_scaled = g*factor
    r_scaled = r*factor
    if b_scaled < 0:
        b_scaled = 0
    if g_scaled < 0:
        g_scaled = 0
    if r_scaled < 0:
        r_scaled = 0

    if b_scaled > 255:
        b_scaled = 255
    if g_scaled > 255:
        g_scaled = 255
    if r_scaled > 255:
        r_scaled = 255
    return [b_scaled,g_scaled,r_scaled]

def scale_exponential(b, g, r, factor):
    b_scaled = pow(b, 1/factor)
    g_scaled = pow(g, 1/factor)
    r_scaled = pow(r, 1/factor)
    if b_scaled < 0:
        b_scaled = 0
    if g_scaled < 0:
        g_scaled = 0
    if r_scaled < 0:
        r_scaled = 0

    if b_scaled > 255:
        b_scaled = 255
    if g_scaled > 255:
        g_scaled = 255
    if r_scaled > 255:
        r_scaled = 255
    return [b_scaled,g_scaled,r_scaled]
