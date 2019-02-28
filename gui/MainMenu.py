import tkinter as tk
from tkinter import font
from gui.Utilities import transfer_to
from gui.LessonPage import draw_lesson
from lessons.Lesson import Lesson
from gui.ReferenceWindow import draw_reference

sample_lesson = Lesson('Lesson 1: Register Addition', {})

"""
Draws the main menu to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
"""

def draw_menu(root, ttk):
    # Set fonts for the menu widgets.
    # print(font.families()) to print available font families.
    menuLabel_font = font.Font(family="Loma", size=24, weight="bold")
    menuButton_font = font.Font(family="Loma", size=22, weight="normal")
    text_announce = font.Font(family="Gentium Book Basic", size=16, weight="normal")

    # background="..." doesn't work...
    ttk.Style().configure('green/black.TLabel', foreground='black', background='DarkOrange1', font=menuLabel_font)
    ttk.Style().configure('green/black.TButton', foreground='black', background='DarkOrange1', font=menuButton_font,
                          width=25)
    ttk.Style().configure('textBox.TLabel', foreground='black', background='cornflower blue', font=text_announce)

    slide = tk.Frame(master=root, bg="medium blue", width=root.winfo_width(), height=root.winfo_height())
    # Fill the empty space of the screen.
    slide.pack(expand=True, fill="both")

    label_banner = ttk.Label(slide, text='\tWelcome to SMIP.\n Your Best Friend for Learning MIPS ',
                             style='green/black.TLabel', width=700, anchor="center")
    label_plug = ttk.Label(slide, style='textBox.TLabel', text=' Our repo: https://github.com/coreyrop/SMIP\n\t'
                                                               '-Last Updated: 02/20/2019-')

    label_banner.pack(pady=10)
    label_plug.pack(side="bottom", pady=5)

    button1 = ttk.Button(slide, text='Start', style='green/black.TButton',
                         command=lambda: transfer_to(slide, lambda: draw_lesson(root, ttk, sample_lesson)))
    button2 = ttk.Button(slide, text='Select Lesson', style='green/black.TButton')
    button3 = ttk.Button(slide, text='Practice', style='green/black.TButton')
    button4 = ttk.Button(slide, text='Reference', style='green/black.TButton',command = lambda: draw_reference())
    button5 = ttk.Button(slide, text='Exit', style='green/black.TButton', command=quit)

    button1.pack(pady=30)
    button2.pack(pady=30)
    button3.pack(pady=30)
    button4.pack(pady=30)
    button5.pack(pady=30)
    pass