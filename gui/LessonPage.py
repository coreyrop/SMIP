import tkinter as tk
from lessons.Submission import run_MIPS
from lessons.Lesson_Transition import write_completed
from gui.Utilities import get_path
"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""

practice_filename = get_path('/lesson_files/Submissions/(Practice).s')


def get_submission_file(lesson):
    return get_path('/lesson_files/Submissions/'+lesson.lesson_title + '(Submission).s')


def submit_code(user_input, register_labels, lesson=None, is_practice=False):
    if is_practice:
        filename = practice_filename
    else:
        filename = get_submission_file(lesson)

    f = open(filename, 'w')
    f.write(user_input.get("1.0", tk.END))
    f.close()

    results = run_MIPS(filename)
    update_registers(results, register_labels)

    if not is_practice:
        if lesson.check_solution(results):
            lesson.lesson_completed = True
            write_completed(lesson.lesson_title, True)
            print('Passed!!')
        else:
            lesson.lesson_completed = False
            write_completed(lesson.lesson_title, False)
            print('Failed!!')
    pass


def get_text(lesson=None, is_practice=False):
    if is_practice:
        try:
            f = open(get_path(practice_filename))
        except FileNotFoundError:
            return '# Welcome to Practice! Write some code!!'
    else:
        try:
            filename = get_submission_file(lesson)
            f = open(filename, 'r')
        except FileNotFoundError:
            try:
                f = open(get_path(lesson.code_base), 'r')
            except FileNotFoundError:
                return "# No base code"
    output = ''.join(line for line in f.readlines())
    f.close()
    return output


def update_registers(answers, register_labels):
    for register, value in answers.items():
        register_labels[register].config(text=value)
    pass
