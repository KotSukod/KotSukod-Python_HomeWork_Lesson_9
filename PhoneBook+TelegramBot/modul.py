import phone_base
import input
import view
import UI

global number
global index
def great_contact (name, surname,tel):

    proverka = phone_base.search_for_duplicates(tel)
    if proverka == 1:
        UI.message('Такой номер телеофна уже существует!!!')
    else:
        phone_base.great(name, surname, tel)
        UI.message("Запись создана")

def search(tel):
    number,index = phone_base.search_number(tel)
    if number == None:
        UI.message("Номер не найден")
    else:
        UI.message("{}-{}-{}".format(number[0],number[1],number[2]))

def change_data(tel):
    global number,index
    number_local, index_local = phone_base.search_number(tel)
    number = number_local
    index = index_local
    UI.canche_data()

def change_data1(data,num):
    global number,index
    if num == 1:
        number[0] = data
    if num == 2:
        number[1] = data
    if num == 3:
        number[2] = data
    phone_base.base_save(number[0],number[1],number[2],index)
    UI.message("Запись изменена")


def delet(tel):
    number,index = phone_base.search_number(tel)
    phone_base.base_delet(index)
    UI.message("Запись удаленна")


