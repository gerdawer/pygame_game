# Окно, в котором происходит выбор уровня
# Функция возвращает уровень сложности игры, который учитывается в функции game

from pygame import *


def levels_window():
    # Объявление основных параметров окна
    init()
    W = 480
    H = 360
    display.set_caption('Levels')
    window = display.set_mode((W, H))
    Play = True

    # Загрузка фона и кнопок
    texture = image.load('images/texture.jpg')
    texture = transform.scale(texture, (W, H))

    easy_button = image.load('images/easy_button.png')
    easy_button = transform.scale(easy_button, (240, 90))
    easy_buttonRect = easy_button.get_rect()
    easy_buttonRect.left, easy_buttonRect.top = 120, 15

    medium_button = image.load('images/medium_button.png')
    medium_button = transform.scale(medium_button, (240, 90))
    medium_buttonRect = medium_button.get_rect()
    medium_buttonRect.left, medium_buttonRect.top = 120, 135

    hard_button = image.load('images/hard_button.png')
    hard_button = transform.scale(hard_button, (240, 90))
    hard_buttonRect = hard_button.get_rect()
    hard_buttonRect.left, hard_buttonRect.top = 120, 255

    # Основной цикл
    while Play:
        # Отрисовка фона и кнопок
        window.blit(texture, (0, 0))
        window.blit(easy_button, (120, 15))
        window.blit(medium_button, (120, 135))
        window.blit(hard_button, (120, 255))

        # Обновление дисплея
        display.update()

        # Обработчик событий
        for e in event.get():
            # Закрытие окна
            if e.type == QUIT:
                Play = False

            # Исходя из координат нажатия определяется выбор игрока
            if e.type == MOUSEBUTTONDOWN:
                coords = mouse.get_pos()
                if easy_buttonRect.collidepoint(coords):
                    return 3
                elif medium_buttonRect.collidepoint(coords):
                    return 5
                elif hard_buttonRect.collidepoint(coords):
                    return 7
