import tkinter as tk
from tkinter import font

"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""

sample_instruction = (" Use the \'add\' instruction to add the values in\n registers R1 and R2."
                        "\n Save the values in register R3.\n" " Remember that the add instruction is "
                        "of the form:\n \'instruction destination, source, source\'")


def feedback(input, label, button):
    label.configure(text=input.get())
    input.pack_forget()
    button.pack_forget()
    label.pack(side="top", pady=10)
    input.pack(side="left", padx=10)
    button.pack(side="right", padx=10)
    pass


def draw_lesson(root, ttk, lesson):
    # Set fonts for the menu widgets.
    # print(font.families()) to print available font families.
    menuLabel_font = font.Font(family="Loma", size=22, weight="bold")
    menuButton_font = font.Font(family="Loma", size=20, weight="normal")

    # background="..." doesn't work...
    ttk.Style().configure('green/black.TLabel', foreground='black', background='DarkOrange1', font=menuLabel_font)
    ttk.Style().configure('green/black.TButton', foreground='black', background='DarkOrange1', font=menuButton_font,
                          width=15)

    # Every lesson has multiple frames for packing.
    # lesson_header is always the prompt/lesson.
    # slide holds lesson interaction
    # ribbon holds buttons for main menu, submit, etc.
    lesson_header = tk.Frame(master=root, bg="medium blue")
    slide = tk.Frame(master=root, bg="medium blue")
    ribbon = tk.Frame(master=root, bg="medium blue")

    # Pack lesson_header Frame over the top of the slide.
    lesson_header.pack(fill="x")
    # Now fill center page.
    slide.pack(expand=True, fill="both")
    # Tack on ribbon.
    ribbon.pack(expand=True, fill="both", side="bottom")

    menu_escape = ttk.Button(ribbon, text='Main Menu', style='green/black.TButton')
    label_prompt = ttk.Label(lesson_header, text=lesson.lesson_prompt,
                             style='green/black.TLabel')
    label_instruction = ttk.Label(slide, text=sample_instruction, style='green/black.TLabel')

    # input_written is the output of their input.
    # lesson_input is their input.
    input_written = ttk.Label(slide, text=' ', style='green/black.TLabel')
    lesson_input = ttk.Entry(master=slide, font=menuLabel_font)

    check_button = ttk.Button(master=slide, text='Submit Code', style='green/black.TButton',
                              command=lambda: feedback(lesson_input, input_written, check_button))

    label_prompt.pack(side="left")
    label_instruction.pack(side="top", pady=5)
    lesson_input.pack(side="left", pady=20, padx=10)
    check_button.pack(side="right", padx=10)
    menu_escape.pack(side="bottom")
    pass