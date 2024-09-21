import sys
import os
import os.path

def main():
    valid_file()


def count_line(path):
        line_no_empty= 0
        with open(path) as file:
            #line_no_com = file.readline()
            for line in file:
                if line.strip() and not line.strip().startswith('#') :  # Check if the line is not empty after stripping whitespace
                    line_no_empty = line_no_empty + 1

        return line_no_empty


def valid_file():
    file = len(sys.argv)
    if file <=1:
        sys.exit('Too few command-line arguments')
    elif file >2:
        sys.exit('Too many command-line arguments')
    elif file ==2:
        if sys.argv[1].endswith('.py'):
            if os.path.isfile(sys.argv[1])==True:
                print(count_line(sys.argv[1]))
            else:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')

# count line
#count_line('hello.py')
valid_file()
