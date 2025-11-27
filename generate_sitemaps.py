import os
import datetime
from pathlib import Path

BASE_URL = "https://developerbee.digital"
WWW_URL = "https://www.developerbee.digital"

DIRECTORIES = {
    "blogs": "sitemap-blogs.xml",
    "projects": "sitemap-projects.xml",
    "services": "sitemap-services.xml",
    "geo": "sitemap-geo.xml",
    ".": "sitemap-main.xml"  # Root directory
}

# Files to exclude from root sitemap
EXCLUDE_ROOT = {
    "google", "yandex", "bing", "sitemap", "robots", "404",
    "google0c7e2.html", "google_verification", "dashboard", "admin"
}

def get_last_mod_date(filepath):
    timestamp = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def generate_sitemap_content(files, priority="0.8", changefreq="monthly"):
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for file_path in files:
        # Convert file path to URL path
        if file_path.startswith("./"):
            url_path = file_path[2:]
        else:
            url_path = file_path

        if url_path == "index.html":
            url_path = "" # Root URL
        elif url_path.endswith("index.html"):
            url_path = url_path[:-10] # Remove index.html from subdirectories if any (though we process files)

        # Standard URL
        loc = f"{BASE_URL}/{url_path}"
        lastmod = get_last_mod_date(file_path)

        xml_content += '  <url>\n'
        xml_content += f'    <loc>{loc}</loc>\n'
        xml_content += f'    <lastmod>{lastmod}</lastmod>\n'
        xml_content += f'    <changefreq>{changefreq}</changefreq>\n'
        xml_content += f'    <priority>{priority}</priority>\n'
        xml_content += '  </url>\n'

        # WWW URL
        loc_www = f"{WWW_URL}/{url_path}"
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{loc_www}</loc>\n'
        xml_content += f'    <lastmod>{lastmod}</lastmod>\n'
        xml_content += f'    <changefreq>{changefreq}</changefreq>\n'
        xml_content += f'    <priority>{priority}</priority>\n'
        xml_content += '  </url>\n'

    xml_content += '</urlset>'
    return xml_content

def main():
    sitemap_index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for directory, sitemap_name in DIRECTORIES.items():
        files_to_include = []
        if directory == ".":
            # Scan root directory for .html files
            for file in os.listdir(directory):
                if file.endswith(".html"):
                    if any(ex in file for ex in EXCLUDE_ROOT):
                        continue
                    files_to_include.append(file)
        else:
            # Scan subdirectory
            if os.path.exists(directory):
                for file in os.listdir(directory):
                    if file.endswith(".html"):
                        files_to_include.append(os.path.join(directory, file))

        if files_to_include:
            # Sort files for consistency
            files_to_include.sort()

            # Determine priority based on directory
            priority = "0.8"
            if directory == ".":
                priority = "1.0"
            elif directory == "services":
                priority = "0.9"
            elif directory == "projects":
                priority = "0.9"
            elif directory == "blogs":
                priority = "0.7"

            content = generate_sitemap_content(files_to_include, priority)
            with open(sitemap_name, "w") as f:
                f.write(content)
            print(f"Created {sitemap_name} with {len(files_to_include)} URLs (x2 for www)")

            # Add to Sitemap Index
            lastmod = datetime.datetime.now().strftime('%Y-%m-%d')
            sitemap_index_content += '  <sitemap>\n'
            sitemap_index_content += f'    <loc>{BASE_URL}/{sitemap_name}</loc>\n'
            sitemap_index_content += f'    <lastmod>{lastmod}</lastmod>\n'
            sitemap_index_content += '  </sitemap>\n'
            # Also add www version to sitemap index? Usually not needed if the sitemap file is the same resource.
            # But the user might want it. However, sitemap index points to the location of the sitemap file.
            # The file is hosted at one place.
            # I will just add the base URL version.

    sitemap_index_content += '</sitemapindex>'

    with open("sitemap.xml", "w") as f:
        f.write(sitemap_index_content)
    print("Created sitemap.xml (Index)")

if __name__ == "__main__":
    main()
