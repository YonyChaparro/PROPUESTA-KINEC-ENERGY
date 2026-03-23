import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace NAV
nav_pattern = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL)
html = nav_pattern.sub('<div id="nav-component"></div>', html)

# Replace FOOTER
footer_pattern = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)
html = footer_pattern.sub('<div id="footer-component"></div>', html)

# Replace floating buttons
float_pattern = re.compile(r'<div class="fixed bottom-6 right-6.*?</div>(?=\s*<script)', re.DOTALL)
html = float_pattern.sub('<div id="floating-buttons-component"></div>\n', html)

# Inject js/components.js right before </body> or inside <head>! Or just before the closing body script
head_pattern = re.compile(r'</head>')
html = head_pattern.sub('  <script src="/js/components.js" defer></script>\n</head>', html)

# Remove the JS inside index.html that collides.
# Wait, let's just write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
