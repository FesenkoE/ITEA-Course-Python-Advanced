"""3. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

Решение покрыть тестами (опционально)."""

translate_lib = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Один'
}

with open("text.txt", 'r') as f1, open("file_new.txt", 'a') as f2:
    for new_line in f1:
        line_list = new_line.split(' - ')
        translate_str = translate_lib[line_list[0]] + ' - ' + line_list[1]
        f2.write(translate_str)
