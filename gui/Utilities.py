from os.path import relpath
from tkinter.filedialog import askopenfilename
from pathlib import Path

p = str(Path().absolute())
i = p.rfind('SMIP')
top_path = p[:i+len('SMIP')]


"""
Destroys all content inside of the given frame
frame: frame who's content will be destroyed
"""


def destroy_content(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    pass


def get_relative_file_path(filetypes):
    try:
        s = askopenfilename(filetypes=filetypes)
        return '/'+relpath(s, top_path)
    except ValueError:
        return 'None Set'


def get_path(relpath):
    return top_path + relpath

"""
Destroys the given frames content and then draws new content to that frame using the given function
current_frame: frame who's content will be changed
draw_function: function that will be called to draw new content
"""


def transfer_to(draw_function, *args):
    for frame in args:
        frame.destroy()
    draw_function()
    pass