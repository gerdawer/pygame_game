# Стартовое окно игры

from pygame import *


def start_window():
    # Объявление основных параметров игры
    init()
    W = 480
    H = 360
    display.set_caption('Main Menu')
    window = display.set_mode((W, H))
    Play = True

    # Загрузка текстуры фона и кнопок
    texture = image.load('images/texture.jpg')
    texture = transform.scale(texture, (W, H))

    play_button = image.load('images/play_button.jfif')
    play_button = transform.scale(play_button, (160, 120))
    play_buttonRect = play_button.get_rect()
    play_buttonRect.left, play_buttonRect.top = 160, 55

    exit_button = image.load('images/exit_button.jpg')
    exit_button = transform.scale(exit_button, (160, 120))
    exit_buttonRect = exit_button.get_rect()
    exit_buttonRect.left, exit_buttonRect.top = 160, 185

    # Основной цикл
    while Play:
        # Отрисовка фона и кнопок
        window.blit(texture, (0, 0))
        window.blit(play_button, (160, 55))
        window.blit(exit_button, (160, 185))

        # Обновление экрана
        display.update()

        # Обработчик событий
        for e in event.get():
            # Закрытие окна
            if e.type == QUIT:
                Play = False

            # Определение выбора игрока
            if e.type == MOUSEBUTTONDOWN:
                coords = mouse.get_pos()
                # Переход к выбору уровней
                if play_buttonRect.collidepoint(coords):
                    return True
                # Закрытие окна
                if exit_buttonRect.collidepoint(coords):
                    Play = False
                    exit()
