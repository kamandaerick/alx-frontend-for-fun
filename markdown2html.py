#!/usr/bin/python3
"""This scripts checks the number of args passed and if a file exists"""
import sys
import os
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}".format(sys.argv[1]))
        sys.exit(1)
    sys.exit(0)