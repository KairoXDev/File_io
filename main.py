from tkinter import *       # Импортируем все классы и функции из модуля tkinter
from tkinter import filedialog as fd      # Импортируем модуль для работы с диалогами файлов
from tkinter import ttk     # Импортируем ttk, чтобы использовать более современные виджеты
from tkinter import messagebox as mb     # Импортируем messagebox для отображения сообщений
import requests     # Импортируем библиотеку requests для выполнения HTTP-запросов
from ttkthemes import ThemedStyle  # Импортируем ThemedStyle из ttkthemes
import pyperclip    # Импортируем библиотеку pyperclip для работы с буфером обмена
import json     # Импортируем модуль для работы с JSON-файлами
import os       # Импортируем модуль для работы с файловой системой


history_file = "upload_history.json"    # Имя файла, в котором будет храниться история загрузок


def save_history(file_path, link):
    history = []    # Создаем пустой список для хранения истории загрузок
    if os.path.exists(history_file):    # Проверяем, существует ли файл истории
        with open(history_file, "r") as f:      # Если файл существует, открываем его для чтения
            history = json.load(f)       # Загружаем содержимое файла в список
    history.append({"file_path": os.path.basename(file_path), "download_link": link})   # Добавляем новую запись в список истории
    with open(history_file, "w") as f:  # Открываем файл истории для записи
        json.dump(history, f, indent=4)     # Сохраняем обновленный список в файл в формате JSON


def upload():
    try:
        filepath = fd.askopenfilename()     # Открываем диалоговое окно для выбора файла и сохраняем путь к выбранному файлу
        if filepath:       # Проверяем, что файл был выбран
            with open(filepath, "rb") as f:
                files = {"file": f}      # Открываем файл для чтения в бинарном режиме и готовим его для отправки
                response = requests.post("http://file.io", files=files)     # Отправляем файл на сервер с помощью POST-запроса
                response.raise_for_status()     # Проверяем, был ли запрос успешным
                link = response.json()["link"]      # Получаем ссылку на загруженный файл из ответа сервера
                entry.delete(0, END)        # Очищаем текстовое поле перед вставкой новой ссылки
                entry.insert(0, link)       # Вставляем полученную ссылку в текстовое поле (в начало строки)
                pyperclip.copy(link)    # Копируем ссылку в буфер обмена
                save_history(filepath, link)    # Вызов функции для сохранения истории загрузки
                mb.showinfo("Ссылка скопирована", f"Ссылка ' {link} ' успешно скопирована в буфер обмена.")     # Показываем сообщение об успешном копировании ссылки в буфер обмена
    except Exception as e:      # Показываем сообщение об ошибке, если что-то пошло не так
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


window = Tk()       # Создаем основное окно приложения
window.title("Сохранение файлов в облаке")
window.geometry("350x80")

# Применяем стиль (тему) из ttkthemes
style = ThemedStyle(window)
style.set_theme('radiance')  # Можно выбрать любую доступную тему (arc, breeze, black, clearlooks, elegance, keramik, plastik, radiance, scidblue, scidgreen, scidpurple, scidred, scidyellow, tcl, winnative, xpnative)


button = ttk.Button(text="Загрузить файл", command=upload)    # Создаем кнопку с текстом
button.pack()


entry = ttk.Entry()     # Создаем текстовое поле для ввода данных
entry.pack()


window.mainloop()