import os
from bs4 import BeautifulSoup
import re

def optimize_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Ensure head exists
    if not soup.head:
        if not soup.html:
            new_html = soup.new_tag("html")
            soup.append(new_html)
        if not soup.html.head:
            new_head = soup.new_tag("head")
            soup.html.insert(0, new_head)

    head = soup.head

    # 1. Canonical Tag
    # Base logic: Use https://developerbee.digital + relative path
    # For blogs/foo.html -> https://developerbee.digital/blogs/foo.html
    rel_path = filepath
    if rel_path.startswith("./"):
        rel_path = rel_path[2:]

    canonical_url = f"https://developerbee.digital/{rel_path}"

    canonical_tag = head.find('link', rel='canonical')
    if canonical_tag:
        canonical_tag['href'] = canonical_url
    else:
        new_tag = soup.new_tag("link", rel="canonical", href=canonical_url)
        head.append(new_tag)

    # 2. Meta Description & Keywords (Check if missing)
    meta_desc = head.find('meta', attrs={'name': 'description'})
    if not meta_desc:
        # Generate a generic one or based on H1
        h1 = soup.find('h1')
        desc_text = h1.get_text().strip() if h1 else "DeveloperBee - Custom Software Development & Digital Marketing Agency"
        desc_text = f"{desc_text}. Expert web development, app creation, and SEO services in India."
        new_meta = soup.new_tag("meta", attrs={"name": "description", "content": desc_text})
        head.append(new_meta)

    meta_keywords = head.find('meta', attrs={'name': 'keywords'})
    if not meta_keywords:
         # Add generic keywords
        keywords = "software development, web development, app development, SEO, digital marketing, Mumbai, India, developerbee"
        new_meta = soup.new_tag("meta", attrs={"name": "keywords", "content": keywords})
        head.append(new_meta)

    # 3. Viewport (Mobile responsiveness)
    viewport = head.find('meta', attrs={'name': 'viewport'})
    if not viewport:
        new_meta = soup.new_tag("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0"})
        head.append(new_meta)

    # 4. Save changes
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

def main():
    for root, dirs, files in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                print(f"Optimizing {filepath}...")
                optimize_html_file(filepath)

if __name__ == "__main__":
    main()
