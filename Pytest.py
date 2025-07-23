"""Pytest for project_2 module."""
import os
import pytest
from project_2 import FileReader, AdvancedFileReader, deco

@pytest.fixture
def file_a():
    """Create a sample file, which will be used and deleted after the test."""
    path = "file_a.txt"
    content = ["Alpha line one", "Alpha line two"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    yield path
    os.remove(path)

@pytest.fixture
def file_b():
    """Create a sample file, which will be used and deleted after the test."""
    path = "file_b.txt"
    content = ["Beta line one", "Beta line two"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    yield path
    os.remove(path)

@pytest.fixture
def file_c():
    """Create a sample file, which will be used and deleted after the test."""
    path = "file_c.txt"
    content = ["Charlie line one", "Charlie line two"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    yield path
    os.remove(path)


def test_is_text_file():
    """Test if it correctly identifies text files."""
    assert FileReader.is_text_file("doc.txt") is True
    assert FileReader.is_text_file("image.png") is False

def test_str(file_a):
    """Test how the FileReader instance is represented as a string."""
    """Returns the filepath and number of lines."""
    reader = FileReader(file_a)
    result = str(reader)
    assert "FileReader(file_a.txt)" in result
    assert "2 lines" in result

def test_add_operator(file_a, file_b):
    """Creates a new file combining both contents"""
    reader1 = FileReader(file_a)
    reader2 = FileReader(file_b)
    combined_reader = reader1 + reader2
    assert isinstance(combined_reader, FileReader)
    assert os.path.exists(combined_reader.filepath)
    with open(combined_reader.filepath, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Alpha line one" in content
    assert "Beta line one" in content
    os.remove(combined_reader.filepath)

def test_add_operator_invalid_type(file_a):
    """Raises TypeError when trying to add FileReader with non-FileReader type."""
    reader = FileReader(file_a)
    with pytest.raises(TypeError):
        _ = reader + 5

def test_combine_multiple_files(file_a, file_b, file_c):
    """Tests combining multiple files into one, all contents should be in the combined file."""
    output_file = "combined_multiple.txt"
    reader = FileReader.combine_multiple_files(file_a, file_b, file_c, output=output_file)
    assert isinstance(reader, FileReader)
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Alpha line one" in content
    assert "Beta line one" in content
    assert "Charlie line one" in content
    os.remove(output_file)

def test_word_count(file_a):
    """Test if the word count function works correctly, based on the content of file_a."""
    reader = AdvancedFileReader(file_a)
    assert reader.word_count() == 6

def test_decorator_colors():
    """Test if the decorator applies the correct ANSI color codes."""
    @deco("red")
    def sample():
        return "color1"

    @deco("green")
    def sample2():
        return "color2"

    @deco("black")
    def sample3():
        return "color3"

    assert "\033[91mcolor1\033[0m" == sample()
    assert "\033[92mcolor2\033[0m" == sample2()
    assert "\033[0mcolor3\033[0m" == sample3()
