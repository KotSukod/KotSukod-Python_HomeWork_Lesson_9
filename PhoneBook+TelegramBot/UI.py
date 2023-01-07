import tkinter as tk
from tkinter import *
import tkinter.messagebox as ms
from tkinter import ttk
import controller
import modul
def main_menu():
    win = tk.Tk()
    win.title("Телефонный справочник v 1.1")
    win.geometry("500x600")
    photo = tk.PhotoImage(file='book_img.png')
    win.iconphoto(False, photo)
    win.config(bg='grey')
    title = tk.Label(win, text='Главное меню', font=('Arial', 20))
    title.pack()
    title_1 = tk.Label(win, text='Выбирите действие', width=20).place(x=0, y=40)
    button_1 = tk.Button(win, text="Записать номер",command=lambda: controller.choice_action(1),width=20).place(x=0, y=65)
    button_2 = tk.Button(win, text="Найти номер",command=lambda: controller.choice_action(2), width=20).place(x=0, y=91)
    button_3 = tk.Button(win, text="Редактировать номер",command=lambda: controller.choice_action(3), width=20).place(x=0, y=117)
    button_4 = tk.Button(win, text="Удалить номер",command=lambda: controller.choice_action(4),width=20).place(x=0, y=143)
    button_5 = tk.Button(win, text="Экспорт в txt", command=lambda: controller.choice_action(5), width=20).place(x=0,y=169)
    button_6 = tk.Button(win, text="Экспорт в csv",command=lambda: controller.choice_action(6), width=20).place(x=0, y=195)
    button_7 = tk.Button(win, text="Импорт из txt",command=lambda: controller.choice_action(7), width=20).place(x=0, y=221)
    button_8 = tk.Button(win, text="Импорт из csv",command=lambda: controller.choice_action(8), width=20).place(x=0, y=247)
    button_0 = tk.Button(win, text="Выход",command=lambda: controller.choice_action(0), width=20).place(x=0, y=273)
    #button_test = tk.Button(win, text="TEST",command= lambda: input_tel1(), width=20).place(x=0, y=299)
    win.mainloop()

def input_data():
    def check_pass():
        if entry_name.get() and entry_surname.get() and entry_tel.get() :
            modul.great_contact(entry_name.get(),entry_surname.get(),entry_tel.get())
            label_welcome.configure(text="ОК")
        else:
            label_welcome.configure(text="Заполните все поля")

    root = tk.Tk()
    label_name = tk.Label(root, text="Имя")
    label_name.pack()
    entry_name = tk.Entry(root, width=10)
    entry_name.pack()
    label_surname = tk.Label(root, text="Фамилия")
    label_surname.pack()
    entry_surname = tk.Entry(root, width=10)
    entry_surname.pack()
    label_tel = tk.Label(root, text="Телефон")
    label_tel.pack()
    entry_tel = tk.Entry(root, width=10)
    entry_tel.pack()
    button = tk.Button(root, text="Enter", command=check_pass,)
    button.pack()
    label_welcome = tk.Label(root)
    label_welcome.pack()
    root.mainloop()

def input_tel():
    def check_pass():
        if entry_tel.get() :
            modul.search(entry_tel.get())
            label_welcome.configure(text="ОК")
        else:
            label_welcome.configure(text="Заполните все поля")

    root = tk.Tk()
    label_tel = tk.Label(root, text="Телефон")
    label_tel.pack()
    entry_tel = tk.Entry(root, width=10)
    entry_tel.pack()
    button = tk.Button(root, text="Enter", command=check_pass,)
    button.pack()
    label_welcome = tk.Label(root)
    label_welcome.pack()
    root.mainloop()

def input_tel_chanche():
    def check_pass():
        if entry_tel.get() :
            modul.change_data(entry_tel.get())
            label_welcome.configure(text="ОК")
        else:
            label_welcome.configure(text="Заполните все поля")

    root = tk.Tk()
    label_tel = tk.Label(root, text="Телефон")
    label_tel.pack()
    entry_tel = tk.Entry(root, width=10)
    entry_tel.pack()
    button = tk.Button(root, text="Enter", command=check_pass,)
    button.pack()
    label_welcome = tk.Label(root)
    label_welcome.pack()
    root.mainloop()

def input_tel_del():
    def check_pass():
        if entry_tel.get() :
            modul.delet(entry_tel.get())
            label_welcome.configure(text="ОК")
        else:
            label_welcome.configure(text="Заполните все поля")

    root = tk.Tk()
    label_tel = tk.Label(root, text="Телефон")
    label_tel.pack()
    entry_tel = tk.Entry(root, width=10)
    entry_tel.pack()
    button = tk.Button(root, text="Enter", command=check_pass,)
    button.pack()
    label_welcome = tk.Label(root)
    label_welcome.pack()
    root.mainloop()

def message (text):
    ms.showinfo(title = 'Информация',message= text)


def canche_data():
    def check_pass():
        if entry_name.get():
            modul.change_data1(entry_name.get(),1)
        elif entry_surname.get():
            modul.change_data1(entry_surname.get(),2)
        elif entry_tel.get():
            modul.change_data1(entry_tel.get(),3)
        else:
            label_welcome.configure(text="Заполните все поля")

    root = tk.Tk()
    label_name = tk.Label(root, text="Имя")
    label_name.pack()
    entry_name = tk.Entry(root, width=10)
    entry_name.pack()
    label_surname = tk.Label(root, text="Фамилия")
    label_surname.pack()
    entry_surname = tk.Entry(root, width=10)
    entry_surname.pack()
    label_tel = tk.Label(root, text="Телефон")
    label_tel.pack()
    entry_tel = tk.Entry(root, width=10)
    entry_tel.pack()
    button = tk.Button(root, text="Enter", command=check_pass,)
    button.pack()
    label_welcome = tk.Label(root)
    label_welcome.pack()
    root.mainloop()








