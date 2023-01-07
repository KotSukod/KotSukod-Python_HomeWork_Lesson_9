import phone_base
import UI
def export():
    base = phone_base.base_open()
    with open('phone_book_export.csv', 'w') as file:
        file.write('{};{};{};{}\n'.format("Номер","Имя","Фамилия","Телефон"))
        index = 1
        for elements in base:
            text = phone_base.elem(elements)
            file.write('{};{};{};{}\n'.format(index,text[0],text[1],text[2]))
            index += 1
    UI.message("Выгрузка завершенна")

def import_csv():
    data = open("phone_book_import.csv").read()
    ls = list()
    while data != '':
        space_pos = data.index('\n')
        ls.append(data[:space_pos])
        data = data[space_pos + 1:]
    ls.remove(ls[0])
    ls1 = []
    for i in ls:
        help = str(i + ';')
        count = ''
        for i in help:
            if i == ';':
                ls1.append(count)
                count = ''
            else:
                count += i
    i = 2
    while i < len(ls1):
        proverka = phone_base.search_for_duplicates(ls1[i])
        if proverka == 1:
            i += 3
        else:
            phone_base.great(ls1[i - 2], ls1[i - 1], ls1[i])
            i += 3
    UI.message("Загрузка завершенна")