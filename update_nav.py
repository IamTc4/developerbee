import os
from bs4 import BeautifulSoup

def add_blog_link(filepath, rel_prefix=""):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    nav = soup.find('ul', id='headerNav')
    if nav:
        # Check if Blog link already exists
        if not nav.find('a', string="Blog"):
            # Create new list item
            li = soup.new_tag("li")

            # Determine correct href
            href = "blog.html"
            if filepath.startswith("./blogs/") or filepath.startswith("blogs/") or \
               filepath.startswith("./projects/") or filepath.startswith("projects/") or \
               filepath.startswith("./services/") or filepath.startswith("services/") or \
               filepath.startswith("./geo/") or filepath.startswith("geo/"):
                 href = "../blog.html"

            a = soup.new_tag("a", href=href)
            a.string = "Blog"
            li.append(a)

            # Insert before "About Us" or "Contact" or at the end
            about_link = nav.find('a', href=lambda x: x and "about.html" in x)
            if about_link:
                about_link.parent.insert_before(li)
            else:
                nav.append(li)

            print(f"Added Blog link to {filepath}")

            # Save
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
        else:
             print(f"Blog link already exists in {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html") and file != "blog.html":
                filepath = os.path.join(root, file)
                add_blog_link(filepath)

if __name__ == "__main__":
    main()
