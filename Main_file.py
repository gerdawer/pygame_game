# Основный файл, в котором "собрана" игра
# При запуске открывается меню, из которого можно перейти в окно выбора уровня
# Есть три уровня разной сложности
# После завершения игры можо вернуться к выбору уровня

from Game_window import game
from Start_Window import start_window
from Result_window import result_window
from Levels_window import levels_window

Play = start_window()

while Play:
    difficulty = levels_window()
    result = game(difficulty)
    Play = result_window(result)
