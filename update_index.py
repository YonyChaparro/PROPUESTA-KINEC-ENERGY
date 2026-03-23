import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace nav
nav_pattern = re.compile(r'\s*<nav\b.*?</nav>', re.DOTALL)
text = nav_pattern.sub('\n  <div id="nav-component"></div>', text, 1)

# 2. Replace footer
footer_pattern = re.compile(r'\s*<footer\b.*?</footer>', re.DOTALL)
text = footer_pattern.sub('\n  <div id="footer-component"></div>', text, 1)

# 3. Replace fixed buttons
buttons_pattern = re.compile(r'\s*<!-- Contenedor de botones flotantes -->\s*<div class="fixed bottom-6 right-6 z-50.*?</div>\n', re.DOTALL)
text = buttons_pattern.sub('\n  <div id="floating-buttons-component"></div>\n', text, 1)

# 4. Remove duplicate JS inside index.html for hamburguer and scroll top
start_marker = "// Menú hamburguesa móvil"
end_marker = "// ── Animaciones de entrada al hacer scroll ──"

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

if idx_start != -1 and idx_end != -1:
    text = text[:idx_start] + text[idx_end:]

# 5. Inject components.js at the end of the body
if '<script src="/js/components.js"></script>' not in text:
    text = text.replace('</body>', '  <script src="/js/components.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
