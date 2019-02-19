import tkinter as tk
from tkinter import ttk
from gui.MainMenu import draw_menu

root = tk.Tk()
root.title("SMIP: The Student MIPS Instruction Program")

# Turning off pack propagate to prevent widgets from determining window size.
# Max and Min window sizes may change.
root.pack_propagate(0)
root.maxsize(1000, 1000)
root.minsize(525, 310)

draw_menu(root, ttk)
root.mainloop()
