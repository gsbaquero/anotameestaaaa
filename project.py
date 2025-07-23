"""project_2.py: Program for reading and handling text files using OOP."""

import os
from functools import wraps

def deco(color):
    """Decorator that applies color to the output using ANSI CODES."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            colors = {
                'red': '\033[91m',
                'green': '\033[92m',
                'yellow': '\033[93m',
                'reset': '\033[0m',
            }

            """"If the color is not in the dictionary,
              it uses the reset color."""
            if color in colors:
                start = colors[color]
            else:
                start = colors['reset']
            
            end = colors['reset']
            result = func(*args, **kwargs)
            return f"{start}{result}{end}"
        return wrapper
    return decorator


class FileReader:
    """Class that reads and writes text files line by line."""

    def __init__(self, filepath):
        """Initializes the FileReader."""
        self.filepath = filepath

    def read_lines(self):
        """Generator that returns all the lines without whitespaces."""
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()

    @property
    def lines(self):
        """Returns all lines as a list."""
        return list(self.read_lines())

    @lines.setter
    def lines(self, new_lines):
        """Overwrites the file with new lines."""
        with open(self.filepath, 'w', encoding='utf-8') as file:
            for line in new_lines:
                file.write(line + '\n')

    def __str__(self):
        """returns the amount of lines in the file."""
        return f"FileReader({self.filepath}) with {len(self.lines)} lines"

    @staticmethod
    def is_text_file(filename):
        """checks if the file is a .txt file."""
        return filename.endswith('.txt')
    

    def __add__(self, other):
        """Allows adding two instances to combine files."""
        if not isinstance(other, FileReader):
            raise TypeError("Can only add FileReader instances together.")

        base1 = os.path.splitext(os.path.basename(self.filepath))[0]
        base2 = os.path.splitext(os.path.basename(other.filepath))[0]
        new_filename = f"{base1}_{base2}_combined.txt"
        directory = os.path.dirname(self.filepath) or '.'
        new_filepath = os.path.join(directory, new_filename)

        with open(new_filepath, 'w', encoding='utf-8') as out:
            with open(self.filepath, 'r', encoding='utf-8') as f1, \
                 open(other.filepath, 'r', encoding='utf-8') as f2:
                out.write(f1.read())
                out.write('\n')
                out.write(f2.read())

        return FileReader(new_filepath)

    @classmethod
    def combine_multiple_files(cls, *files, output='combined_multiple.txt'):
        """Combines multiple files into a single one."""
        with open(output, 'w', encoding='utf-8') as out:
            for filename in files:
                with open(filename, 'r', encoding='utf-8') as file:
                    out.write(file.read())
                    out.write('\n')
        return cls(output)


class AdvancedFileReader(FileReader):
    """Extends FileReader with additional functions like word counting 
    and colorized output."""

    def word_count(self):
        """Counts the total number of words in the file."""
        count = 0
        for line in self.read_lines():
            count += len(line.split())
        return count

    @deco('red')
    def print_content(self):
        """Prints the content of the file with color using the decorator."""
        return "\n".join(self.lines)




if __name__ == '__main__':
    file1= FileReader("test.txt")
    file2= FileReader("test2.txt")
    reader = AdvancedFileReader("test.txt")
    print(reader.print_content())
    print(f"Words: ", reader.word_count())
    print(FileReader.combine_multiple_files(file1.filepath, file2.filepath, output='combined.txt'))
    combined = file1 + file2
    print("\n".join(combined.lines))
    print(reader) 

