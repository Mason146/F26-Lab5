# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Mason Chan
# Date: 10/23/2026
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
  # divide a by b
  # Add an exception block to raise the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    result = a / b
    print(result)
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Error
  
if __name__ == "__main__":
  main()