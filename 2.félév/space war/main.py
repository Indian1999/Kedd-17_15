import pygame # pip install pygame
import os
import random
import math

WIDTH = 900
HEIGHT = 500

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

SPACESHIP_WIDTH = WIDTH // 11
SPACESHIP_HEIGHT = HEIGHT // 7

FPS = 60
VELOCITY = 5

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

ASSETS = os.path.join(os.path.dirname(__file__), "Assets")

BACKGROUND = pygame.image.load(os.path.join(ASSETS, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)

BORDER = pygame.Rect(WIDTH // 2 - 7, 0, 14, HEIGHT)

def draw_frame(red, yellow):
    WINDOW.blit(BACKGROUND, (0,0))

    pygame.draw.rect(WINDOW, BLACK, BORDER)

    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    pygame.display.update()

    
def red_controll(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x > 5:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_d] and red.x < WIDTH // 2 - SPACESHIP_WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_w] and red.y > 5:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_s] and red.y < HEIGHT - SPACESHIP_HEIGHT - 5:
        red.y += VELOCITY

def yellow_controll(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x > WIDTH // 2 + 5:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and yellow.x < WIDTH - SPACESHIP_WIDTH - 5:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP] and yellow.y > 5:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y < HEIGHT - SPACESHIP_HEIGHT - 5:
        yellow.y += VELOCITY

def main():
    red = pygame.Rect(20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH - SPACESHIP_WIDTH - 20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    gameOn = True
    while gameOn:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pass
        
        keys_pressed = pygame.key.get_pressed()
        red_controll(keys_pressed, red)
        yellow_controll(keys_pressed, yellow)

        draw_frame(red, yellow)

if __name__ == "__main__":
    main()