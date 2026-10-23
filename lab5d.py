# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/23/2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.
with open("pythonStatements.txt", "r") as pythonFile, open("machineCode.txt", "r") as machineFile, open("output.txt", "w") as outputFile:
    for pythonLine, machineLine in zip(pythonFile, machineFile):
        pythonLine = pythonLine.split("#")[0].strip()
        machineLine = machineLine.strip()
        outputFile.write(pythonLine + "\t" + machineLine + "\n")
