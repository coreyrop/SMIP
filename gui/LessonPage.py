import tkinter as tk
from lessons.Submission import run_MIPS
"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""


def submit_code(user_input, register_labels, lesson):
    f = open('input.s', 'w')
    f.write(user_input.get("1.0", tk.END))
    f.close()

    results = run_MIPS('input.s')
    update_registers(results, register_labels)

    if lesson.check_solution(results):
        print('Passed!!')
    else:
        print('Failed!!')
    pass


def get_text():
    f = open('Sample1.s', 'r')
    output = ""
    for x in f.readlines():
        output += x
    f.close()
    return output


def update_registers(answers, register_labels):
    for register, value in answers.items():
        register_labels[register].config(text=value)
    pass


