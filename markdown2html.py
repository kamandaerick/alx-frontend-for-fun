#!/usr/bin/env python3
"""This script converts a markdown file to HTML by parsing headings."""
import sys
import os

if __name__ == '__main__':
    # Step 1: Check if the number of arguments is correct
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Step 2: Check if the input file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    try:
        # Step 3: Open the input markdown file and output HTML file
        with open(input_file, 'r') as markdown_file, open(output_file, 'w') as html_file:
            # Step 4: Process each line in the markdown file
            for line in markdown_file:
                line = line.strip()  # Remove leading/trailing whitespace
                
                # Check if the line starts with a heading (up to 6 levels)
                if line.startswith('#'):
                    # Count the number of `#` symbols to determine heading level
                    heading_level = len(line.split(' ')[0])  # Count `#`
                    
                    # Ensure we are within valid heading levels (1 to 6)
                    if 1 <= heading_level <= 6:
                        # Get the content of the heading (text after the `#`)
                        heading_content = line[heading_level:].strip()
                        # Write the corresponding HTML heading tag
                        html_file.write(f"<h{heading_level}>{heading_content}</h{heading_level}>\n")
                    else:
                        # In case it's an invalid heading level (though per instruction it's strictly correct)
                        sys.stderr.write(f"Invalid heading syntax: {line}\n")
                        sys.exit(1)
                else:
                    # For now, we are ignoring other markdown elements
                    pass

        # Exit with success code
        sys.exit(0)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)