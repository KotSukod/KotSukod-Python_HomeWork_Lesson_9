def head ():
    print(" ")
    print("Выбирите действие:")
    print("1 - Записать номер")
    print("2 - Найти номер")
    print("3 - редактировать номер")
    print("4 - Удалить номер ")
    print("5 - Экспорт в txt")
    print("6 - Экспорт в cvs")
    print("7 - Импорт из txt")
    print("8 - Импорт из cvs")
    print("0 - Выход")

def get_value ():
   return int(input("=> "))