import tkinter as tk
from PIL import Image, ImageTk
import PIL.Image
from trial import *


app3 = tk.Tk()

bg_img = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text/3rdpage.png"))
bg = tk.Label(app3, image=bg_img)
bg.place(x=-1, y=0)
app3.title("Disease Diagnosis Application")
app3.geometry("1366x768")

txt = get_latest_inserted_disease()
label1 = tk.Label(app3, text = txt, font=('arial', 28), background="#fcffdb")
label1.place(x = 325, y = 85)

result_text1 = tk.Text(app3, height=14, width=32, background="#fcffdb", bd=1, font=('arial', 16))
result_text1.place(x=220, y=300)

result_text1.config(state="normal")
result_text1.delete(1.0, tk.END)
result_text1.insert(tk.END, f"{get_information(txt)}")
result_text1.config(state="disabled")



result_text2 = tk.Text(app3, height=14, width=32, background="#fcffdb", bd=1, font=('arial', 16))
result_text2.place(x=720, y=300)

result_text2.config(state="normal")
result_text2.delete(1.0, tk.END)
result_text2.insert(tk.END, f"{get_remedy(txt)}")
result_text2.config(state="disabled")


app3.mainloop()