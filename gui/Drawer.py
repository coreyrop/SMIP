import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import *
from gui.ReferenceWindow import draw_reference
from gui.LessonPage import submit_code
from gui.Utilities import transfer_to

SIDEBAR_COLUMN_WIDTH = 5
registers = []


def draw_menu(root, ttk, next_lesson):
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

    main_frame = tk.Frame(master=root, bg="medium blue", width=root.winfo_width(), height=root.winfo_height())
    # Fill the empty space of the screen.
    main_frame.pack(expand=True, fill="both")

    label_banner = ttk.Label(main_frame, text='\tWelcome to SMIP.\n Your Best Friend for Learning MIPS ',
                             style='green/black.TLabel', width=700, anchor="center")
    label_plug = ttk.Label(main_frame, style='textBox.TLabel', text=' Our repo: https://github.com/coreyrop/SMIP\n\t'
                                                                    '-Last Updated: 02/20/2019-')

    label_banner.pack(pady=10)
    label_plug.pack(side="bottom", pady=5)

    button1 = ttk.Button(main_frame, text='Start', style='green/black.TButton',
                         command=lambda: transfer_to(
                             lambda: draw_lesson(root, ttk, next_lesson, submit_code, messagebox.showinfo), main_frame))
    button2 = ttk.Button(main_frame, text='Select Lesson', style='green/black.TButton')
    button3 = ttk.Button(main_frame, text='Practice', style='green/black.TButton')
    button4 = ttk.Button(main_frame, text='Reference', style='green/black.TButton', command=lambda:draw_reference("local_file", "MIPS_Green_Sheet.pdf"))
    button5 = ttk.Button(main_frame, text='Exit', style='green/black.TButton', command=quit)

    button1.pack(pady=30)
    button2.pack(pady=30)
    button3.pack(pady=30)
    button4.pack(pady=30)
    button5.pack(pady=30)
    pass


def draw_lesson(root, ttk, lesson, submit_function, hint_function):
    # Set fonts for the menu widgets.
    # print(font.families()) to print available font families.
    menuLabel_font = font.Font(family="Loma", size=22, weight="bold")
    menuButton_font = font.Font(family="Loma", size=20, weight="normal")
    # background="..." doesn't work...
    ttk.Style().configure('B_DO1.TLabel', foreground='black', background='DarkOrange1', font=menuLabel_font)
    ttk.Style().configure('B_DO1.TButton', foreground='black', background='DarkOrange1', font=menuButton_font, width=15)

    lesson_header = tk.Frame(master=root, bg="medium blue")
    center_frame = tk.Frame(master=root, bg="medium blue")
    bottom_frame_top = tk.Frame(master=root, bg="medium blue")
    bottom_frame_bottom = tk.Frame(master=root, bg="medium blue")
    register_frame = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)

    registers = []
    draw_sidebar(register_frame, registers)

    # Pack lesson_header Frame over the top of the center_frame.
    register_frame.pack(expand=True, fill='both', side='left')
    lesson_header.pack(fill="x")
    center_frame.pack(expand=True, fill="both")
    bottom_frame_top.pack(expand=True, fill="both")
    bottom_frame_bottom.pack(expand=True, fill="both", side="bottom")

    label_instruction = ttk.Label(center_frame, text=lesson.lesson_prompt, style='B_DO1.TLabel')
    lesson_input = ttk.Entry(master=center_frame, font=menuLabel_font)
    lesson_input = tk.Text(center_frame, height=30, width=100)
    lesson_input.insert(tk.END, lesson.code_base)

    label_instruction.pack(side="top", pady=5)
    lesson_input.pack(pady=20, padx=10)


    hints = ''.join([str(i+1)+'. ' + lesson.lesson_hint[i] + '\n\n' for i in range(len(lesson.lesson_hint))])

    menu_escape = ttk.Button(bottom_frame_top, text='Main Menu', style='B_DO1.TButton', cursor="target",
                             command=lambda: transfer_to(lambda: draw_menu(root, ttk, lesson), center_frame,
                                                         bottom_frame_top, bottom_frame_bottom, register_frame))
    hint_button = ttk.Button(bottom_frame_bottom, text='Hint', style='B_DO1.TButton',
                             cursor="target", command=lambda: hint_function("Hint", hints))
    reference_button = ttk.Button(bottom_frame_bottom, text='Reference', style='B_DO1.TButton',
                                  cursor="target")#, command=draw_reference)

    popup_reference = Menu(root, tearoff=0, bg = '#f27446', font = 20)

    for reference in lesson.lesson_reference:
        popup_reference.add_command(label=reference['Name'], command=lambda r=reference: draw_reference(r['Type'],r['Path']))


    def do_popup_ref(event):
        # display the popup menu
        popup_reference.tk_popup(event.x_root, event.y_root, 0)


    reference_button.bind("<ButtonRelease-1>", do_popup_ref)

    submit_button = ttk.Button(bottom_frame_top, text='Submit Code', style='B_DO1.TButton',
                               cursor="target", command=lambda: submit_function(lesson_input, registers, lesson))

    menu_escape.pack(side='left', padx=10)
    submit_button.pack(side='right', padx=10)
    hint_button.pack(side='left', padx=10)
    reference_button.pack(side='right', padx=10)
    pass


def draw_sidebar(sidebar, registers):
    tk.Label(sidebar, text="NAME", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=0)
    tk.Label(sidebar, text="NUM", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=1)
    tk.Label(sidebar, text="VALUE", width=SIDEBAR_COLUMN_WIDTH).grid(row=0, column=2)

    for i in range(32):
        label = tk.Label(sidebar, text="0", width="5")
        label.grid(row=i + 1, column=2)
        registers.append(label)  # global arr so labels can be updated

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
    for i in range(32):
        tk.Label(sidebar, text=i, width=SIDEBAR_COLUMN_WIDTH).grid(row=i + 1, column=1)
    pass
