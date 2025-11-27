import os

blogs_dir = 'blogs'

def fix_blog_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Add style.css if missing
    if 'href="../static/style.css"' not in content:
        # Insert before mobile-optimization.css or before </head>
        if 'href="../static/mobile-optimization.css"' in content:
             content = content.replace('<link rel="stylesheet" href="../static/mobile-optimization.css">', '<link rel="stylesheet" href="../static/style.css">\n    <link rel="stylesheet" href="../static/mobile-optimization.css">')
        else:
             content = content.replace('</head>', '<link rel="stylesheet" href="../static/style.css">\n</head>')

    # Ensure header.js is present (it was present in the example checked, but let's be safe)
    if 'header.js' not in content:
        content = content.replace('</head>', '<script src="../static/header.js" defer></script>\n</head>')

    # Check for CTA at the end. The example had one.

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Fixed {filepath}")

for filename in os.listdir(blogs_dir):
    if filename.endswith('.html'):
        fix_blog_file(os.path.join(blogs_dir, filename))
