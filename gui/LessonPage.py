import tkinter as tk
from tkinter import messagebox
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

sample_hint = (" The add instruction expects a destination register followed by two source registers,"
               " which are comma separated.")

registers = []
SIDEBAR_COLUMN_WIDTH = 5
# Function to store user code from text box to store it in a file


def store_source_code(user_text):
    out = open("user_input.txt", "w")
    out.write(user_text)
    out.close()
    pass


def feedback(user_input, label, button1, button2 ):
    label.configure(text=user_input.get())
    textinp = user_input.get()                  # Store text
    store_source_code(textinp)                  # Send to write to the file
    user_input.pack_forget()
    button2.pack_forget()
    button1.pack_forget()
    label.pack(side="top", pady=10)
    user_input.pack(side="left", padx=10)
    button1.pack(side="right")
    button2.pack(side="right", padx=10)
    pass


def sub(user_input, lesson_input):
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

    sidebar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

    draw_sidebar(sidebar, ttk)

    # Pack lesson_header Frame over the top of the slide.
    lesson_header.pack(fill="x")
    slide.pack(expand=True, fill="both")
    slide2.pack(expand=True, fill="both")
    ribbon.pack(expand=True, fill="both", side="bottom")
    label_prompt = ttk.Label(lesson_header, text=lesson.lesson_prompt, style='B_DO1.TLabel')
    label_instruction = ttk.Label(slide, text=sample_instruction, style='B_DO1.TLabel')
    menu_escape = ttk.Button(ribbon, text='Main Menu', style='B_DO1.TButton', cursor="target")
    hint_button = ttk.Button(slide2, text='Hint', style='B_DO1.TButton',
                             cursor="target", command=lambda: messagebox.showinfo("Hint", sample_hint))

    # input_written is the output of their input.
    # lesson_input is their input.
    input_written = ttk.Label(slide, text=' ', style='B_DO1.TLabel')
    lesson_input = ttk.Entry(master=slide, font=menuLabel_font)
    lesson_input = tk.Text(slide, height=30, width=100)
    quote = get_text()
    lesson_input.insert(tk.END, quote)
    submit_button = ttk.Button(master=slide2, text='Submit Code', style='B_DO1.TButton',
                               cursor="target", command=lambda: sub(lesson_input, lesson_input))

    label_instruction.pack(side="top", pady=5)
    lesson_input.pack(pady=20, padx=10)
    submit_button.pack(side='right',padx=10)
    menu_escape.pack()
    hint_button.pack(side='left',padx=10)
    pass


def draw_sidebar(sidebar, ttk):
    tk.Label(sidebar, text="NAME", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=0)
    tk.Label(sidebar, text="NUM", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=1)
    tk.Label(sidebar, text="VALUE", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=2)
    dict = {} # debugging purposes, this'll get deleted once we geet output from pyspim

    for i in range (32):
        label = tk.Label(sidebar, text="0", width="5")
        label.grid(row=i+1, column=2)
        registers.append(label) # global arr so labels can be updated
        dict[i] = i * 2 # for debugging purposes, this will be the Lessons answer returned from pyspim

    tk.Label(sidebar, text="$zero", width=SIDEBAR_COLUMN_WIDTH).grid(row=1, column=0)
    tk.Label(sidebar, text="$at", width=SIDEBAR_COLUMN_WIDTH).grid(row=2, column=0)
    tk.Label(sidebar, text="$v0", width=SIDEBAR_COLUMN_WIDTH).grid(row=3, column=0)
    tk.Label(sidebar, text="$v1", width=SIDEBAR_COLUMN_WIDTH).grid(row=4, column=0)
    tk.Label(sidebar, text="$a0", width=SIDEBAR_COLUMN_WIDTH).grid(row=5, column=0)
    tk.Label(sidebar, text="$a1", width=SIDEBAR_COLUMN_WIDTH).grid(row=6, column=0)
    tk.Label(sidebar, text="$a2", width=SIDEBAR_COLUMN_WIDTH).grid(row=7, column=0)
    tk.Label(sidebar, text="$a3", width=SIDEBAR_COLUMN_WIDTH).grid(row=8, column=0)
    tk.Label(sidebar, text="$t0", width=SIDEBAR_COLUMN_WIDTH).grid(row=9, column=0)
    tk.Label(sidebar, text="$t1", width=SIDEBAR_COLUMN_WIDTH).grid(row=10, column=0)
    tk.Label(sidebar, text="$t2", width=SIDEBAR_COLUMN_WIDTH).grid(row=11, column=0)
    tk.Label(sidebar, text="$t3", width=SIDEBAR_COLUMN_WIDTH).grid(row=12, column=0)
    tk.Label(sidebar, text="$t4", width=SIDEBAR_COLUMN_WIDTH).grid(row=13, column=0)
    tk.Label(sidebar, text="$t5", width=SIDEBAR_COLUMN_WIDTH).grid(row=14, column=0)
    tk.Label(sidebar, text="$t6", width=SIDEBAR_COLUMN_WIDTH).grid(row=15, column=0)
    tk.Label(sidebar, text="$t7", width=SIDEBAR_COLUMN_WIDTH).grid(row=16, column=0)
    tk.Label(sidebar, text="$s0", width=SIDEBAR_COLUMN_WIDTH).grid(row=17, column=0)
    tk.Label(sidebar, text="$s1", width=SIDEBAR_COLUMN_WIDTH).grid(row=18, column=0)
    tk.Label(sidebar, text="$s2", width=SIDEBAR_COLUMN_WIDTH).grid(row=19, column=0)
    tk.Label(sidebar, text="$s3", width=SIDEBAR_COLUMN_WIDTH).grid(row=20, column=0)
    tk.Label(sidebar, text="$s4", width=SIDEBAR_COLUMN_WIDTH).grid(row=21, column=0)
    tk.Label(sidebar, text="$s5", width=SIDEBAR_COLUMN_WIDTH).grid(row=22, column=0)
    tk.Label(sidebar, text="$s6", width=SIDEBAR_COLUMN_WIDTH).grid(row=23, column=0)
    tk.Label(sidebar, text="$s7", width=SIDEBAR_COLUMN_WIDTH).grid(row=24, column=0)
    tk.Label(sidebar, text="$t8", width=SIDEBAR_COLUMN_WIDTH).grid(row=25, column=0)
    tk.Label(sidebar, text="$t9", width=SIDEBAR_COLUMN_WIDTH).grid(row=26, column=0)
    tk.Label(sidebar, text="$k0", width=SIDEBAR_COLUMN_WIDTH).grid(row=27, column=0)
    tk.Label(sidebar, text="$k1", width=SIDEBAR_COLUMN_WIDTH).grid(row=28, column=0)
    tk.Label(sidebar, text="$gp", width=SIDEBAR_COLUMN_WIDTH).grid(row=29, column=0)
    tk.Label(sidebar, text="$sp", width=SIDEBAR_COLUMN_WIDTH).grid(row=30, column=0)
    tk.Label(sidebar, text="$fp", width=SIDEBAR_COLUMN_WIDTH).grid(row=31, column=0)
    tk.Label(sidebar, text="$ra", width=SIDEBAR_COLUMN_WIDTH).grid(row=32, column=0)
    for i in range (32):
        tk.Label(sidebar, text=i, width=SIDEBAR_COLUMN_WIDTH).grid(row=i+1, column=1)
    update_registers(sidebar, dict)


def update_registers(sidebar, answers):
    i = 0
    for answer in answers:
        res = answers[i]
        registers[i].config(text=res)
        i = i + 1
