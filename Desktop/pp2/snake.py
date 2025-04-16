import pygame
import random
import psycopg2
import time

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect("dbname=snake_game user=postgres password=Zz159632")
cursor = conn.cursor()

# Параметры игры
snake_speed = 10
WIDTH = 720
HEIGHT = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Zhylanchick')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
fps = pygame.time.Clock()

# Ввод имени пользователя
username = input("Введите имя пользователя: ")

# Проверка на существующего пользователя
cursor.execute("SELECT user_id, level FROM users WHERE username = %s", (username,))
user_data = cursor.fetchone()

# Если пользователь не найден, создаем нового
if not user_data:
    cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO user_scores (user_id, score) VALUES (%s, %s)", (user_id, 0))
    conn.commit()
    level = 1
    print(f"Новый пользователь {username} создан. Уровень: {level}")
else:
    user_id, level = user_data
    print(f"Добро пожаловать, {username}. Ваш текущий уровень: {level}")

# Инициализация позиции змеи
snake_position = [100, 50]
snake_body = [[100, 50], [80, 50], [60, 50], [40, 50]]
fruit_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Функция для отображения счета
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score : {score}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Функция для завершения игры
def game_over():
    global level
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)

    # Обновляем уровень в зависимости от счета
    if score >= 100:
        level = 2
    elif score >= 200:
        level = 3

    new_level = level
    if score >= 100:
        new_level += 1
        print(f"Поздравляем! Новый уровень: {new_level}")

    # Обновляем уровень в базе данных
    cursor.execute("UPDATE users SET level = %s WHERE user_id = %s", (level, user_id))
    cursor.execute("UPDATE user_scores SET score = %s WHERE user_id = %s", (score, user_id))
    conn.commit()

    pygame.quit()
    quit()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_p:  # Паузим игру при нажатии 'p'
                cursor.execute("UPDATE user_scores SET score = %s WHERE user_id = %s", (score, user_id))
                conn.commit()
                print("Игра приостановлена. Прогресс сохранен.")

    # Изменение направления змеи
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Обновление позиции змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Добавление новой головы
    snake_body.insert(0, list(snake_position))

    # Если змейка съела фрукт, увеличиваем счет
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Появление нового фрукта
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        fruit_spawn = True

    # Рисуем экран
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Проверка на столкновение с границами
    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10 or snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        game_over()

    # Проверка на столкновение с собой
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Отображаем счет
    show_score(1, white, 'times new roman', 20)
    pygame.display.update()

    # Устанавливаем скорость змеи
    fps.tick(snake_speed)
