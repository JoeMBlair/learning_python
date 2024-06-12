#! python3
# bulletpoint_adder.py - Adds bullet points to start of each line in clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f"* {lines[i]}"

text = '\n'.join(lines)
pyperclip.copy(text)