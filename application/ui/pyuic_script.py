import argparse
import glob
import os

def parse_arguments():
    """Parse command line arguments and return the path to pyuic."""
    parser = argparse.ArgumentParser(
        description='Convert modified Qt Designer ui files using pyuic.')
    parser.add_argument('pyuic_path', type=str)
    args = parser.parse_args()
    return args.pyuic_path

def modified_ui_files():
    """Return (ui, py) filename pairs for ui files that have been modified or
    newly created.

    """
    os.chdir(os.path.dirname(__file__))
    for ui_file in glob.iglob('*.ui'):
        py_file = os.path.splitext(ui_file)[0] + '.py'
        try:
            ui_file_mtime = os.path.getmtime(ui_file)
            py_file_mtime = os.path.getmtime(py_file)
            if ui_file_mtime > py_file_mtime:
                # A py file will need to be generated if the ui file has been
                # modified.
                yield ui_file, py_file
        except os.error:
            # If the py file doesn't exist, it will need to be generated.
            yield ui_file, py_file

def main():
    pyuic_path = parse_arguments()
    for ui_file, py_file in modified_ui_files():
        pyuic_command = ' '.join(
            (pyuic_path, '-x', '--output=' + py_file, ui_file))
        print 'Generating', py_file, 'from', ui_file
        os.system(pyuic_command)

if __name__ == '__main__':
    main()