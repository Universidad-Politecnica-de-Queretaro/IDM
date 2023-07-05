import pygame
import random

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamaño de la serpiente, la comida y el obstáculo
SNAKE_SIZE = 20
FOOD_SIZE = 20
OBSTACLE_SIZE = 20

# Velocidad de movimiento de la serpiente
SNAKE_SPEED = 20

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Viborita")

clock = pygame.time.Clock()

# Función principal del juego
def game():
    # Posición inicial de la serpiente
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2

    # Velocidad inicial de la serpiente
    snake_dx = SNAKE_SPEED
    snake_dy = 0

    # Lista para almacenar las partes del cuerpo de la serpiente
    snake_body = []
    snake_length = 1

    # Posición inicial de la comida
    food_x = round(random.randrange(0, WIDTH - FOOD_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - FOOD_SIZE) / 20.0) * 20.0

    # Puntaje y nivel
    score = 0
    level = 1

    # Variable para controlar si el juego se está ejecutando
    game_over = False

    # Crear obstáculos para niveles avanzados
    obstacles = []
    if level > 1:
        for _ in range(level + 3):
            obstacle_x = round(random.randrange(0, WIDTH - OBSTACLE_SIZE) / 20.0) * 20.0
            obstacle_y = round(random.randrange(0, HEIGHT - OBSTACLE_SIZE) / 20.0) * 20.0
            obstacles.append([obstacle_x, obstacle_y])

    # Ciclo principal del juego
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Capturar eventos de teclado para mover la serpiente
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dx != SNAKE_SPEED:
                    snake_dx = -SNAKE_SPEED
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -SNAKE_SPEED:
                    snake_dx = SNAKE_SPEED
                    snake_dy = 0
                elif event.key == pygame.K_UP and snake_dy != SNAKE_SPEED:
                    snake_dy = -SNAKE_SPEED
                    snake_dx = 0
                elif event.key == pygame.K_DOWN and snake_dy != -SNAKE_SPEED:
                    snake_dy = SNAKE_SPEED
                    snake_dx = 0

        # Mover la serpiente
        snake_x += snake_dx
        snake_y += snake_dy

        # Comprobar si la serpiente ha colisionado con los bordes de la pantalla
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over = True

        # Comprobar si la serpiente ha colisionado consigo misma
        if [snake_x, snake_y] in snake_body[:-1]:
            game_over = True

        # Comprobar si la serpiente ha colisionado con un obstáculo
        for obstacle in obstacles:
            if snake_x == obstacle[0] and snake_y == obstacle[1]:
                game_over = True

        # Comprobar si la serpiente ha comido la comida
        if snake_x == food_x and snake_y == food_y:
            # Generar nueva posición para la comida
            food_x = round(random.randrange(0, WIDTH - FOOD_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - FOOD_SIZE) / 20.0) * 20.0

            # Aumentar la longitud de la serpiente
            snake_length += 1

            # Incrementar el puntaje
            score += 1

            # Comprobar si se alcanzó el puntaje necesario para subir de nivel
            if score % 10 == 0 and level < 4:
                level += 1

                # Crear nuevos obstáculos para el nuevo nivel
                obstacles = []
                for _ in range(level + 3):
                    obstacle_x = round(random.randrange(0, WIDTH - OBSTACLE_SIZE) / 20.0) * 20.0
                    obstacle_y = round(random.randrange(0, HEIGHT - OBSTACLE_SIZE) / 20.0) * 20.0
                    obstacles.append([obstacle_x, obstacle_y])

        # Actualizar la lista de partes del cuerpo de la serpiente
        snake_body.append([snake_x, snake_y])

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Dibujar en la pantalla
        screen.fill(BLACK)

        # Dibujar la serpiente
        for part in snake_body:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], SNAKE_SIZE, SNAKE_SIZE))

        # Dibujar la comida
        pygame.draw.rect(screen, RED, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

        # Dibujar los obstáculos
        for obstacle in obstacles:
            pygame.draw.rect(screen, BLUE, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))

        # Mostrar puntaje y nivel
        font = pygame.font.Font(None, 36)
        text_score = font.render("Puntaje: " + str(score), True, WHITE)
        text_level = font.render("Nivel: " + str(level), True, WHITE)
        screen.blit(text_score, (10, 10))
        screen.blit(text_level, (10, 50))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de actualización
        clock.tick(10)

    # Mostrar mensaje de fin de juego y opciones
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Dibujar en la pantalla
        screen.fill(BLACK)

        # Mostrar mensaje de fin de juego y opciones
        font = pygame.font.Font(None, 36)
        text_game_over = font.render("¡Perdiste! ¿Quieres volver a jugar?", True, WHITE)
        text_retry = font.render("Presiona ENTER para volver a jugar", True, WHITE)
        text_quit = font.render("Presiona ESCAPE para salir", True, WHITE)
        screen.blit(text_game_over, (WIDTH // 2 - text_game_over.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(text_retry, (WIDTH // 2 - text_retry.get_width() // 2, HEIGHT // 2))
        screen.blit(text_quit, (WIDTH // 2 - text_quit.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

# Función para mostrar el menú
def menu():
    menu_running = True

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_running = game()
                    if not game_running:
                        menu_running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Dibujar en la pantalla
        screen.fill(BLACK)

        # Mostrar opciones del menú
        font = pygame.font.Font(None, 36)
        text = font.render("Presiona ENTER para jugar", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

# Ejecutar el menú
menu()
