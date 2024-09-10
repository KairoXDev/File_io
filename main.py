from tkinter import *       # Импортируем все классы и функции из модуля tkinter
from tkinter import filedialog as fd      # Импортируем модуль для работы с диалогами файлов
from tkinter import ttk     # Импортируем ttk, чтобы использовать более современные виджеты
import requests     # Импортируем библиотеку requests для выполнения HTTP-запросов


window = Tk()       # Создаем основное окно приложения
window.title("")
window.geometry("400x200")

button = ttk.Button(text="", command=upload)    # Создаем кнопку с текстом
button.pack

entry = ttk.Entry()     # Создаем текстовое поле для ввода данных
entry.pack

window.mainloop()