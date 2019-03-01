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
#Function to store user code from text box to store it in a file
def store_source_code(user_text):
    out = open("user_input.txt", "w")
    out.write(user_text)
    out.close()
    pass
def feedback(user_input, label, button1, button2 ):
    label.configure(text=user_input.get())
    textinp = user_input.get()                 #store text
    store_source_code(textinp)            #send to write to the file
    user_input.pack_forget()
    button2.pack_forget()
    button1.pack_forget()
    label.pack(side="top", pady=10)
    user_input.pack(side="left", padx=10)
    button1.pack(side="right")
    button2.pack(side="right", padx=10)
    pass

def sub(user_input,lesson_input):
    f = open('input.s', 'w')
    f.write(user_input.get("1.0", tk.END))
    f.close()
    pass
def get_text():
    f = open('Sample1.s', 'r')
    output = ""
    for x in f.readlines():
        output += x

    return output


def draw_lesson(root, ttk, lesson):
    # Set fonts for the menu widgets.
    # print(font.families()) to print available font families.
    menuLabel_font = font.Font(family="Loma", size=22, weight="bold")
    menuButton_font = font.Font(family="Loma", size=20, weight="normal")
    # background="..." doesn't work...
    ttk.Style().configure('B_DO1.TLabel', foreground='black', background='DarkOrange1', font=menuLabel_font)
    ttk.Style().configure('B_DO1.TButton', foreground='black', background='DarkOrange1', font=menuButton_font, width=15)

    lesson_header = tk.Frame(master=root, bg="medium blue")
    slide = tk.Frame(master=root, bg="medium blue")
    slide2 = tk.Frame(master=root, bg="medium blue")
    ribbon = tk.Frame(master=root, bg="medium blue")
    lesson_header.pack(fill="x")
    slide.pack(expand=True, fill="both")
    slide2.pack(expand=True, fill="both")
    ribbon.pack(expand=True, fill="both", side="bottom")
    label_prompt = ttk.Label(lesson_header, text=lesson.lesson_prompt, style='B_DO1.TLabel')
    label_instruction = ttk.Label(slide, text=sample_instruction, style='B_DO1.TLabel')
    menu_escape = ttk.Button(ribbon, text='Main Menu', style='B_DO1.TButton')
    hint_button = ttk.Button(slide2, text='Hint', style='B_DO1.TButton', command=None)

    # input_written is the output of their input.
    # lesson_input is their input.
    input_written = ttk.Label(slide, text=' ', style='B_DO1.TLabel')
    lesson_input = ttk.Entry(master=slide, font=menuLabel_font)
    lesson_input = tk.Text(slide, height=30, width=100)
    quote = get_text()
    lesson_input.insert(tk.END, quote)
    submit_button = ttk.Button(master=slide2, text='Submit Code', style='B_DO1.TButton',
                              command=lambda: sub(lesson_input,lesson_input))


    label_instruction.pack(side="top", pady=5)
    lesson_input.pack(pady=20, padx=10)
    submit_button.pack(side='right',padx=10)
    menu_escape.pack()
    hint_button.pack(side='left',padx=10)
    pass