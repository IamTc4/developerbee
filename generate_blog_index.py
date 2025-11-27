import os
from bs4 import BeautifulSoup
import re

def create_blog_index():
    blog_dir = "blogs"
    blog_files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]
    blog_files.sort()

    # Base template structure (borrowed from index.html)
    template_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeveloperBee Blog | Insights on Tech, SEO, and Growth</title>
    <meta name="description" content="Read the latest insights from DeveloperBee on software development, SEO, digital marketing, and business growth strategies.">
    <link rel="canonical" href="https://developerbee.digital/blog.html">
    <link rel="icon" type="image/x-icon" href="static/Design.jpeg">
    <link rel="stylesheet" href="static/style.css">
    <link rel="stylesheet" href="static/mobile-optimization.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 4rem 5%;
            max-width: 1200px;
            margin: 0 auto;
        }
        .blog-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(95, 247, 255, 0.2);
            border-radius: 12px;
            padding: 2rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .blog-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(95, 247, 255, 0.1);
            background: rgba(255, 255, 255, 0.08);
        }
        .blog-card h3 {
            margin-top: 0;
            font-family: 'Playfair Display', serif;
            color: #5FF7FF;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .blog-card p {
            color: #e0e0e0;
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }
        .blog-card a {
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            border-bottom: 2px solid #5FF7FF;
            padding-bottom: 2px;
        }
        .blog-card a:hover {
            color: #5FF7FF;
        }
        .page-header {
            text-align: center;
            padding: 8rem 2rem 4rem;
            background: linear-gradient(to bottom, #000, #111);
        }
        .page-header h1 {
            font-size: 3rem;
            color: #fff;
            margin-bottom: 1rem;
        }
        .page-header p {
            color: #aaa;
            max-width: 600px;
            margin: 0 auto;
            font-size: 1.2rem;
        }
    </style>
</head>
<body style="background-color: #000; color: #fff;">

    <!-- Header (Navigation) -->
    <header class="island-header" id="mainHeader">
        <div class="island-logo">
            <img src="static/Design.jpeg" alt="DeveloperBee Logo"> DeveloperBee
        </div>
        <button class="hamburger" id="navToggle" aria-label="Menu" tabindex="0">
            <span></span><span></span><span></span>
        </button>
        <ul class="island-nav" id="headerNav">
            <li><a href="index.html">Home</a></li>
            <li tabindex="0">
                <a href="services.html">Services</a>
                <div class="services-dropdown">
                    <a href="services.html#web-app-development">Web & App Development</a>
                    <a href="services.html#ui-ux-design">UI/UX Design</a>
                    <a href="services.html#seo-site-optimization">SEO & Optimization</a>
                    <a href="services.html#ml-automation">ML & Automation</a>
                    <a href="services.html#business-analysis">Business Analysis</a>
                    <a href="services.html#product-packaging">Product Packaging</a>
                </div>
            </li>
            <li><a href="portfolio.html">Portfolio</a></li>
            <li><a href="blog.html" class="active">Blog</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="pricing.html">Pricing</a></li>
        </ul>
        <div class="island-action">
            <a href="contact.html" class="nav-contact-btn">Contact Us</a>
        </div>
    </header>

    <div class="page-header">
        <h1>Our Latest Insights</h1>
        <p>Expert advice on software development, digital marketing, and business growth.</p>
    </div>

    <div class="blog-grid">
"""

    template_end = """
    </div>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="footer-content">
            <div class="footer-top">
                <div class="footer-brand">
                    <img src="static/Design.jpeg" alt="DeveloperBee Logo" class="footer-logo" loading="lazy">
                    <span class="footer-brand-name">DeveloperBee</span>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="portfolio.html">Portfolio</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="pricing.html">Pricing</a></li>
                        <li><a href="blog.html">Blog</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Get in Touch</h4>
                    <p>Email: <a href="mailto:developerbee.off@gmail.com">info@developerbee.com</a></p>
                    <p>Phone: <a href="tel:+917021975373">+91 7021975373</a></p>
                    <p>Location: Remote / Global</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="footer-copyright">&copy; 2025 DeveloperBee. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="static/header.js"></script>
    <script src="static/script.js"></script>
    <a href="https://wa.me/917021975373?text=Hi%20DeveloperBee,%20I%20found%20you%20via%20your%20blog!" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" />
    </a>
</body>
</html>
"""

    cards = ""
    for filename in blog_files:
        filepath = os.path.join(blog_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Extract Title
            title_tag = soup.find('title')
            title = title_tag.get_text().replace(" | DeveloperBee", "").strip() if title_tag else filename.replace("-", " ").title()

            # Extract Description
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            if desc_tag:
                description = desc_tag['content']
            else:
                # Fallback to first paragraph
                p_tag = soup.find('p')
                description = p_tag.get_text()[:150] + "..." if p_tag else "Read more about this topic."

            # Create Card HTML
            cards += f"""
        <article class="blog-card">
            <h3>{title}</h3>
            <p>{description}</p>
            <a href="blogs/{filename}">Read Article &rarr;</a>
        </article>
"""

    full_html = template_start + cards + template_end

    with open("blog.html", "w", encoding='utf-8') as f:
        f.write(full_html)
    print("Created blog.html successfully.")

if __name__ == "__main__":
    create_blog_index()
