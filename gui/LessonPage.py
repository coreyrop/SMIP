import tkinter as tk
from tkinter import font, messagebox
from lessons.Submission import run_MIPS
from lessons.Lesson_Transition import write_completed
from gui.Utilities import get_path
from os import remove, path
import shutil

"""
Draws a lesson to the frame
root: tkinter root to draw to 
ttk: tkinter ttk used for styling
lesson: the lesson to be drawn to the screen
"""

practice_filename = get_path("/lesson_files/Submissions/(Practice).s")


def get_submission_file(lesson):
    return get_path(
        "/lesson_files/Submissions/" + lesson.lesson_title + "(Submission).s"
    )


def submit_code(
    root, center_frame, user_input, register_labels, lesson=None, is_practice=False
):
    if is_practice:
        filename = practice_filename
    else:
        filename = "temp.s"

    f = open(filename, "w")
    f.write(user_input.get("1.0", tk.END))
    f.close()

    results = run_MIPS(filename)
    update_registers(results, register_labels)
    menuButton_font = font.Font(family="Loma", size=22, weight="bold")

    if not is_practice:
        if lesson.check_solution(results):
            shutil.copy(filename, get_submission_file(lesson))
            lesson.lesson_completed = True
            write_completed(lesson.lesson_title, True)

            alert = tk.Label(
                center_frame,
                background="green2",
                text="    PASSED    ",
                font=menuButton_font,
            )
            alert.grid(row=4, column=2)
            root.update()
            alert.after(3000, alert.grid_forget())

        else:
            alert = tk.Label(
                center_frame,
                background="red2",
                text="    FAILED    ",
                font=menuButton_font,
            )
            alert.grid(row=4, column=2)
            root.update()
            alert.after(3000, alert.grid_forget())

            if lesson.lesson_completed and path.isfile(get_submission_file(lesson)):
                if messagebox.askyesno(
                    "Overwrite Correct Submission?",
                    "You have a correct submission saved, would you like to overwrite it with this incorrect submission?",
                ):
                    shutil.copy(filename, get_submission_file(lesson))
                    lesson.lesson_completed = False
                    write_completed(lesson.lesson_title, False)
            else:
                shutil.copy(filename, get_submission_file(lesson))
                lesson.lesson_completed = False
                write_completed(lesson.lesson_title, False)
        remove(filename)
    pass


def get_text(lesson=None, is_practice=False):
    if is_practice:
        try:
            f = open(practice_filename)
        except FileNotFoundError:
            return "# Welcome to Practice! Write some code!!"
    else:
        try:
            filename = get_submission_file(lesson)
            f = open(filename, "r")
        except FileNotFoundError:
            try:
                f = open(get_path(lesson.code_base), "r")
            except FileNotFoundError:
                return "# No base code"
    output = "".join(line for line in f.readlines())
    f.close()
    return output


def update_registers(answers, register_labels):
    for register, value in answers.items():
        register_labels[register].config(text=value)
    pass
