from tkinter import *
from tkinter import messagebox
from random import choice
import time
import os
import sys

answers = ['Бесспорно', 'Предрешено', 'Никаких\nсомнений', 'Определённо\nда', 'Можешь быть\nуверен\nв этом',
           'Мне кажется \nда', 'Вероятнее\nвсего', 'Хорошие\nперспективы', 'Знаки говорят\nда', 'Да',
           'Даже\nне думай', 'Мой ответ\nнет', 'По моим данным\nнет', 'Перспективы\nне очень\nхорошие',
           'Весьма\nсомнительно', 'Пока неясно,\nпопробуй снова', 'Спроси\nпозже', 'Лучше\nне рассказывать',
           'Сейчас\nнельзя\nпредсказать', 'Сконцентрируйся\nи спроси опять']

def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работает для разработки и для скомпилированных приложений"""
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Если не скомпилировано, используем директорию скрипта
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

def choice_answer():        # функция для выбора ответа
    time.sleep(0.3)
    global ans_old
    ans_new = ans_old
    while ans_new == ans_old:   # чтобы один и тот же ответ не выпал два раза подряд
        ans_new = choice(answers)
    ans_old = ans_new
    canvas.itemconfig(answer, text=ans_old)

def on_restart():
    canvas.itemconfig(answer, text='Добро\nпожаловать!')

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()

def window_close(this_window):      # функция чтобы окно инфо не дублировалось
    global window_open
    window_open = False
    this_window.destroy()

def press_info():
    global window_open
    if window_open:
        return
    info_window = Toplevel(root)
    info_window.title('Инфо')
    info_window.geometry('350x350+770+320')
    info_window.resizable(0, 0)
    info_window.iconphoto(False, icon)
    info_window.focus()
    info_window.wm_attributes("-topmost", 1)
    info_window.protocol("WM_DELETE_WINDOW", lambda this_window=info_window: window_close(this_window))
    window_open = True

    canvas_1 = Canvas(info_window, width=350, height=350,
                      bg="#391558", highlightthickness=0)  # включаем canvas
    canvas_1.pack()

    canvas_1.create_text(175, 80, text="Автор:\nИлья Панкратов", font=("WiGuru 2", 20),
                         fill='white', justify=CENTER, anchor=CENTER)

    canvas_1.create_text(175, 160, text="ilya-pankratov@list.ru", font=("WiGuru 2", 15),
                         fill='white', justify=CENTER, anchor=CENTER)

    canvas_1.create_text(175, 280, text="Создано на Python\nс помощью модуля tkinter", font=("WiGuru 2", 15),
                         fill='white', justify=CENTER, anchor=CENTER)

root = Tk()
root.title('Магический шар')        # параметры окна
root.geometry('700x556+600+200')
root.resizable(0, 0)

# Проверяем существование файлов и выводим информацию для отладки
print("Текущая рабочая директория:", os.getcwd())
print("Директория скрипта:", os.path.dirname(os.path.abspath(__file__)))

# Загружаем иконку с правильным путем
icon_path = resource_path('img/logo.png')
print("Путь к иконке:", icon_path)
print("Файл существует:", os.path.exists(icon_path))

try:
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
except Exception as e:
    print(f"Ошибка загрузки иконки: {e}")
    # Создаем пустую иконку или используем заглушку
    icon = PhotoImage(width=1, height=1)

canvas = Canvas(root, width=700, height=556, highlightthickness=0)  # включаем canvas
canvas.pack()

# Загружаем фоновое изображение
try:
    img_obj1_path = resource_path("img/magic_ball.png")
    print("Путь к фону:", img_obj1_path)
    print("Файл фона существует:", os.path.exists(img_obj1_path))
    img_obj1 = PhotoImage(file=img_obj1_path)
    canvas.create_image(0, 0, anchor=NW, image=img_obj1)
except Exception as e:
    print(f"Ошибка загрузки фона: {e}")
    # Заливаем фон цветом, если изображение не загрузилось
    canvas.create_rectangle(0, 0, 700, 556, fill="#391558", outline="")

# Загружаем заголовок
try:
    img_obj2_path = resource_path("img/title.png")
    print("Путь к заголовку:", img_obj2_path)
    print("Файл заголовка существует:", os.path.exists(img_obj2_path))
    img_obj2 = PhotoImage(file=img_obj2_path)
    canvas.create_image(-38, 10, anchor=NW, image=img_obj2)
except Exception as e:
    print(f"Ошибка загрузки заголовка: {e}")
    # Создаем текстовый заголовок, если изображение не загрузилось
    canvas.create_text(100, 50, text="МАГИЧЕСКИЙ ШАР", 
                       font=("Arial", 30), fill="white", anchor=NW)

ans_old = 'Добро\nпожаловать!'                              # текст с ответом
answer = canvas.create_text(345, 300, text=ans_old,
                            font=("WiGuru 2", 20), fill='white',
                            justify=CENTER, anchor=CENTER)

b1 = Button(root, text='ЗАДАЙ ВОПРОС И НАЖМИ',              # главная кнопка
            font=("WiGuru 2", 15), command=choice_answer,
            bg='#9FEE00', bd=8)
b1.place(x=182, y=480, width=330, height=50)

# Загружаем кнопку перезапуска
try:
    our_button1_path = resource_path("img/button_restart.png")
    our_button1 = PhotoImage(file=our_button1_path)
    id_button1 = Button(root, image=our_button1, highlightthickness=0,
                        bg='#9FEE00', bd=4, command=on_restart)
    id_button1.place(x=15, y=505)
except Exception as e:
    print(f"Ошибка загрузки кнопки перезапуска: {e}")
    # Создаем текстовую кнопку как запасной вариант
    id_button1 = Button(root, text="Сброс", command=on_restart,
                        bg='#9FEE00', bd=4, font=("Arial", 10))
    id_button1.place(x=15, y=505, width=50, height=30)

# Загружаем кнопку выхода
try:
    our_button2_path = resource_path("img/button_exit.png")
    our_button2 = PhotoImage(file=our_button2_path)
    id_button2 = Button(root, image=our_button2, highlightthickness=0,
                        bg='#9FEE00', bd=4, command=on_closing)
    id_button2.place(x=645, y=505)
except Exception as e:
    print(f"Ошибка загрузки кнопки выхода: {e}")
    id_button2 = Button(root, text="Выход", command=on_closing,
                        bg='#9FEE00', bd=4, font=("Arial", 10))
    id_button2.place(x=645, y=505, width=50, height=30)

window_open = False

# Загружаем кнопку информации
try:
    our_button3_path = resource_path("img/button_info.png")
    our_button3 = PhotoImage(file=our_button3_path)
    id_button3 = Button(root, image=our_button3, highlightthickness=0,
                        bg='#9FEE00', bd=4, command=press_info)
    id_button3.place(x=15, y=450)
except Exception as e:
    print(f"Ошибка загрузки кнопки информации: {e}")
    id_button3 = Button(root, text="Инфо", command=press_info,
                        bg='#9FEE00', bd=4, font=("Arial", 10))
    id_button3.place(x=15, y=450, width=50, height=30)

root.mainloop()