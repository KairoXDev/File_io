from tkinter import *       # Импортируем все классы и функции из модуля tkinter
from tkinter import filedialog as fd      # Импортируем модуль для работы с диалогами файлов
from tkinter import ttk     # Импортируем ttk, чтобы использовать более современные виджеты
import requests     # Импортируем библиотеку requests для выполнения HTTP-запросов


def upload():
    filepath = fd.askopenfilename()     # Открываем диалоговое окно для выбора файла и сохраняем путь к выбранному файлу
    if filepath:       # Проверяем, что файл был выбран
        files = {"file": open(filepath, "rb")}      # Открываем файл для чтения в бинарном режиме и готовим его для отправки
        response = requests.post("http://file.io", files=files)     # Отправляем файл на сервер с помощью POST-запроса
        if response.status_code == 200:     # Если сервер успешно обработал запрос
            link = response.json()["link"]      # Получаем ссылку на загруженный файл из ответа сервера
            entry.insert(0, link)       # Вставляем полученную ссылку в текстовое поле (в начало строки)

window = Tk()       # Создаем основное окно приложения
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)    # Создаем кнопку с текстом
button.pack()

entry = ttk.Entry()     # Создаем текстовое поле для ввода данных
entry.pack()

window.mainloop()