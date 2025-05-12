import os
import re

WORDS_TO_REPLACE = ['и', 'в', 'на', 'с', 'по', 'к', 'из', 'для', 'от', 'а', 'о', 'но']
PATTERN = r'\b(' + '|'.join(WORDS_TO_REPLACE) + r')\s+'

def replace_spaces_in_file(file_path):
    if not os.path.exists(file_path):
        return  # Если файл не найден, просто выходим из функции

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if re.search(PATTERN, content):
        # Заменяем пробелы на неразрывные
        new_content = re.sub(PATTERN, lambda m: m.group(1) + '\u00A0', content)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

for root, dirs, files in os.walk('es'):
    for file in files:
        if file.endswith('.html') or file.endswith('.md'):
            replace_spaces_in_file(os.path.join(root, file))
