import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, window, title, source=0,width=1280, height=740):
        #Setup window
        self.window = window
        self.window.title(title)
        self.window.geometry(str(width)+"x"+str(height))
        self.window.resizable(False, False)

        #Widgets
        # set up the canvas for the image display
        self.window.originalCanvas = tk.Canvas(window, width=600, height=340)
        self.window.originalCanvas.grid(row=0, column=0, pady=10, padx=20)
        self.window.maskCanvas = tk.Canvas(window, width=600, height=340)
        self.window.maskCanvas.grid(row=1, column=0, pady=10, padx=20)
        self.window.resultCanvas = tk.Canvas(window, width=600, height=340)
        self.window.resultCanvas.grid(row=1, column=1, pady=10, padx=20)
        #sliders frame
        self.slider_frame = tk.Frame(self.window, width=600, height=50, bd=1, relief="solid")
        self.slider_frame.grid(row=0, column=1, pady=10, padx=20)
        #hue sliders
        self.hue_min_slider = tk.Scale(self.slider_frame, label='HUE Min', from_=0, to=180, orient=tk.HORIZONTAL)
        self.hue_min_slider.grid(row=0, column=0, pady=10, padx=20)
        self.hue_max_slider = tk.Scale(self.slider_frame, label='HUE Max', from_=0, to=180, orient=tk.HORIZONTAL)
        self.hue_max_slider.set(180)
        self.hue_max_slider.grid(row=0, column=1, pady=10, padx=20)
        #saturation sliders
        self.saturation_min_slider = tk.Scale(self.slider_frame, label='Saturation Min', from_=0, to=255, orient=tk.HORIZONTAL)
        self.saturation_min_slider.grid(row=1, column=0, pady=10, padx=20)
        self.saturation_max_slider = tk.Scale(self.slider_frame, label='Saturation Max', from_=0, to=255, orient=tk.HORIZONTAL)
        self.saturation_max_slider.set(255)
        self.saturation_max_slider.grid(row=1, column=1, pady=10, padx=20)
        #value sliders
        self.value_min_slider = tk.Scale(self.slider_frame, label='Value Min', from_=0, to=255, orient=tk.HORIZONTAL)
        self.value_min_slider.grid(row=2, column=0, pady=10, padx=20)
        self.value_max_slider = tk.Scale(self.slider_frame, label='Value Max', from_=0, to=255, orient=tk.HORIZONTAL)
        self.value_max_slider.set(255)
        self.value_max_slider.grid(row=2, column=1, pady=10, padx=20)
        # create a canvas for the image
        self.imageCanvas = tk.Canvas(self.slider_frame, width=500, height=110)
        self.imageCanvas.grid(row=3, column=0, columnspan=3)
        # load the image
        img = Image.open('Images/hue.png')
        img = img.resize((495, 108), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        # add the image to the canvas
        self.imageCanvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.imageCanvas.img_tk = img_tk

        #open source
        self.video = cv2.VideoCapture(source)
        # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

        # start the video display loop
        self.update()

    def update(self):
        # Definir range
        lower_range = np.array([self.hue_min_slider.get(),self.saturation_min_slider.get(),self.value_min_slider.get()])
        upper_range = np.array([self.hue_max_slider.get(),self.saturation_max_slider.get(),self.value_max_slider.get()])
        
        ret, frame = self.video.read()
    
        if ret:
            # cv2.imshow('Original', frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # cv2.imshow('hsv', hsv)
            mask = cv2.inRange(hsv, lower_range, upper_range)
            # cv2.imshow('mascara', mask)
            result = cv2.bitwise_and(frame, frame, mask=mask)
            
            # convert the original frame to a PIL image
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            imgArray = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(imgArray)
            # update the original frame canvas
            self.window.originalCanvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.window.originalCanvas.img_tk = img_tk

            # convert the mask frame to a PIL image
            maskArray = Image.fromarray(mask)
            array_tk = ImageTk.PhotoImage(maskArray)
            # update the mask frame canvas
            self.window.maskCanvas.create_image(0, 0, anchor=tk.NW, image=array_tk)
            self.window.maskCanvas.img_tk = array_tk

            # convert the result frame to a PIL image
            img = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
            resultArray = Image.fromarray(img)
            array_tk = ImageTk.PhotoImage(resultArray)
            # update the result frame canvas
            self.window.resultCanvas.create_image(0, 0, anchor=tk.NW, image=array_tk)
            self.window.resultCanvas.img_tk = array_tk

        # call this function again after 15 milliseconds
        self.window.after(15, self.update)
        