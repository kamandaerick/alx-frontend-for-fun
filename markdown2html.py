#!/usr/bin/python3
"""This script checks the number of args passed and if a file exists."""
import sys
import os

# Correct __name__ comparison
if __name__ == '__main__':
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    
    # Check if the input file exists
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        sys.exit(1)

    # If all checks pass, exit silently
    sys.exit(0)