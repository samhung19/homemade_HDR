import cv2
import numpy as np
from matplotlib import pyplot as plt

#this function takes an image as input and gives the hisogram as output


def get_hist(img_in):
    hist = cv2.calcHist([img_in],[0],None,[256],[0,256])
    plt.figure()
    plt.title("Histogram")
    plt.xlabel("Bin")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    return hist
    #cv2.imshow('image', img_in)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
