import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen dimensions
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Snake function to draw the snake
def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_blocks = []
    snake_length = 1

    foodx = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    foody = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            font_style = pygame.font.SysFont("bahnschrift", 25)
            mesg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, RED)
            screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_blocks.append(snake_head)
        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        for block in snake_blocks[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_blocks)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            foody = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        clock.tick(15)

    pygame.quit()

gameLoop()