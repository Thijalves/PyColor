import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Load image
image = Image.open("hue.png")
photo = ImageTk.PhotoImage(image)

# Create label and add image
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
