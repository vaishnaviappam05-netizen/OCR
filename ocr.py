import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import pytesseract as pyt

def display(pic):
    img = Image.open(pic)
    img_lbl.config(image=ImageTk.PhotoImage(img))
    img_lbl.img = img

def select():
    path = fd.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if path:
        display(path)
        path_lbl.config(text=path)

def ocr():
    path = path_lbl.cget("text")
    lang = lang_var.get()
    text = pyt.image_to_string(Image.open(path), lang=lang)
    res_lbl.config(text=text if text else "OCR failed.")

root = tk.Tk()
root.title("Anime OCR")

img_lbl = tk.Label(root)
path_lbl = tk.Label(root, text="")
res_lbl = tk.Label(root, text="")

sel_btn = tk.Button(root, text="Select", command=select)
ocr_btn = tk.Button(root, text="OCR", command=ocr)

lang_var = tk.StringVar(root)
lang_var.set("eng")
lang_opt = tk.OptionMenu(root, lang_var, "english", "hindi", "japanese", "telugu")

img_lbl.pack()
path_lbl.pack()
res_lbl.pack()
sel_btn.pack(pady=10)
ocr_btn.pack(pady=10)
lang_opt.pack()

root.mainloop()
