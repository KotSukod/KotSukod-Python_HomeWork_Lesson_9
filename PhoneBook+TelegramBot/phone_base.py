def elem(data):
    text = []
    while data != '':
        if data == "\n":
            data = ''
            continue
        space_pos = data.index(' ')
        text.append(data[:space_pos].lower())
        data = data[space_pos + 1:]
    return text

def base_open():
    data = open('Base.txt', 'r')
    phone_data = list()
    for line in data:
        help = ''
        ls = list()
        for i in line:
            if i == ";":
                help += ' '
            else:
                help += i
        ls.append(help)
        phone_data.append(ls[0])
    return phone_data
    data.close()
    exit()

def great (name, surname, tel):
    data = open('Base.txt', 'a')
    data.writelines("{};{};{};\n".format(name, surname, tel))
    data.close()

def base_save(name, surname, tel,index):
    help = base_open()
    help[index] = str(name + " " + surname + " " +tel + " \n")
    data = open('Base.txt', 'w')
    for elements in help:
        text = elem(elements)
        data.writelines("{};{};{};\n".format(text[0], text[1], text[2]))
    data.close()

def search_for_duplicates(tel):
    help = base_open()
    for elements in help:
        text = elem(elements)
        i = 0
        while i < len(text):
            if text[i] == tel:
                return 1
            i += 1
    return 0

def search_number(tel):
    help = base_open()
    for elements in help:
        index = help.index(elements)
        text = elem(elements)
        if text[2] == tel:
            return text, index
    return None, 0


def base_delet(index):
    help = base_open()
    help.pop(index)
    data = open('Base.txt', 'w')
    for elements in help:
        text = elem(elements)
        data.writelines("{};{};{};\n".format(text[0], text[1], text[2]))
    data.close()