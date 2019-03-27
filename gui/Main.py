import tkinter as tk
from tkinter import ttk
from gui.Drawer import draw_menu
from gui.LessonPage import get_text
from lessons.Lesson import Lesson

root = tk.Tk()
root.title("SMIP: The Student MIPS Instruction Program")

sample_lesson = Lesson('Lesson 1: Register Addition'," Use the \'add\' instruction to set\n $t0 to 3,$t1 to 5,\n and then their sum in $t2.",
                       {8: 3, 9: 5, 10: 8}, " The add instruction expects a destination register followed by two source registers,"
               " which are comma separated.", ({'Name': "Green Sheet",'Type': "local_file",'Path': "MIPS_Green_Sheet.pdf"},{'Name':"Test Link", 'Type':"web_link", 'Path':"https://en.wikipedia.org/wiki/MIPS_architecture"}) , get_text())

# Turning off pack propagate to prevent widgets from determining window size.
# Max and Min window sizes may change.
root.pack_propagate(0)
# Max size of window is the dimensions of their screen.
their_width = root.winfo_screenwidth()
their_height = root.winfo_screenheight()
root.maxsize(their_width, their_height)
root.minsize(700, 800)
# Put app at the center of the screen.
x = (their_width / 2) - (700 / 2)
y = (their_height / 2) - (800 / 2)
root.geometry("%dx%d+%d+%d" % (700, 800, x, y))

draw_menu(root, ttk, sample_lesson)
root.mainloop()

