This repository contains a Python program for reading, writing, 
and managing .txt files using Object-Oriented Programming (OOP) principles, 2 txt files with their own texts and
one python program for testing the main code

Description

The first script (project_2.py) defines two main classes:
  •	FileReader: A base class that allows you to:
	  •	Read files line by line
  	•	Get and set the full content of a file
	  •	Combine two or more .txt files
	  •	Check if a file has a .txt extension
	•	AdvancedFileReader: An extended version of FileReader with additional functionality:
  	•	Counts the total number of words in a file
  	•	Prints the file content with colored output using a custom decorator
 
There’s also a deco(color) decorator that adds ANSI color codes to console output.

The second script (test_2.py) defines diverse tests for the main code:
  • verifies if file ends in.txt
  • verifies that a file is being used and specifies number of lines
  • Creates new file combining 2 texts
  • verifies that combination code is well written
  • Combines multiple files in 1
  • Count words in a file 
  • verifies if decorator color the text as it should

How to Use
  1. make sure you are using Python 3.13
  2. make sure that you have one or two .txt files with any content with name text1 and text2
  3. make sure all scripts are in the same folder
  4. run the script

have fun :)
