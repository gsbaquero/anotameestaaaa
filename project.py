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


if "__name__" == "__main__":
    reader = FileReader()
    print("contenido del archivo test.txt=")
    for line in reader.lines:
        print(line)
        
