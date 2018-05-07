import cv2
import numpy as np
from matplotlib import pyplot as plt

#this function takes a histogram as input and gives its CDF as output


def get_CDF(hist):
    CDF = np.cumsum(hist)
    CDF_max = max(CDF)
    CDF = CDF/CDF_max

    plt.figure()
    plt.title("CDF of Histogram")
    plt.xlabel("Bin")
    plt.ylabel("%")
    plt.plot(CDF)
    plt.xlim([0, 256])
    plt.show()

    return CDF
