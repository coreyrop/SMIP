import os
import sys

if __name__ == '__main__':
    for dir_path, dir_name, filename in os.walk(os.getcwd()):
        if (str(dir_path).find('__pycache__') == -1 and str(dir_path).find('.vscode') == -1):
            sys.path.append(dir_path)

    from gui.Main import main
    main()