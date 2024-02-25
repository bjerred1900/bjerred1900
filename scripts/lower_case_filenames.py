"""Syftet med denna modul är att normalisera filnamn till lowercase."""
import os
import re

def lowercase_markdown_filenames() -> None:
    """Scan each Markdown (.md) file in the root directory. Ensure each file name is lowercase."""
    for file in os.listdir():
        if file.endswith('.md'):
            os.rename(file, file.lower())

if __name__ == '__main__':
    lowercase_markdown_filenames()
