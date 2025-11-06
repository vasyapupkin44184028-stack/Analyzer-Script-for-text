# Приложение: Анализатор текстовых файлов
# Разработано на Python 3
"""
Приложение анализирует текстовый файл и произвожит его статистику.
    
Args:
    filename (str): Путь к файлу для анализа
        
Returns:
    str: Строка с результатами анализа или сообщением об ошибке
"""

import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox

def text_analyzer(filename):
   
    try:
        # Чтение файла 
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Формирование заголовка результатов
        result = f"Файл: {filename}\n"
        result += "=" * 30 + "\n"
        
        # Поиск всех слов в тексте (только буквы, регистр не учитывается)
        words = re.findall(r'\b[а-яёa-z]+\b', text.lower())
        result += f"Количество слов: {len(words)}\n"
        
        # Разделение текста на предложения по знакам препинания
        sentences = re.split(r'[.!?…]+', text)
        # Удаление пустых строк и лишних пробелов
        sentences = [s.strip() for s in sentences if s.strip()]
        result += f"Количество предложений: {len(sentences)}\n"
        
        # Если в тексте есть слова, вычисляем дополнительную статистику
        if words:
            # Подсчет частоты каждого слова
            word_counts = Counter(words)
            # Поиск самого частого слова и количества его вхождений
            common_word, count = word_counts.most_common(1)[0]
            result += f"Самое частое слово: '{common_word}' (встречается {count} раз)\n"
            
            # Вычисление средней длины слова
            avg_length = sum(len(word) for word in words) / len(words)
            result += f"Средняя длина слова: {int(round(avg_length, 0))} символов\n"
            # Использует округление: число > 4.5 = 4, число =< 4.5 = 5
        
        return result
            
    except FileNotFoundError:
        return f"Ошибка: Файл '{filename}' не найден!"
    except UnicodeDecodeError:
        return "Ошибка: Не удается прочитать файл."
    except Exception as e:
        return f"Ошибка при обработке файла: {e}"

def select_and_analyze():
    # Открытие диалогового окна для выбора текстового файла
    filename = filedialog.askopenfilename(
        title="Выберите текстовый файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    
    # Если файл выбран
    if filename:
        result = text_analyzer(filename)
        # Показ результатов в диалоговом окне
        messagebox.showinfo("Результаты анализа", result)

# Создание и настройка главного окна приложения
root = tk.Tk()
root.title("Анализатор текста")  # Заголовок окна
root.geometry("300x150")         # Размер окна (ширина x высота)
root.resizable(False, False)     # Запрет изменения размера окна, можно заменить на (True, True) для снятия запретаpython analyzer.py

# Создание надписи в окне
label = tk.Label(
    root, 
    text="Анализатор текста", 
    font=("Arial", 14)
)
label.pack(pady=20)  # Размещение с отступом 20 пикселей сверху и снизу

# Создание кнопки для выбора файла
button = tk.Button(
    root, 
    text="Выберите файл",
    command=select_and_analyze,  # Функция, вызываемая при нажатии
    bg="lightblue",              
    font=("Arial", 12)           
)
button.pack(pady=10)  # Размещение с отступом 10 пикселей

# Запуск главного цикла обработки событий
# Программа работает до закрытия окна
root.mainloop()