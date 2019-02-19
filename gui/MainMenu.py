import tkinter as tk
from tkinter import font


def destroy_content(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def draw_menu(root, ttk):
    # Set fonts for the menu widgets.
    # print(font.families()) to print available font families.
    menuLabel_font = font.Font(family="Loma", size=22, weight="bold")
    menuButton_font = font.Font(family="Loma", size=20, weight="normal")

    # background="..." doesn't work...
    ttk.Style().configure('green/black.TLabel', foreground='black', background='DarkOrange1', font=menuLabel_font)
    ttk.Style().configure('green/black.TButton', foreground='black', background='DarkOrange1', font=menuButton_font,
                          width=15)

    slide = tk.Frame(master=root, bg="dodger blue")
    slide.pack()

    label = ttk.Label(slide, text='\tWelcome to SMIP.\n Your Best Friend for Learning MIPS ',
                      style='green/black.TLabel')
    label.pack()

    button1 = ttk.Button(slide, text='Start', style='green/black.TButton', command=lambda: destroy_content(slide))
    button2 = ttk.Button(slide, text='Select Lesson', style='green/black.TButton')
    button3 = ttk.Button(slide, text='Practice', style='green/black.TButton')
    button4 = ttk.Button(slide, text='Exit', style='green/black.TButton', command=quit)

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    pass