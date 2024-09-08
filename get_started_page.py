import tkinter as tk
from PIL import Image, ImageTk
import PIL.Image

def getStarted():
    app1.destroy()
    import main

# Create the main application window
app1 = tk.Tk()
app1.title("Disease Diagnosis Application")
app1.geometry("1366x768")

bg_img = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text/1.png"))
bg = tk.Label(image=bg_img)
bg.place(x=-1, y=0)


get_started_img = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text\getStarted.png"))

get_started_button = tk.Button(app1, image=get_started_img, command=getStarted, bd=0)
get_started_button.place(x=165, y=639)



app1.mainloop()