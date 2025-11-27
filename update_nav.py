import os
from bs4 import BeautifulSoup

def update_nav(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {filepath}: {e}")
        return

    soup = BeautifulSoup(content, 'html.parser')

    # Locate the header nav
    nav = soup.find(id="headerNav")
    if not nav:
        # Try to find nav inside header if id is missing or different structure
        nav = soup.find("nav")

    if not nav:
        print(f"No navigation found in {filepath}")
        return

    # Check if Blog link exists
    existing_link = nav.find("a", string=lambda t: t and "Blog" in t)
    if existing_link:
        print(f"Blog link already exists in {filepath}")
        return

    # Determine relative path to blog.html
    # if filepath is index.html, href="blog.html"
    # if filepath is services/foo.html, href="../blog.html"

    depth = filepath.count(os.sep)
    if filepath.startswith("./"):
        depth -= 1

    if depth == 0:
        href = "blog.html"
    else:
        href = "../" * depth + "blog.html"

    # Create new link
    new_li = soup.new_tag("a", href=href)
    new_li.string = "Blog"
    new_li['class'] = "nav-link" # Assuming standard bootstrap/custom class

    # Insert it. Where? Usually before "Contact" or at the end.
    # Let's verify the structure. Usually nav contains a list or just 'a' tags.
    # If nav contains ul/li:
    ul = nav.find("ul")
    if ul:
        li = soup.new_tag("li")
        li.append(new_li)
        ul.append(li)
    else:
        # Just append to nav
        nav.append(new_li)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    print(f"Updated navigation in {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                update_nav(filepath)

if __name__ == "__main__":
    main()
