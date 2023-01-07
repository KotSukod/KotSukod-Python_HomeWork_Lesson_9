import phone_base
import UI
def export():
    base = phone_base.base_open()
    with open('phone_book_export.txt', 'w') as file:
        for elements in base:
            text = phone_base.elem(elements)
            file.write('Имя: {}\n'.format(text[0]))
            file.write('Фамилия: {}\n'.format(text[1]))
            file.write('Телефон: {}\n'.format(text[2]))
            file.write('\n')
    UI.message("Выгрузка завершенна")

def import_txt():
    data = open("phone_book_import.txt").read()
    ls = list()
    while data != '':
        space_pos = data.index('\n')
        ls.append(data[:space_pos])
        data = data[space_pos + 1:]
    ls1 = []
    for i in ls:
        help = str(i)
        if help == '':
            continue
        pos = help.index(":")
        ls1.append((help[pos + 2:]))
    i = 2
    while i < len(ls1):
        proverka = phone_base.search_for_duplicates(ls1[i])
        if proverka == 1:
            i += 3
        else:
            phone_base.great(ls1[i -2],ls1[i -1],ls1[i])
            i += 3

    UI.message("Загрузка завершенна")