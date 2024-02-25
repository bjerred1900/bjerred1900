"""Syftet med denna modul är att i varje fil i slutet lägga till en lista med länkar till andra artiklar som har en referens till denna artikel."""
import os
import re

def update_inbound_references() -> None:
    """For each Markdown (.md) file in the root directory (in each iteration called the current file).
    First, see if there is a section called "Referenser till denna artikel" in the file. If yes, remove that section and its content. We expect this file to be a level 2 header.
    Then scan every other markdown file in the root directory.
    Detect if there is an instance of standard GitHub link (example: [Current file](Current file.md)) linking to the current file.
    If there is, store a reference to the name of that file.
    Once we have a list of all references, then append a new level 2 Markdown section at the end of the current file called "Referenser till denna artikel"
    and list all the references in a bullet point format."""
    md_files = [f for f in os.listdir() if f.endswith('.md')]
    
    for current_file in md_files:
        with open(current_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove existing "Referenser till denna artikel" section
        content = re.sub(r'\n## Referenser till denna artikel\n.*', '', content, flags=re.DOTALL)
        
        references = []
        
        # Scan every other markdown file for references to the current file
        for file in md_files:
            if file == current_file:
                continue
            
            with open(file, 'r', encoding='utf-8') as f:
                other_content = f.read()
            
            # Remove existing "Referenser till denna artikel" section in the other file's content as to not count it as a reference
            other_content = re.sub(r'\n## Referenser till denna artikel\n.*', '', other_content, flags=re.DOTALL)
            
            # Check if current file is linked within another file
            pattern = rf'\[{re.escape(current_file[:-3])}\]\({re.escape(current_file)}\)'
            if re.search(pattern, other_content):
                references.append(file[:-3])  # Remove .md extension
        
        # Append new references section if there are any references
        if references:
            content += '\n## Referenser till denna artikel\n\n'
            ref: str
            for ref in references:
                link_without_spaces: str = ref.replace(' ', '%20')
                content += f'* [{ref}]({link_without_spaces}.md)\n'
        
        # Write the modified content back to the file
        with open(current_file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_inbound_references()
