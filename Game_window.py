# В этом файле реализован сам игровой процесс
# Функция game принимает на вход уровен сложности, возвращает результат игры
# Сложность влияет на то, как часто будут появляться новые враги на карте

from random import *

from Enemies import *
from Base import *
from Bullet import *


def game(difficulty):
    # инициализация основных параметров игры
    init()
    W = 640
    H = 480
    display.set_caption('Game')
    window = display.set_mode((W, H))
    keys = {'up': False, 'down': False}
    playerPos = {'x': 135, 'y': 100}
    mousePos = {'x': 0, 'y': 0}

    # загрузка тектур и изображений
    player = image.load('images/player.png')
    player = transform.scale(player, (50, 45))
    texture = image.load('images/texture.jpg')
    texture = transform.scale(texture, (W, H))
    baseImage = image.load('images/base.jpg')
    bullet = image.load('images/bullet.png')
    bullet = transform.scale(bullet, (20, 10))

    # создание базы и определение ее границ
    base = Base(5, H % baseImage.get_height() // 2)
    x = H // baseImage.get_height()
    baseRect = Rect(base.get_coords(), (baseImage.get_width(), baseImage.get_height() * x))

    CanPlay = True
    fps = time.Clock()
    delay = 100
    shooting_type = 1
    shooting_flag = True

    # списки, в которых хранятся противники и выстрелы
    bullets = []
    enemies = []

    # основной игровой цикл
    while CanPlay:
        # отрисовка фона
        window.blit(texture, (0, 0))
        # отрисовка базы
        for y in range(H % baseImage.get_height() // 2, H - baseImage.get_height(), baseImage.get_height()):
            window.blit(baseImage, (5, y))

        # отрисовка игрока с учетом поворота
        mousePos['x'], mousePos['y'] = mouse.get_pos()
        angleRad = atan2(mousePos['y'] - playerPos['y'], mousePos['x'] - playerPos['x'])
        angleDeg = angleRad * 180 / pi
        playerRotated = transform.rotate(player, 360 - angleDeg)
        playerCenter = (playerPos['x'] - playerRotated.get_width() // 2,
                        playerPos['y'] - playerRotated.get_height() // 2)
        window.blit(playerRotated, playerCenter)

        # отрисовка выстрелов
        for b in bullets:
            b.change_coords()
            bulletRotated = transform.rotate(bullet, 360 - b.angle * 180 / pi)
            window.blit(bulletRotated, b.get_coords())
            if b.x < 0 or b.x > W or b.y < 0 or b.y > H:
                bullets.remove(b)

        # отрисовка противников через случайные промежутки времени
        # Чем выше сложность, тем меньше эти промежутки
        # При генерации случайно определяется тип врага и его стартовая координата
        delay -= randint(0, difficulty)
        if delay < 0:
            temp_enemies = [SimpleEnemy(W, H, baseImage.get_height()),
                            HardEnemy(W, H, baseImage.get_height()),
                            FastEnemy(W, H, baseImage.get_height())]
            enemies.append(choice(temp_enemies))
            delay = 100

        # Отрисовываются противники и проверяется попдание по врагу
        # В случае попадания враг теряет хп, а выстрел пропадает
        # Если хп, противника равно 0, то он погибает
        for enemy in enemies:
            enemy.move()
            window.blit(enemy.image, enemy.get_coords())
            enemyRect = enemy.image.get_rect()
            enemyRect.left, enemyRect.top = enemy.get_coords()
            for b in bullets:
                bulletRect = bullet.get_rect()
                bulletRect.left, bulletRect.top = b.get_coords()
                if enemyRect.colliderect(bulletRect):
                    enemy.shot()
                    bullets.remove(b)
                    if enemy.health == 0:
                        enemies.remove(enemy)

        # Проверка повреждения базы противниками
        # В таком случае враг погибает, а база получает урон
        for e in enemies:
            enemyRect = e.image.get_rect()
            enemyRect.left, enemyRect.top = e.get_coords()
            if enemyRect.colliderect(baseRect):
                base.damage(e.damage)
                enemies.remove(e)

        # Отображние текущего игрового времени и здоровья базы
        Font = font.SysFont('Courier', 16, 1, 0)
        timeLabel = Font.render('Time: ' + str(round((time.get_ticks() / 1000), 1)),
                                True, (255, 0, 0), (0, 0, 0))
        healthlabel = Font.render(f'Health: {base.health}%', True, (0, 255, 0), (0, 0, 0))

        window.blit(timeLabel, (5, H - 32))
        window.blit(healthlabel, (5, H - 16))

        # Проверка результата игры
        # Игрок выигрывает, если продержится минуту
        # Если база разрушена, то игрок проиграл
        if base.health <= 0:
            return False
        if time.get_ticks() > 60000:
            return True

        # Обновление дисплея
        fps.tick(60)
        display.update()

        # Обработчик событий
        for e in event.get():
            # закрытие окна
            if e.type == QUIT:
                quit()

            # При зажатии клавиши проиходит движение персонажа игрока
            if e.type == KEYDOWN:
                if e.key == K_w:
                    keys['up'] = True
                elif e.key == K_s:
                    keys['down'] = True
                elif e.key == K_1:
                    if shooting_type != 1:
                        shooting_type = 1
                elif e.key == K_2:
                    if shooting_type != 2:
                        shooting_type = 2
                elif e.key == K_3:
                    if shooting_type != 3:
                        shooting_type = 3

            # Персонаж останавливается, если отпустить клавишу
            if e.type == KEYUP:
                if e.key == K_w:
                    keys['up'] = False
                elif e.key == K_s:
                    keys['down'] = False

            # В игре реализованы три режима стрельбы
            # Первый режим выбран по умолчанию и к нему можно перейти нажав клавишу "1"
            # В нем стрельба ведется одиночными выстрелами
            # Второй режим активироуется по клавише "2"
            # В нем за раз веером разлетается 3 пули
            # Третий режим активируется по клавише "3"
            # В нем снаряды летят с отклонением от изначальной траектории
            # При нажатии ЛКМ происходит выстрел
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if shooting_type == 1:
                    bullets.append(Bullet(angleRad, playerPos['x'], playerPos['y']))
                elif shooting_type == 2:
                    bullets.append(Bullet(angleRad, playerPos['x'], playerPos['y']))
                    bullets.append(Bullet(angleRad + 0.35, playerPos['x'], playerPos['y']))
                    bullets.append(Bullet(angleRad - 0.35, playerPos['x'], playerPos['y']))
                elif shooting_type == 3:
                    if shooting_flag:
                        shooting_flag = False
                        temp_time = time.get_ticks()
                        bullets.append(Bullet(angleRad - 0.35, playerPos['x'], playerPos['y']))
                    if not shooting_flag:
                        if temp_time + 300 < time.get_ticks():
                            bullets.append(Bullet(angleRad + 0.35, playerPos['x'], playerPos['y']))
                            shooting_flag = True

        # Движение персонажа
        if keys['up'] and playerPos['y']:
            playerPos['y'] -= 5
        elif keys['down'] and playerPos['y'] < H - player.get_width():
            playerPos['y'] += 5

    # Цикл, который задерживает закрытие программы
    while True:
        for e in event.get():
            if e.type == QUIT:
                quit()
