import os

geo_dir = 'geo'

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix static assets
    content = content.replace('href="static/', 'href="../static/')
    content = content.replace('src="static/', 'src="../static/')

    # Fix main navigation links
    links_to_fix = [
        'index.html', 'services.html', 'portfolio.html',
        'about.html', 'contact.html', 'pricing.html'
    ]

    for link in links_to_fix:
        # Avoid double fixing if run multiple times or if some are already fixed
        # We look for href="link" and replace with href="../link"
        # We need to be careful not to replace href="../link" with href="../../link"
        # So we use a negative lookbehind pattern approach or just simple string replacement if we are sure of the state.
        # Since the files are currently broken (verified geo/usa.html), I will assume they are "static/..." or "index.html".

        # Simple replacement for exact matches
        content = content.replace(f'href="{link}"', f'href="../{link}"')

    # Fix subdirectory links in footer or body
    content = content.replace('href="services/', 'href="../services/')
    content = content.replace('href="blogs/', 'href="../blogs/')

    # Add header.js if missing
    if 'header.js' not in content:
        content = content.replace('</head>', '<script src="../static/header.js" defer></script>\n</head>')

    # Write back
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Fixed {filepath}")

for filename in os.listdir(geo_dir):
    if filename.endswith('.html'):
        fix_file(os.path.join(geo_dir, filename))
