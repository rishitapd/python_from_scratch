from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

root= tk.Tk()
root.title("IMage slideshow viewer")

#list of Image path
image_paths=[
    r"C:\Users\KIIT\Desktop\siya\ajxdo_512.webp",
    r"C:\Users\KIIT\Desktop\siya\981323.jpg",
    r"C:\Users\KIIT\Desktop\siya\WhatsApp Image 2024-05-27 at 09.54.24_efacc35b.jpg",
    r"C:\Users\KIIT\Desktop\siya\WhatsApp Image 2024-05-27 at 09.54.47_6f051846.jpg",
    r"C:\Users\KIIT\Desktop\siya\Cute-Desktop-HD-Wallpaper.jpg",
]
#resize the image to 1080*1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(2)

slidshow=cycle(photo_images)

def start_slidshow():
    for _ in range(len(image_paths)):
       update_image()

play_button =tk.Button(root,text='play Slideshow',command=start_slidshow)
play_button.pack()

root.mainloop()