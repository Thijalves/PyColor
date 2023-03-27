from tkinter import *
import cv2
from PIL import Image, ImageTk

#abrir a imagem
img = cv2.imread('Images/colors.png')
height = img.shape[0]
width = img.shape[1]

#Pagina princial do programa
root = Tk()
root.title('PyColor - Ferramenta para Segmentação de Cores')
canvas = Canvas(root, width=1280, height=720)
canvas.pack()

# converter imagem para um formato de imagem do tkinter
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_pil = Image.fromarray(img_rgb)
img_tk = ImageTk.PhotoImage(img_pil)

canvas.create_image(0, 0, anchor=NW, image=img_tk)

root.mainloop()