import tkinter as tk
from lessons.Submission import run_MIPS
"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""


def submit_code(user_input, register_labels, lesson):
    filename = '../lesson_files/Submissions/'+lesson.lesson_title + '(Submission).s'
    f = open(filename, 'w')
    f.write(user_input.get("1.0", tk.END))
    f.close()

    results = run_MIPS(filename)
    update_registers(results, register_labels)


    if lesson.check_solution(results):
        print('Passed!!')
    else:
        print('Failed!!')
    pass


def run_practice(user_input, register_labels):
    filename = '../lesson_files/Submissions/(Practice).s'
    f = open(filename, 'w')
    f.write(user_input.get("1.0", tk.END))
    f.close()
    results = run_MIPS(filename)
    update_registers(results, register_labels)
    print(" SMIP RUNS YOUR  CODE ")
    print(results)
    pass


def get_text(filename):
    try:
        f = open(filename, 'r')
        output = ""
        for x in f.readlines():
            output += x
        f.close()
        return output
    except FileNotFoundError:
        return "No base code"


def update_registers(answers, register_labels):
    for register, value in answers.items():
        register_labels[register].config(text=value)
    pass


