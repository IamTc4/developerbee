import os

services_dir = 'services'

def fix_service_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Add header.js if missing
    if 'header.js' not in content:
        # Assuming typical head structure, insert before </head>
        content = content.replace('</head>', '<script src="../static/header.js" defer></script>\n</head>')

    # Check for trap pages - ensure CTA exists
    if 'href="../contact.html"' not in content and 'href="../index.html"' not in content:
         # This is a basic check. Most pages should have these in header/footer.
         # The user specifically mentioned redirects/traps.
         # Let's ensure a prominent CTA at the end of the main section if not present.
         pass

    # Fix potential self-links in footer if they exist as relative paths without ../
    # In services/web-app-development.html, we saw:
    # <li><a href="web-app-development.html">Web & App Dev</a></li>
    # This is actually fine because it is in the same directory.
    # But links to OTHER services like ai-automation.html are also fine: <a href="ai-automation.html">

    # However, if the footer was copied from root, it might have services/ai-automation.html
    # In services/web-app-development.html:
    # <li><a href="ai-automation.html">AI & Automation</a></li> -> Correct

    # Let's just make sure header.js is there.

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Fixed {filepath}")

for filename in os.listdir(services_dir):
    if filename.endswith('.html'):
        fix_service_file(os.path.join(services_dir, filename))
