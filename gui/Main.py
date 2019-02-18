import tkinter as tk
from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("SMIP: The Student MIPS Instruction Program")

# Turning off pack propagate to prevent widgets from determining window size.
# Max and Min window sizes may change.
root.pack_propagate(0)
root.maxsize(1000, 1000)
root.minsize(525, 310)

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

label = ttk.Label(slide, text='\tWelcome to SMIP.\n Your Best Friend for Learning MIPS ', style='green/black.TLabel')
label.pack()

button1 = ttk.Button(slide, text='Start', style='green/black.TButton')
button2 = ttk.Button(slide, text='Select Lesson', style='green/black.TButton')
button3 = ttk.Button(slide, text='Practice', style='green/black.TButton')
button4 = ttk.Button(slide, text='Exit', style='green/black.TButton', command=quit)


def quit():
    root.destroy()


button1.pack()
button2.pack()
button3.pack()
button4.pack()
root.mainloop()
