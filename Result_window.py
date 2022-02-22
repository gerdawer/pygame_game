# Окно, в котором отражается результат игры

from pygame import *


def result_window(result):
    # Объявление основных параметров окна
    init()
    display.set_caption('Your result')
    window = display.set_mode((480, 360))

    # Загрузка изображений
    win = image.load('images/win_image.jpg')
    win = transform.scale(win, (480, 360))
    lost = image.load('images/lose_image.jpg')
    lost = transform.scale(lost, (480, 360))

    # Основной цикл
    while True:
        # Отражение результата
        if result:
            window.blit(win, (0, 0))
        if not result:
            window.blit(lost, (0, 0))

        # Обновление экрана
        display.update()

        # Обработчик событий
        for e in event.get():
            # Закрытие окна
            if e.type == QUIT:
                quit()

            # При нажатии клавиши "Enter" игрок возвращается к выбору уровня
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    return True
