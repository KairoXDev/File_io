from tkinter import *       # Импортируем все классы и функции из модуля tkinter
from tkinter import filedialog as fd      # Импортируем модуль для работы с диалогами файлов
from tkinter import ttk     # Импортируем ttk, чтобы использовать более современные виджеты
from tkinter import messagebox as mb     # Импортируем messagebox для отображения сообщений
import requests     # Импортируем библиотеку requests для выполнения HTTP-запросов
from ttkthemes import ThemedStyle  # Импортируем ThemedStyle из ttkthemes


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