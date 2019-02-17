import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SMIP: The Student MIPS Instruction Program")
# Turning off pack propagate to prevent widgets from determining window size.
# Max and Min window sizes may change.
root.pack_propagate(0)
root.maxsize(1000, 1000)
root.minsize(450, 400)


# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='black', background='white')
ttk.Style().configure('green/black.TButton', foreground='black', background='white')

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
