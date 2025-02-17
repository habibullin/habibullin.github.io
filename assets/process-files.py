import os
import re

words_to_replace = ['и', 'в', 'на', 'с', 'по', 'к', 'из', 'для', 'от', 'а', 'но']

def replace_non_breaking_spaces(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for word in words_to_replace:
        content = re.sub(r'(\s)(' + re.escape(word) + r')', r'\1&nbsp;\2', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md') or file.endswith('.html'):
            replace_non_breaking_spaces(os.path.join(root, file))
