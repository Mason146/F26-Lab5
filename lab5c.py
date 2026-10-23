# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/23/2026
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
with open("rhyme.txt", "w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

# TO DO 2: Open rhyme.txt file.
dataFile = open("rhyme.txt", "r")
line = dataFile.readline()

# TO DO 3: Print the output as directed in readme.md file.
while line:
    line = line.strip()
    line = line.strip(".")
    words = line.split()
    print(line, "---", len(words), "words")
    line = dataFile.readline()

dataFile.close()
