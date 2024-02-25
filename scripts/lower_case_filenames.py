"""Syftet med denna modul är att normalisera filnamn till lowercase."""
import os
import re

def lowercase_filenames() -> None:
    """Scan each Markdown (.md) file in the root directory. Ensure each file name is lowercase."""
    for file in os.listdir():
        if file.endswith('.md'):
            os.rename(file, file.lower())
    # also check for each jpg, jpeg, png, gif, and svg file in the images directory
    for file in os.listdir('images'):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.svg'):
            os.rename(f'images/{file}', f'images/{file.lower()}')

if __name__ == '__main__':
    lowercase_filenames()
