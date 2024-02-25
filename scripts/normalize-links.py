"""Syftet med denna modul är att normalisera länkar i markdown-filer."""
import os
import re

def normalize_links() -> None:
    """Scan each Markdown (.md) file in the root directory.
    Find each instance of a wiki link (example: [[Linked file]])
    and normalize to a standard link format (example: [Linked file](Linked file.md))."""
    for file in os.listdir():
        if file.endswith('.md'):
            with open(file, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding here
                content = f.read()
            links = re.findall(r'\[\[(.*?)\]\]', content)
            for link in links:
                content = content.replace(f'[[{link}]]', f'[{link}]({link}.md)')

            # for each link ([file name](file name.md)) in the content, replace spaces with %20, like this: ([file name](file%20name.md))
            content = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', lambda m: f'[{m.group(1)}]({m.group(2).replace(" ", "%20")})', content)
            with open(file, 'w', encoding='utf-8') as f:  # And also here
                f.write(content)

if __name__ == '__main__':
    normalize_links()
