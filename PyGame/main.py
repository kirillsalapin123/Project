import pygame
import sys
from button import ImageButton
from random import randint as ri

pygame.mixer.pre_init(44100, -16, 1, 512)  # важно вызвать до pygame.init()

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1280, 720
MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Отображаемое название меню
pygame.display.set_caption("PyGame test Game")

# Загрузка изображения
fon = pygame.image.load(f"images/fons/menu_fon{WIDTH}x{HEIGHT}.png").convert_alpha()

# Создайте объекты Sound для музыки меню и музыки игры
menu_music = pygame.mixer.Sound("music/menu_music.mp3")
game_music = pygame.mixer.Sound("music/game_music.mp3")
menu = True
game = True

clock = pygame.time.Clock()

# Иконка игры
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)

# Загрузка и установка курсора
cursor = pygame.image.load("images/cursor.png")
pygame.mouse.set_visible(False)  # Скрываем стандартный курсор


def main_menu():
    global menu

    if menu:
        menu_music.play(-1)
    else:
        menu_music.stop()

    # Создание кнопок
    play = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Play",
                       "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    settings = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "Настройки",
                           "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    exit_game = ImageButton(WIDTH / 2 - (252 / 2), 470, 252, 74, "Выйти",
                            "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Меню", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == play:
                menu_music.stop()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings:
                settings_menu()
                for btn in [play, settings, exit_game]:
                    btn.set_pos(WIDTH / 2 - (252 / 2))

            if event.type == pygame.USEREVENT and event.button == exit_game:
                pygame.quit()
                sys.exit()

            for btn in [play, settings, exit_game]:
                btn.handle_event(event)

        for btn in [play, settings, exit_game]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def settings_menu():
    # Создание кнопок
    video_button = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Видео",
                               "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    audio_button = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "Аудио",
                               "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 470, 252, 74, "Назад",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Настройки", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == video_button:
                video_settings_menu()
                for btn in [audio_button, video_button, back_button]:
                    btn.set_pos(WIDTH / 2 - (252 / 2))

            if event.type == pygame.USEREVENT and event.button == audio_button:
                audio_settings_menu()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def video_settings_menu():
    # Создание кнопок
    video1_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Full HD",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    video2_button = ImageButton(WIDTH / 2 - (252 / 2), 330, 252, 74, "1280x720",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    video3_button = ImageButton(WIDTH / 2 - (252 / 2), 410, 252, 74, "1024x720",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    video4_button = ImageButton(WIDTH / 2 - (252 / 2), 490, 252, 74, "1024x600",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 570, 252, 74, "Назад",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Настройки видео", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == video1_button:
                change_video_mode(1920, 1080)
                running = False

            if event.type == pygame.USEREVENT and event.button == video2_button:
                change_video_mode(1280, 720)
                running = False

            if event.type == pygame.USEREVENT and event.button == video3_button:
                change_video_mode(1024, 720)
                running = False

            if event.type == pygame.USEREVENT and event.button == video4_button:
                change_video_mode(1024, 600)
                running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [video1_button, video2_button, video3_button, video4_button, back_button]:
                btn.handle_event(event)

        for btn in [video1_button, video2_button, video3_button, video4_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def audio_settings_menu():
    # Создание кнопок
    audio1_button = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Фоновая музыка",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    audio2_button = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "Мызыка игры",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    audio3_button = ImageButton(WIDTH / 2 - (252 / 2), 470, 252, 74, "Звуки игры",
                                "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 570, 252, 74, "Назад",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Настройки аудио", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == audio1_button:
                audio_settings_fon_music()

            if event.type == pygame.USEREVENT and event.button == audio2_button:
                audio_settings_fon_game_music()

            if event.type == pygame.USEREVENT and event.button == audio3_button:
                audio_settings_fon_game_music()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio1_button, audio2_button, audio3_button, back_button]:
                btn.handle_event(event)

        for btn in [audio1_button, audio2_button, audio3_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def audio_settings_fon_music():
    global menu

    # Создание кнопок
    audio_on_button = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Вкл",
                                  "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    audio_off_button = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "Выкл",
                                   "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 485, 252, 74, "Назад",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Фоновоя музыка меню", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == audio_off_button:
                if menu:
                    menu_music.stop()
                    menu = False
            elif event.type == pygame.USEREVENT and event.button == audio_on_button:
                if not menu:
                    menu_music.play(-1)
                    menu = True

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio_on_button, audio_off_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_on_button, audio_off_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def audio_settings_fon_game_music():
    global game

    # Создание кнопок
    audio_on_button = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Вкл",
                                  "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    audio_off_button = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "Выкл",
                                   "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    back_button = ImageButton(WIDTH / 2 - (252 / 2), 485, 252, 74, "Назад",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Музыка игры", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == audio_off_button:
                game = False
            elif event.type == pygame.USEREVENT and event.button == audio_on_button:
                game = True

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio_on_button, audio_off_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_on_button, audio_off_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def new_game():
    global game
    global menu
    # --------------------[Настройки игры]-----------------------

    # Фон
    game_fon = pygame.image.load(f"images/fons/game_fon{WIDTH}x{HEIGHT}.png").convert_alpha()

    # Музыка
    if game:
        game_music.play(-1)
    else:
        game_music.stop()

    # Музыка при проигрыше
    gameover = pygame.mixer.Sound('music/gameover.mp3')

    # -----------------------------------------------------------

    # --------------------[Player]-------------------------------\

    # Настройка скорости игрока
    player_speed = 2.3

    # Настройка первоначального положения игрока по x
    player_x = 150

    # Настройка первоначального положения игрока по y
    if HEIGHT == 1080:
        player_y = 735
    elif HEIGHT == 720:
        player_y = 535
    elif HEIGHT == 600:
        player_y = 440

    # Параметры прыжка
    is_jumping = False
    jump_velocity = 9  # Высота прыжка
    if HEIGHT == 1080:
        player_jump_y = 735
    elif HEIGHT == 720:
        player_jump_y = 535
    elif HEIGHT == 600:
        player_jump_y = 440
    gravity = 0.3  # скорость подъема\спуска
    jump_height = jump_velocity

    # Начальное здоровье игрока
    player_health = 3

    player_anim_speed = 10  # Чем больше значение, тем медленнее анимация
    igrok_anim_count = 0
    player_anim_count = 0
    fon_x = 0

    # Список картинок анимаций для игрока
    walk_right = [
        pygame.image.load("images/player/player_right/player_right.png").convert_alpha(),
        pygame.image.load("images/player/player_right/player_right1.png").convert_alpha(),
        pygame.image.load("images/player/player_right/player_right2.png").convert_alpha(),
        pygame.image.load("images/player/player_right/player_right3.png").convert_alpha(),
    ]

    walk_left = [
        pygame.image.load("images/player/player_left/player_left.png").convert_alpha(),
        pygame.image.load("images/player/player_left/player_left1.png").convert_alpha(),
        pygame.image.load("images/player/player_left/player_left2.png").convert_alpha(),
        pygame.image.load("images/player/player_left/player_left3.png").convert_alpha(),
    ]

    # -----------------------------------------------------------

    # --------------------[Враги]--------------------------------

    zombi = [
        pygame.image.load('images/zombi/1.png').convert_alpha(),
        pygame.image.load('images/zombi/2.png').convert_alpha(),
        pygame.image.load('images/zombi/3.png').convert_alpha(),
        pygame.image.load('images/zombi/4.png').convert_alpha(),
        pygame.image.load('images/zombi/5.png').convert_alpha(),
        pygame.image.load('images/zombi/6.png').convert_alpha(),
        pygame.image.load('images/zombi/7.png').convert_alpha(),
        pygame.image.load('images/zombi/8.png').convert_alpha(),
        pygame.image.load('images/zombi/9.png').convert_alpha(),
        pygame.image.load('images/zombi/10.png').convert_alpha(),
        pygame.image.load('images/zombi/11.png').convert_alpha(),
        pygame.image.load('images/zombi/12.png').convert_alpha(),
        pygame.image.load('images/zombi/13.png').convert_alpha(),
        pygame.image.load('images/zombi/14.png').convert_alpha(),
        pygame.image.load('images/zombi/15.png').convert_alpha(),
        pygame.image.load('images/zombi/16.png').convert_alpha(),
        pygame.image.load('images/zombi/17.png').convert_alpha(),
        pygame.image.load('images/zombi/18.png').convert_alpha(),
    ]

    zombi_anim_count = 0
    zombibi_anim_count = 0
    zombi_list = []
    zombi_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        zombi_y = 690
    elif HEIGHT == 720:
        zombi_y = 490
    elif HEIGHT == 600:
        zombi_y = 390
    zombi_anim_speed = 18  # Чем меньше значение, тем быстрее анимация
    zombi_speed = 3

    ghost_image = pygame.image.load("images/ghost.png").convert_alpha()

    ghost_list_in_game = []
    ghost_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        ghost_y = 743
    elif HEIGHT == 720:
        ghost_y = 553
    elif HEIGHT == 600:
        ghost_y = 453
    ghost_speed = 3

    aptechka_image = pygame.image.load("images/heart/1.png").convert_alpha()

    aptechka_list_in_game = []
    aptechka_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        aptechka_y = 733
    elif HEIGHT == 720:
        aptechka_y = 543
    elif HEIGHT == 600:
        aptechka_y = 443
    aptechka_speed = 3

    aptechka_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(aptechka_timer, 5000)

    score_list_in_game = []
    score_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        score_y = 750
    elif HEIGHT == 720:
        score_y = 550
    elif HEIGHT == 600:
        score_y = 450
    score_speed = 3

    score_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(score_timer, 5000)

    diamond_list_in_game = []
    diamond_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        diamond_y = 754
    elif HEIGHT == 720:
        diamond_y = 554
    elif HEIGHT == 600:
        diamond_y = 454
    diamond_speed = 3

    diamond_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(diamond_timer, 5000)

    bullet_list_in_game = []
    bullet_rect_x = WIDTH + 50
    if HEIGHT == 1080:
        bullet_y = 752
    elif HEIGHT == 720:
        bullet_y = 562
    elif HEIGHT == 600:
        bullet_y = 462
    bullet_speed = 3

    bullet_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(bullet_timer, 5000)

    # -----------------------------------------------------------

    # --------------------[Шрифты,Надписи]-------------------------------

    laber1 = pygame.font.Font("shrifts/Gilroy.ttf", 20)

    # Шрифт кнопки Начать заново
    laber2 = pygame.font.Font("shrifts/Gilroy.ttf", 40)

    laber3 = pygame.font.Font("shrifts/Gilroy.ttf", 20)

    # Настройка надписи Начать заново
    restart_game = laber2.render('Начать заново', True, (70, 242, 2))
    restart_game_rect = restart_game.get_rect(topleft=(WIDTH/2-(292/2), 250))

    heart1 = pygame.image.load("images/heart/1.png").convert_alpha()

    # -----------------------------------------------------------

    bullets_left = 5
    bullet_right = pygame.image.load("images/bullet-right.png").convert_alpha()
    bullet_left = pygame.image.load("images/bullet-left.png").convert_alpha()
    bullet = pygame.image.load("images/icon-bullets.png").convert_alpha()
    icon_bullets = pygame.image.load("images/icon-bullets.png").convert_alpha()
    bullets = []

    score = 0
    icon_score_image = pygame.image.load("images/score.png").convert_alpha()
    score_img = pygame.image.load("images/icon-score.png").convert_alpha()

    diamond = 0
    icon_diamond_image = pygame.image.load("images/diamond.png").convert_alpha()
    diamond_img = pygame.image.load("images/icon-diamond.png").convert_alpha()

    game_over_fon = pygame.image.load("images/gameover.png").convert_alpha()

    # Инициализация переменной направления игрока
    facing_right = True

    # Переменная для отслеживания, продолжается ли игра
    gameplay = True

    # Переменная для отслеживания, работает ли основной игровой цикл
    running = True

    # Основной цикл
    while running:

        if player_health <= 0 and gameplay:
            gameover.play()
            gameplay = False

        # Отображаем картинку
        screen.blit(game_fon, (fon_x, 0))
        screen.blit(game_fon, (fon_x + WIDTH, 0))

        # игровой цикл
        if gameplay:
            # Отображение здоровья игрока
            for i in range(player_health):
                screen.blit(heart1, (WIDTH / 2 - (252 / 2) + WIDTH / 2.1 + i * 50, 5))

            # Отображение количества патронов
            bullets_list = laber3.render(str(bullets_left), False, (250, 252, 252))
            screen.blit(bullets_list, (40, 10))
            screen.blit(icon_bullets, (15, 10))

            # Отображение количества очков
            score_list = laber1.render(str(score), False, (250, 252, 252))
            screen.blit(score_img, (15, 41))
            screen.blit(score_list, (43, 40))

            # Отображение количества алмазов
            diamond_list = laber1.render(str(diamond), False, (250, 252, 252))
            screen.blit(diamond_img, (15, 71))
            screen.blit(diamond_list, (43, 70))

            # Обновление позиции игрока
            player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

            check = ri(0, 400)
            if check == 2:
                ghost_list_in_game.append(ghost_image.get_rect(topleft=(WIDTH, ghost_y)))
                ghost_rect_x -= 4

            if ghost_list_in_game:
                for (i, el) in enumerate(ghost_list_in_game):
                    screen.blit(ghost_image, el)
                    el.x -= ghost_speed
                    if el.x < -10:
                        ghost_list_in_game.pop(i)
                    if player_rect.colliderect(el):
                        player_health -= 1
                        ghost_list_in_game.pop(i)

            check = ri(0, 1000)
            if check == 2:
                aptechka_list_in_game.append(aptechka_image.get_rect(topleft=(WIDTH, aptechka_y)))
                aptechka_rect_x -= 4

            if aptechka_list_in_game:
                for (i_a, el_a) in enumerate(aptechka_list_in_game):
                    screen.blit(aptechka_image, el_a)
                    el_a.x -= aptechka_speed
                    if el_a.x < -10:
                        aptechka_list_in_game.pop(i_a)
                    if player_rect.colliderect(el_a):
                        if player_health <= 2:
                            player_health += 1
                        aptechka_list_in_game.pop(i_a)

            check = ri(0, 1000)
            if check == 2:
                bullet_list_in_game.append(bullet.get_rect(topleft=(WIDTH, bullet_y)))
                bullet_rect_x -= 4

            if bullet_list_in_game:
                for (b_a, el_a) in enumerate(bullet_list_in_game):
                    screen.blit(bullet, el_a)
                    el_a.x -= bullet_speed
                    if el_a.x < -10:
                        bullet_list_in_game.pop(b_a)
                    if player_rect.colliderect(el_a):
                        if bullets_left <= 4:
                            bullets_left += 1
                        bullet_list_in_game.pop(b_a)

            check = ri(0, 1000)
            if check == 2:
                score_list_in_game.append(icon_score_image.get_rect(topleft=(WIDTH, score_y)))
                score_rect_x -= 4

            if score_list_in_game:
                for (i_s, el_s) in enumerate(score_list_in_game):
                    screen.blit(icon_score_image, el_s)
                    el_s.x -= score_speed
                    if el_s.x < -10:
                        score_list_in_game.pop(i_s)
                    if player_rect.colliderect(el_s):
                        score += 100
                        score_list_in_game.pop(i_s)

            check = ri(0, 1000)
            if check == 2:
                diamond_list_in_game.append(icon_diamond_image.get_rect(topleft=(WIDTH, diamond_y)))
                diamond_rect_x -= 4

            if diamond_list_in_game:
                for (d_s, el_s) in enumerate(diamond_list_in_game):
                    screen.blit(icon_diamond_image, el_s)
                    el_s.x -= diamond_speed
                    if el_s.x < -10:
                        diamond_list_in_game.pop(d_s)
                    if player_rect.colliderect(el_s):
                        diamond += 1
                        diamond_list_in_game.pop(d_s)

            check = ri(0, 400)
            if check == 2:
                zombi_list.append(zombi[zombi_anim_count].get_rect(topleft=(zombi_rect_x, zombi_y)))
                zombi_rect_x -= 4

            if zombi_list:
                for (i_z, el_z) in enumerate(zombi_list):
                    screen.blit(zombi[zombi_anim_count], el_z)
                    el_z.x -= zombi_speed
                    if el_z.x < -10:
                        zombi_list.pop(i_z)
                    zombi_collision_rect = el_z.inflate(-34, -34)
                    if player_rect.colliderect(zombi_collision_rect):
                        player_health -= 1
                        zombi_list.pop(i_z)

            # Настройка хадьбы игрока вперед,назад
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                facing_right = False
                player_x -= player_speed
            else:
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    facing_right = True
                    player_x += player_speed

            # Отрисовка игрока
            if facing_right:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))
            else:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))

            # Настройка границы карты для игрока
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0 or keys[pygame.K_a] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < WIDTH - 40 or keys[pygame.K_d] and player_x < WIDTH - 40:
                player_x += player_speed

            # Логика прыжка
            if not is_jumping:
                if keys[pygame.K_SPACE]:
                    is_jumping = True
                    jump_height = jump_velocity
            else:
                player_y -= jump_height
                jump_height -= gravity
                if player_y >= player_jump_y:
                    player_y = player_jump_y
                    is_jumping = False

            # Обновление счетчика анимации
            igrok_anim_count += 1
            if igrok_anim_count >= player_anim_speed:
                player_anim_count = (player_anim_count + 1) % len(walk_right)
                igrok_anim_count = 0  # Сброс счетчика после обновления кадра анимации

            zombibi_anim_count += 1
            if zombibi_anim_count >= zombi_anim_speed:
                # Обновляем кадр анимации зомби
                zombi_anim_count = (zombi_anim_count + 1) % len(zombi)

            # анимация фона
            fon_x -= 2
            if fon_x <= -WIDTH:
                fon_x = 0

            if bullets:
                for (i, (el, direction)) in enumerate(bullets):
                    if facing_right:
                        screen.blit(bullet_right, (el.x, el.y))
                    else:
                        screen.blit(bullet_left, (el.x, el.y))
                    el.x += direction * 3.5  # Движение в зависимости от направления (вправо или влево)

                    if el.x > WIDTH + 30 or el.x < -30:  # Удаление пуль, вышедших за пределы экрана
                        bullets.pop(i)

                    # Проверка столкновений между пулями и призраками
                    if ghost_list_in_game:
                        for (index, ghost_el) in enumerate(ghost_list_in_game):
                            if el.colliderect(ghost_el):
                                ghost_list_in_game.pop(index)
                                score += 100
                                bullets.pop(i)

                    # Проверка столкновений между пулями и зомби
                    if zombi_list:
                        for (index, zombi_el) in enumerate(zombi_list):
                            if el.colliderect(zombi_el):
                                zombi_list.pop(index)
                                score += 100
                                bullets.pop(i)

                    # Проверка что пули не сталкиваются с игроком
                    if player_rect.colliderect(el):
                        continue  # Игнорируем столкновение пули с игроком
        else:
            screen.blit(game_over_fon, (WIDTH / 2 - (572 / 2), 150))
            screen.blit(restart_game, restart_game_rect)

            game = False
            if not game:
                game_music.stop()

            # Отслеживаем местоположение курсора мыши
            mouse = pygame.mouse.get_pos()
            # Отображаем курсор в текущей позиции мыши
            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 2, y - 2))
            if restart_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                game = True
                if game:
                    game_music.play(-1)
                    game = False
                score = 0   # Сброс монет
                diamond = 0  # Сброс алмазов
                player_x = 150  # Сброс положения игрока
                player_health = 3  # Сброс здоровья игрока
                ghost_list_in_game.clear()  # Удаление всех призраков
                aptechka_list_in_game.clear()  # Удаление всех аптечек
                zombi_list.clear()  # Удаление всех зомби
                bullets.clear()  # Удаление всех патронов
                bullets_left = 5  # Сброс патронов

        # Обновление дисплея
        pygame.display.update()

        # Ивент выключения игры нажатием крестика
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в главное меню
                if event.key == pygame.K_ESCAPE:
                    game_music.stop()
                    if menu:
                        menu_music.play(-1)
                    else:
                        menu_music.stop()
                    menu_esc()

            # Настройки снаряда
            if event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
                direction = 1 if facing_right else -1
                if facing_right:
                    new_bullet = bullet_right.get_rect(topleft=(player_x + (30 if facing_right else -10), player_y + 10))
                else:
                    new_bullet = bullet_left.get_rect(
                        topleft=(player_x + (30 if facing_right else -10), player_y + 10))
                bullets.append((new_bullet, direction))
                bullets_left -= 1

        clock.tick(MAX_FPS)


def menu_esc():
    global game
    global menu

    if menu:
        menu_music.play(-1)
    else:
        menu_music.stop()

    # Создание кнопок
    menu_button = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "главное меню",
                              "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    continue_button = ImageButton(WIDTH / 2 - (252 / 2), 385, 252, 74, "продолжить",
                                  "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    restart_button = ImageButton(WIDTH / 2 - (252 / 2), 470, 252, 74, "начать заново",
                                 "images/button/button.png", "images/button/button_click.png", "music/click.mp3")
    settings_button = ImageButton(WIDTH / 2 - (252 / 2), 570, 252, 74, "Настройки",
                                  "images/button/button.png", "images/button/button_click.png", "music/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Меню", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_music.stop()
                    if game:
                        game_music.play(-1)
                    else:
                        game_music.stop()
                    running = False

            if event.type == pygame.USEREVENT and event.button == menu_button:
                menu_music.stop()
                main_menu()
                running = False
                for btn in [menu_button, continue_button, restart_button]:
                    btn.set_pos(WIDTH / 2 - (252 / 2))

            if event.type == pygame.USEREVENT and event.button == continue_button:
                menu_music.stop()
                if game:
                    game_music.play(-1)
                else:
                    game_music.stop()
                running = False

            if event.type == pygame.USEREVENT and event.button == restart_button:
                menu_music.stop()
                if game:
                    game_music.play(-1)
                else:
                    game_music.stop()
                running = False

            if event.type == pygame.USEREVENT and event.button == settings_button:
                settings_menu()

            for btn in [menu_button, continue_button, restart_button, settings_button]:
                btn.handle_event(event)

        for btn in [menu_button, continue_button, restart_button, settings_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        # Отображаем курсор в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def change_video_mode(w, h):
    global WIDTH, HEIGHT, screen, fon

    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    fon = pygame.image.load(f"images/fons/menu_fon{WIDTH}x{HEIGHT}.png")


if __name__ == "__main__":
    main_menu()
