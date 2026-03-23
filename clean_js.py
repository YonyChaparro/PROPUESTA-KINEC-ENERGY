with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_str = "// Menú hamburguesa móvil"
end_str = "// ── Animaciones de entrada al hacer scroll ──"

start_idx = text.find(start_str)
end_idx = text.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + "\n    " + text[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced!")
else:
    print("Not found!")
