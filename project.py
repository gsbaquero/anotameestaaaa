"""project_2.py: Program for reading and handling text files using OOP."""

import os
from functools import wraps


def deco(color):
    """Decorador para colorear la salida en consola usando códigos ANSI."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            colors = {
                'red': '\033[91m',
                'green': '\033[92m',
                'yellow': '\033[93m',
                'reset': '\033[0m',
            }
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
    """Clase para leer y escribir archivos línea por línea."""

    def __init__(self):
        """Inicializa el FileReader con la ruta del archivo."""
        self.filepath = "test.txt"

    def read_lines(self):
        """Generador que retorna cada línea del archivo sin espacios al final."""
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()

    @property
    def lines(self):
        """Devuelve todas las líneas como una lista."""
        return list(self.read_lines())

    @lines.setter
    def lines(self, new_lines):
        """Sobrescribe el archivo con nuevas líneas."""
        with open(self.filepath, 'w', encoding='utf-8') as file:
            for line in new_lines:
                file.write(line + '\n')
    
    def __str__(self):
        """Devuelve una descripción del archivo y cantidad de líneas."""
        return f"FileReader({self.filepath}) with {len(self.lines)} lines"

    @staticmethod
    def is_text_file(filename):
        """Verifica si un archivo tiene extensión .txt."""
        return filename.endswith('.txt')

    @classmethod
    def from_two_files(cls, file1, file2, output='combined.txt'):
        """Combina el contenido de dos archivos en uno nuevo."""
        with open(output, 'w', encoding='utf-8') as out:
            for path in (file1, file2):
                with open(path, 'r', encoding='utf-8') as file:
                    out.write(file.read())
                    out.write('\n')
        return cls(output)

    def __add__(self, other):
        """Permite sumar dos instancias para combinar archivos."""
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
        """Combina múltiples archivos en uno solo."""
        with open(output, 'w', encoding='utf-8') as out:
            for filename in files:
                with open(filename, 'r', encoding='utf-8') as file:
                    out.write(file.read())
                    out.write('\n')
        return cls(output)

if "__name__" == "__main__":
    reader = FileReader()
    print("contenido del archivo test.txt=")
    for line in reader.lines:
        print(line)
        
