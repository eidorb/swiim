import argparse
import os
import pysideuic

def parse_arguments():
    """Parse command line arguments and return the path to the ui directory."""
    def directory(path):
        if os.path.isdir(path):
            return path
        else:
            raise argparse.ArgumentTypeError(
                '{} is not a directory'.format(path))
    parser = argparse.ArgumentParser(
        description= 'Convert Qt Designer ui files to Python modules.')
    parser.add_argument(
        'dir',
        nargs='?',
        default=os.getcwd(),
        type=directory,
        help='directory containing ui files (default: current directory)')
    args = parser.parse_args()
    return args.dir

def main():
    dir = parse_arguments()
    class bogus_string(str):
        """A string subclass with the string formatting operator overridden."""
        def __mod__(*args):
            """Instead of formatting, an empty string is returned."""
            return ''
    # Replace pysideuic's _header so that a header isn't created in the
    # generated Python module.
    pysideuic._header = bogus_string()
    pysideuic.compileUiDir(dir)

if __name__ == '__main__':
    main()