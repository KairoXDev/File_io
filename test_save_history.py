import json
import os


history_file = "test_save_history.json"      # Имя файла, в котором будет храниться история загрузок

# Копируем функцию из главного файла
def save_history(file_path, link):
    history = []    # Создаем пустой список для хранения истории загрузок
    if os.path.exists(history_file):    # Проверяем, существует ли файл истории
        with open(history_file, "r") as f:      # Если файл существует, открываем его для чтения
            history = json.load(f)       # Загружаем содержимое файла в список
    history.append({"file_path": os.path.basename(file_path), "download_link": link})   # Добавляем новую запись в список истории
    with open(history_file, "w") as f:  # Открываем файл истории для записи
        json.dump(history, f, indent=4)     # Сохраняем обновленный список в файл в формате JSON


def test_save_history():
    test_file_path = "test_file.txt"         # Путь к тестовому файлу
    test_download_link = "http://file.io/fdgdfgd"       # Ссылка на тестовую загрузку

    save_history(test_file_path, test_download_link)        # Вызываем функцию для сохранения истории с тестовыми данными

    with open("test_save_history.json", "r") as f:      # Открываем файл истории для проверки
        history = json.load(f)      # Загружаем содержимое файла в список
        assert len(history) == 1        # Проверяем, что в истории есть ровно одна запись
        assert history[0]["file_path"] == test_file_path      # Проверяем, что путь к файлу совпадает с тестовым значением
        assert history[0]["download_link"] == test_download_link    # Проверяем, что ссылка на загрузку совпадает с тестовым значением

    os.remove("test_save_history.json")      # Удаляем файл истории после теста

test_save_history()     # Запускаем тест