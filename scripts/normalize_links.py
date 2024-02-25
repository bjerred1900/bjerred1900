"""Syftet med denna modul är att normalisera länkar i markdown-filer."""
import os
import re

def normalize_links() -> None:
    """Scan each Markdown (.md) file in the root directory.
    Find each instance of a wiki link (example: [[Linked file]])
    and normalize to a standard link format (example: [Linked file](Linked file.md))."""

    for file in os.listdir():
        # Only process .md files
        if file.endswith('.md'):
            # Read the file's content
            with open(file, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding here
                content = f.read()

            # find all wiki links in the content
            links = re.findall(r'\[\[(.*?)\]\]', content)

            # for each link in the content
            for link in links:
                # replace it with a standard markdown link
                content = content.replace(f'[[{link}]]', f'[{link}]({link})')

            # for each link ([file name](file name)) in the content, replace spaces with %20, like this: ([file name](file%20name))
            content = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', lambda m: f'[{m.group(1)}]({m.group(2).replace(" ", "%20")})', content)

            # also remove any .md link endings if they exist
            content = re.sub(r'\.md\)', ')', content)

            # also lowercase all links (not the link text, just the link itself)
            content = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', lambda m: f'[{m.group(1)}]({m.group(2).lower()})', content)
            
            # Write the modified content back to the file
            with open(file, 'w', encoding='utf-8') as f:  # And also here
                f.write(content)

if __name__ == '__main__':
    normalize_links()
