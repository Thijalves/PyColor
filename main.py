import cv2
import numpy as np
import time

def empty(a):
        pass

#abrir a imagem
img = cv2.imread('Images/colors.png')

#criar trackbars
cv2.namedWindow("Range HSV")
cv2.resizeWindow("Range HSV", 500, 350)
cv2.createTrackbar("HUE Min", "Range HSV", 0,180, empty)
cv2.createTrackbar("HUE Max", "Range HSV", 180,180, empty)
cv2.createTrackbar("SAT Min", "Range HSV", 0,255, empty)
cv2.createTrackbar("SAT Max", "Range HSV", 255,255, empty)
cv2.createTrackbar("VALUE Min", "Range HSV", 0,255, empty)
cv2.createTrackbar("VALUE Max", "Range HSV", 255,255, empty)

while True:
    # Ler valores do trackbar
    h_min = cv2.getTrackbarPos("HUE Min", "Range HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "Range HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "Range HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "Range HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "Range HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "Range HSV")

    # Definir range
    lower_range = np.array([h_min,s_min,v_min])
    upper_range = np.array([h_max, s_max, v_max])

    # converter para HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # threshold the hsv image to get some color
    mascara = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('Original', img)

    cv2.imshow('Mascara', mascara)
    cv2.waitKey(1)