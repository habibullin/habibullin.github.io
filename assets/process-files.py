import os
import re

def replace_spaces_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Список предлогов и союзов
    words_to_replace = ['и', 'в', 'на', 'с', 'по', 'к', 'из', 'для', 'от', 'а', 'но']
    pattern = r'\b(' + '|'.join(words_to_replace) + r')\s+'
    
    # Заменяем пробелы на неразрывные
    new_content = re.sub(pattern, lambda m: m.group(0).replace(' ', '\u00A0'), content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Примените функцию ко всем нужным файлам
for root, dirs, files in os.walk('es'):
    for file in files:
        if file.endswith('.html') or file.endswith('.md'):  # Укажите нужные расширения
            replace_spaces_in_file(os.path.join(root, file))

