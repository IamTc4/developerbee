import os
from bs4 import BeautifulSoup
import re

def parse_blog_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    title = soup.find('h1').get_text().strip() if soup.find('h1') else "Untitled Post"

    # Try to find meta description
    meta = soup.find('meta', attrs={'name': 'description'})
    excerpt = meta['content'] if meta else "Read this insightful article about software development and business growth."

    # Try to find date (maybe in a time tag or distinct class)
    # If not found, use file modification date or default
    date = "2024"

    # Construct relative link
    # blog.html is in root. Post is in blogs/
    link = filepath # e.g. blogs/foo.html

    return {
        "title": title,
        "excerpt": excerpt,
        "link": link,
        "date": date
    }

def generate_blog_index():
    posts = []
    blog_dir = "blogs"

    if not os.path.exists(blog_dir):
        print("No blogs directory found.")
        return

    for file in os.listdir(blog_dir):
        if file.endswith(".html"):
            posts.append(parse_blog_post(os.path.join(blog_dir, file)))

    # Generate HTML content
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeveloperBee Blog - Insights on Web Development & SEO</title>
    <meta name="description" content="Read the latest insights, tips, and strategies on web development, mobile apps, and SEO from DeveloperBee experts.">
    <link rel="canonical" href="https://developerbee.digital/blog.html">
    <link rel="stylesheet" href="static/style.css">
    <link rel="stylesheet" href="static/mobile-optimization.css">
    <style>
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            padding: 2rem 5%;
        }
        .blog-card {
            border: 1px solid #eee;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.2s;
            background: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .blog-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .blog-card h2 {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            color: #333;
        }
        .blog-card p {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
            line-height: 1.5;
        }
        .read-more {
            color: #007bff;
            text-decoration: none;
            font-weight: 500;
        }
        .hero-section {
            background: #f8f9fa;
            padding: 4rem 5%;
            text-align: center;
        }
        .hero-section h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <header>
        <!-- Placeholder for Nav, will be populated or handled by JS/include -->
        <nav id="headerNav" style="display: flex; justify-content: space-between; padding: 1rem 5%; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div class="logo"><a href="index.html" style="font-weight:bold; font-size:1.2rem; text-decoration:none; color:#333;">DeveloperBee</a></div>
            <div class="nav-links">
                <a href="index.html" style="margin-left: 1rem;">Home</a>
                <a href="services.html" style="margin-left: 1rem;">Services</a>
                <a href="projects.html" style="margin-left: 1rem;">Projects</a>
                <a href="contact.html" style="margin-left: 1rem;">Contact</a>
            </div>
        </nav>
    </header>

    <section class="hero-section">
        <h1>Our Latest Insights</h1>
        <p>Expert advice on Software, SEO, and Business Growth.</p>
    </section>

    <section class="blog-grid">
"""

    for post in posts:
        html += f"""
        <article class="blog-card">
            <h2>{post['title']}</h2>
            <p>{post['excerpt']}</p>
            <a href="{post['link']}" class="read-more">Read Article &rarr;</a>
        </article>
"""

    html += """
    </section>

    <footer style="background: #333; color: #fff; padding: 2rem 5%; text-align: center; margin-top: 3rem;">
        <p>&copy; 2025 DeveloperBee. All rights reserved.</p>
    </footer>

    <script src="static/header.js"></script>
</body>
</html>
"""

    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated blog.html with {len(posts)} posts.")

if __name__ == "__main__":
    generate_blog_index()
