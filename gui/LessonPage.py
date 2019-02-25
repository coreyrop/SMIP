import tkinter as tk
from tkinter import font

"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""


def draw_lesson(root, ttk, lesson):
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
    menu_escape = ttk.Button(slide, text='Main Menu', style='green/black.TButton')
    label_prompt = ttk.Label(slide, text=lesson.lesson_prompt,
                             style='green/black.TLabel')

    label_prompt.pack(side="top")
    menu_escape.pack(side="bottom")
    label.pack()

    button1 = ttk.Button(slide, text='Hint', style='green/black.TButton',
                         command=None)

    button1.pack()
    pass