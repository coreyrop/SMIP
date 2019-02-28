import os, sys, subprocess

def draw_reference():

    filename = 'MIPS_Green_Sheet.pdf'

    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

    pass