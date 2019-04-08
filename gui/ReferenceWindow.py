import os, sys, subprocess, webbrowser, enum


class Reference(enum.Enum):
    web_link = 'web_link'
    local_file = 'local_file'


def draw_reference_path(file_path):

    dirname = os.path.dirname(__file__)

    #Removing gui folder from the absolute path
    dirname = dirname[:-3]
    
    filename = os.path.join(dirname,'References', file_path)

    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

    pass


def draw_reference_link(file_link):
    webbrowser.open(file_link)


def draw_reference(type, path):
    if Reference[type].value == Reference.local_file.value:
        draw_reference_path(file_path = path)
    elif Reference[type].value == Reference.web_link.value:
        draw_reference_link(file_link = path)

