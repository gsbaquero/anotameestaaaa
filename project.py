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
        
