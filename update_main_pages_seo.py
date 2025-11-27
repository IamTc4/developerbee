import os
from bs4 import BeautifulSoup

PAGES_SEO = {
    "index.html": {
        "title": "Top Web Development & Digital Agency India | DeveloperBee",
        "desc": "Partner with DeveloperBee for premium web development, app creation, and digital growth strategies. Expert IT outsourcing from India.",
        "h1": "Premier Digital Transformation Agency",
        "keywords": "web development India, IT outsourcing, app developers, digital agency"
    },
    "services.html": {
        "title": "Custom Software & App Development Services | DeveloperBee",
        "desc": "Comprehensive IT services: Web Design, Mobile Apps, SEO, Automation, and Cybersecurity. Tailored solutions for scaling businesses.",
        "h1": "Our Core Services",
        "keywords": "custom software, app development services, business automation, SEO services"
    },
    "about.html": {
        "title": "About DeveloperBee | Innovative Tech Solutions Team",
        "desc": "Learn about DeveloperBee's mission to empower businesses with cutting-edge technology, expert developers, and result-driven strategies.",
        "h1": "Innovating for Your Growth",
        "keywords": "about DeveloperBee, tech team India, software company mission"
    },
    "contact.html": {
        "title": "Contact DeveloperBee | Get a Free Consultation",
        "desc": "Ready to start your project? Contact DeveloperBee today for a free consultation and quote on web, app, and digital services.",
        "h1": "Let's Build Something Great",
        "keywords": "contact web developers, hire developers, project consultation"
    },
    "portfolio.html": {
        "title": "Our Work & Case Studies | DeveloperBee Portfolio",
        "desc": "Explore our successful projects in FinTech, Healthcare, E-commerce, and more. See how we deliver results for global clients.",
        "h1": "Our Portfolio of Success",
        "keywords": "software case studies, web development portfolio, app projects"
    },
    "blog.html": {
        "title": "Insights on Tech, AI & Business Growth | DeveloperBee Blog",
        "desc": "Read expert articles on web development trends, AI integration, SEO strategies, and business automation tips.",
        "h1": "Tech Insights & News",
        "keywords": "tech blog, web dev tips, business growth strategies, AI trends"
    },
    "pricing.html": {
        "title": "Affordable Web Development Pricing Packages | DeveloperBee",
        "desc": "Transparent pricing for web and app development. Flexible plans for startups and enterprises. Get high-quality code at competitive rates.",
        "h1": "Transparent Service Pricing",
        "keywords": "web development pricing India, app cost, affordable IT services"
    }
}

def update_page_seo(filename, seo_data):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # Update Title
    if soup.title:
        soup.title.string = seo_data["title"]
    else:
        new_title = soup.new_tag("title")
        new_title.string = seo_data["title"]
        if soup.head:
            soup.head.append(new_title)

    # Update Meta Description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        meta_desc["content"] = seo_data["desc"]
    else:
        new_meta = soup.new_tag("meta", attrs={"name": "description", "content": seo_data["desc"]})
        if soup.head:
            soup.head.append(new_meta)

    # Update Keywords
    meta_keys = soup.find("meta", attrs={"name": "keywords"})
    if meta_keys:
        meta_keys["content"] = seo_data["keywords"]
    else:
        new_meta = soup.new_tag("meta", attrs={"name": "keywords", "content": seo_data["keywords"]})
        if soup.head:
            soup.head.append(new_meta)

    # Update H1
    h1 = soup.find("h1")
    if h1:
        h1.string = seo_data["h1"]

    # Save
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))
    print(f"Updated SEO for {filename}")

if __name__ == "__main__":
    for filename, data in PAGES_SEO.items():
        update_page_seo(filename, data)
