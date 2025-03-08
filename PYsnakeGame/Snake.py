import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definir dimensiones de la pantalla
width = 600
height = 400

# Crear la pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Tamaño de la serpiente y velocidad
snake_block = 10
snake_speed = 15

# Estilo de fuente para el menú y el puntaje
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
menu_font = pygame.font.SysFont("comicsansms", 50)

# Función para mostrar el puntaje
def Your_score(score):
    value = score_font.render("Tu Puntaje: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# Función para dibujar la serpiente
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Función para mostrar mensajes en la pantalla
def message(msg, color, y_offset=0, font=font_style):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3 + y_offset])

# Función para mostrar el menú principal
def show_menu():
    menu = True
    while menu:
        screen.fill(black)
        message("Snake Game", green, -100, menu_font)
        message("1. Jugar", white, -50)
        message("2. Instrucciones", white, 0)
        message("3. Salir", white, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "play"
                elif event.key == pygame.K_2:
                    return "instructions"
                elif event.key == pygame.K_3:
                    pygame.quit()
                    quit()

# Función para mostrar las instrucciones
def show_instructions():
    instructions = True
    while instructions:
        screen.fill(black)
        message("Instrucciones:", green, -100, menu_font)
        message("Usa las flechas para mover la serpiente.", white, -50)
        message("Come la comida (cuadro rojo) para crecer.", white, 0)
        message("Evita chocar con los bordes o contigo mismo.", white, 50)
        message("Presiona Q para salir o C para jugar de nuevo.", white, 100)
        message("Presiona M para volver al menú.", white, 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Cambio en la posición de la serpiente
    x1_change = 0
    y1_change = 0

    # Lista para almacenar el cuerpo de la serpiente
    snake_List = []
    Length_of_snake = 1

    # Posición de la comida
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("¡Perdiste! Presiona Q para salir o C para jugar de nuevo", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_m:
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Si la serpiente choca con los bordes, termina el juego
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Dibujar la comida
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Añadir la cabeza de la serpiente a la lista
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Si la serpiente es más larga que su longitud, eliminar la cola
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Si la serpiente choca consigo misma, termina el juego
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Si la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Función principal para manejar el menú y el juego
def main():
    while True:
        choice = show_menu()
        if choice == "play":
            gameLoop()
        elif choice == "instructions":
            show_instructions()

# Iniciar el programa
main()