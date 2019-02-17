import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='black', background='black')
ttk.Style().configure('green/black.TButton', foreground='black', background='black')

label = ttk.Label(root, text='Welcome to SMIP. Your Best Friend for Learning MIPS', style='green/black.TLabel')
label.pack()

button1 = ttk.Button(root, text='Start', style='green/black.TButton')
button2 = ttk.Button(root, text='Select Lesson', style='green/black.TButton')
button3 = ttk.Button(root, text='Practice', style='green/black.TButton')
button4 = ttk.Button(root, text='Exit', style='green/black.TButton')

button1.pack()
button2.pack()
button3.pack()
button4.pack()
root.mainloop()
