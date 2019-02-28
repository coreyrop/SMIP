from PIL import ImageTk, Image
from tkinter import font
import tkinter as tk

def draw_reference():
    reference_window = tk.Toplevel()
    reference_window.title("MIPS: Green Sheet")

    #Relative path to the green sheet
    path = "Green Sheet.jpg"

    # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path).resize((1000,500),Image.ANTIALIAS))

    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(reference_window, image=img)
    panel.image = img
    # The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side="bottom", fill="both", expand="yes")
    pass