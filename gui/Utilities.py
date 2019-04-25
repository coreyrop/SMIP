from os.path import relpath
from tkinter.filedialog import askopenfilename
from pathlib import Path


top_path = str(Path().absolute())[:str(Path().absolute()).rfind('SMIP')+len('SMIP')]


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


def save_setting(choice):
    choice = str(choice.get())
    f = open("cur_set.txt", "w")
    if (choice == '1'):
        f.write("black,black,light grey,snow")
        pass

    elif(choice == '2'):
        f.write("black,blue2,light grey,snow")
        pass

    elif(choice == '3'):
        f.write("black,blue2,light grey,snow")
        pass

    f.close()
    print("Settings Saved Successfully")



def load_setting():
    f = open("cur_set.txt", "r")
    ans = []
    for x in f.readline().split(','):
        ans.append(x)

    return ans

