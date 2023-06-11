import pygame
import time
import random

# Initial position of the snake
x = 250
y = 250

# Initial speed and direction of the snake
speed = 10
direction = "UP"

# Dimensions of the snake
snake_width = 10
snake_length = 1

# Snake's body
body = []

# Food information
food_x = round(random.randrange(0, 49)) * 10
food_y = round(random.randrange(0, 49)) * 10

pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

game_running = True
clock = pygame.time.Clock()

score = 0
title_font = pygame.font.Font('freesansbold.ttf', 40)
score_font = pygame.font.Font('freesansbold.ttf', 30)

game_start_countdown = 3
start_time = time.time()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Display countdown before the game starts
    if game_start_countdown > 0:
        screen.fill((0, 0, 0))
        title_text = title_font.render("SNAKE GAME", True, (255, 255, 255))
        screen.blit(title_text, (100, 200))

        countdown_text = score_font.render(str(game_start_countdown), True, (255, 255, 255))
        screen.blit(countdown_text, (240, 300))

        pygame.display.update()
        time.sleep(1)

        game_start_countdown -= 1
        if game_start_countdown == 0:
            start_time = time.time()

        continue

    # Calculate game duration after the game starts
    game_duration = int(time.time() - start_time)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    elif keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"

    if direction == "LEFT":
        x -= speed
    elif direction == "RIGHT":
        x += speed
    elif direction == "UP":
        y -= speed
    elif direction == "DOWN":
        y += speed

    # Wrap the snake around the screen edges
    if x < 0:
        x = screen_width - snake_width
    elif x >= screen_width:
        x = 0
    elif y < 0:
        y = screen_height - snake_width
    elif y >= screen_height:
        y = 0

    # Check if the snake collides with itself
    for segment in body:
        if segment[0] == x and segment[1] == y:
            game_running = False

    # Check if the snake eats the food
    if x == food_x and y == food_y:
        score += 1
        food_x = round(random.randrange(0, 49)) * 10
        food_y = round(random.randrange(0, 49)) * 10
        snake_length += 1

    screen.fill((0, 0, 0))  # Clear the screen

    # Update the snake's body
    body.insert(0, [x, y])
    if len(body) > snake_length:
        del body[snake_length]

    # Draw the snake's body
    for segment in body:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], snake_width, snake_width))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_width, snake_width))

    # Display the score and game duration
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    duration_text = score_font.render("Duration: " + str(game_duration), True, (255, 255, 255))
    screen.blit(duration_text, (10, 40))

    pygame.display.update()

    clock.tick(30)

pygame.quit()