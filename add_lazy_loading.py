import os
from bs4 import BeautifulSoup

def add_lazy_loading(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    images = soup.find_all('img')
    modified = False
    for img in images:
        if not img.has_attr('loading'):
            img['loading'] = 'lazy'
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        print(f"Added lazy loading to {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                add_lazy_loading(filepath)

if __name__ == "__main__":
    main()
