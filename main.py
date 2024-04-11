import pygame
import random
pygame.init()

# Setting up the game window
window_width = 900
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# snake color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake body
snake_body = []

x1 = window_width / 2
y1 = window_height / 2

x1_change = 0
y1_change = 0

# Snake speed
snake_speed = 10

# Length of snake
length_of_snake = 1

# SCORE
score = 0

# Random position of food
food_x = random.randrange(0, window_width - 10, 10)
food_y = random.randrange(0, window_height - 10, 10)

# Setting snake movement time
clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Checked the pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0

            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0

            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10

            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    # Moving the snake base on window si
    x1 = x1 + x1_change
    y1 = y1 + y1_change
    window.fill(black)

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)

    # Checking when food is eaten
    if x1 == food_x and y1 == food_y:
        food_x = random.randrange(0, window_width - 10, 10)
        food_y = random.randrange(0, window_height - 10, 10)
        snake_speed += 2
        length_of_snake += 1
        score += 1

    # Setting snake boundaries
    if x1 >= window_width or x1 <= 0 or y1 >= window_height or y1<=0:
        game_over = True

    # Checking snake body length
    if len(snake_body) > length_of_snake:
        del snake_body[0]

    # Checking if the snake eat itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    # Adding font to the window
    font_style = pygame.font.SysFont(None, 50)
    score_text = font_style.render("Score: "+str(score), True, white)
    window.blit(score_text, (10, 10))

    # Drawing the snake food
    pygame.draw.rect(window, red, [food_x, food_y, 10, 10])

    # Drawing the initial snake
    for segement in snake_body:
        pygame.draw.rect(window, white, [segement[0], segement[1], 10, 10])
    pygame.display.update()
    clock.tick(snake_speed)

