def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    try:
        for i, line in enumerate(strings, start=1):
            position = file.tell()
            file.write(line + '\n')
            strings_positions[(i, position)] = line

    finally:
        file.close()

    return strings_positions

info = ['Text for tell.', 'Используйте кодировку utf-8', 'Because there are 2 languages', 'Спасибо!']

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)