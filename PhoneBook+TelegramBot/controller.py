import modul
import txt
import csv
import view
import UI

def choice_action (value):
    if   value == 1:
        UI.input_data()
    elif value == 2:
        UI.input_tel()
    elif value == 3:
        UI.input_tel_chanche()
    elif value == 4:
        UI.input_tel_del()
    elif value == 5:
        txt.export()
    elif value == 6:
        csv.export()
    elif value == 7:
        txt.import_txt()
    elif value == 8:
        csv.import_csv()
    elif value == 0:
        exit()



