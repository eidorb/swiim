import glob
import os

def main():
    PY_UIC_PATH = '../../../swiimenv/Scripts/pyside-uic.exe'
    os.chdir(os.path.dirname(__file__))
    ui_files = glob.glob('*.ui')
    for ui_file in ui_files

if __name__ == '__main__':
    main()