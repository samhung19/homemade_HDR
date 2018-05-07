import cv2
import numpy as np
#resources:
#https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html
#https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/


def merge(lo, hi):
    sigma = .33
    lo_edges = auto_canny(lo, sigma)
    hi_edges = auto_canny(hi, sigma)
    cv2.imshow('lo_edges', lo_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow('hi_edges', hi_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    init_MSE = getMSE(lo, hi)

    #shift left 1 pixel
    hi_edges_left = img_translate(hi_edges, -1, 0)

    #shift right 1 pixel
    hi_edges_right = img_translate(hi_edges, 1, 0)

    #shift up 1 pixel
    hi_edges_up = img_translate(hi_edges, 0, 1)

    #shift down 1 pixel
    hi_edges_down = img_translate(hi_edges, 0, -1)

    #determine which direction of the four is best
    print("left_MSE: ")
    left_MSE = getMSE(lo, hi_edges_left)

    print("right_MSE: ")
    right_MSE = getMSE(lo, hi_edges_right)

    print("up_MSE: ")
    up_MSE = getMSE(lo, hi_edges_up)

    print("down_MSE: ")
    down_MSE = getMSE(lo, hi_edges_down)
    choices = [left_MSE, right_MSE, up_MSE, down_MSE]
    min_choice = choices.index(min(choices))
    if min(choices) < init_MSE:
        print("choose: ",min_choice)
        return min_choice
    else:
        print("no need to shift")
        return -1



def img_translate(img, dx, dy):
    h, w = img.shape
    M = np.float32([[1,0,dx],[0,1,dy]])   #diagonal matrix
    warped = cv2.warpAffine(img,M,(w,h))
    return warped


#get difference mean squared error of the central part of the image
def getMSE(lo, hi):
    MSE = 0
    h, w = lo.shape
    border_offset = 5 #in case we need to crop image
    for j in range(border_offset, h-border_offset):
        for i in range(border_offset, w-border_offset):
            pixel_lo = lo[j,i]
            pixel_hi = hi[j,i]
            MSE = MSE + (pow(int(pixel_lo) - int(pixel_hi),2)/(w*h))
    print(MSE)
    return MSE

#get median of pixel intensity, use it to find parameters for openCV's canny edge detection function
def auto_canny(image, sigma):
    pixel_median = np.median(image)
    lower = int(max(0, (1.0 - sigma) * pixel_median))
    upper = int(min(255, (1.0 + sigma) * pixel_median))

    edges = cv2.Canny(image, lower, upper)
    return edges

#main fcn starts here (for testing purposes)
img_lo = cv2.imread('7_lo.jpg', 0) #get grayscale images
img_hi = cv2.imread('7_hi.jpg', 0)
merge(img_lo, img_hi)
