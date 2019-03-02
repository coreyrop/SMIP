import os, sys, subprocess

def draw_reference():

    dirname = os.path.dirname(__file__)

    #Removing gui folder from the absolute path
    dirname = dirname[:-3]
    
    filename = os.path.join(dirname,'References','MIPS_Green_Sheet.pdf')

    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

    pass