import pygame # pip install pygame
import os
import random
import math
pygame.mixer.init()
pygame.font.init()

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

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

ASSETS = os.path.join(os.path.dirname(__file__), "Assets")

LASER_SOUND = pygame.mixer.Sound(os.path.join(ASSETS, "laser.wav"))
LASER_SOUND.set_volume(0.3)
EXPLOSION_SOUND = pygame.mixer.Sound(os.path.join(ASSETS, "explosion.wav"))
EXPLOSION_SOUND.set_volume(0.2)

BACKGROUND = pygame.image.load(os.path.join(ASSETS, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)

BORDER = pygame.Rect(WIDTH // 2 - 7, 0, 14, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("arial", 40)

def draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WINDOW.blit(BACKGROUND, (0,0))

    pygame.draw.rect(WINDOW, BLACK, BORDER)

    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    red_health_text = HEALTH_FONT.render(f"Health: {red_health}", True, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Health: {yellow_health}", True, WHITE)
    WINDOW.blit(red_health_text, (10, 10))
    WINDOW.blit(yellow_health_text, (WIDTH-yellow_health_text.get_width()-10, 10))

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

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x += VELOCITY * 1.5
        if bullet.x > WIDTH:
            red_bullets.remove(bullet)
        if bullet.colliderect(yellow):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))

    for bullet in yellow_bullets:
        bullet.x -= VELOCITY * 1.5
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        if bullet.colliderect(red):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))
    
def draw_winner(text):
    font = pygame.font.SysFont("Arial", 100)
    rendered = font.render(text, True, WHITE)
    left = WIDTH // 2 - rendered.get_width() // 2
    top = HEIGHT // 2 - rendered.get_height() // 2
    WINDOW.blit(rendered, (left, top))
    pygame.display.update()
    pygame.time.delay(5000) # 5mp

def main():
    red = pygame.Rect(20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH - SPACESHIP_WIDTH - 20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

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
                if event.key == pygame.K_LCTRL and len(red_bullets) < 3:
                    start_x = red.x + SPACESHIP_WIDTH - 5
                    start_y = red.y + SPACESHIP_HEIGHT // 2
                    bullet = pygame.Rect(start_x, start_y, 10, 5)
                    red_bullets.append(bullet)
                    LASER_SOUND.play()
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < 3:
                    start_x = yellow.x - 10
                    start_y = yellow.y + SPACESHIP_HEIGHT // 2
                    bullet = pygame.Rect(start_x, start_y, 10, 5)
                    yellow_bullets.append(bullet)
                    LASER_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                EXPLOSION_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                EXPLOSION_SOUND.play()

        keys_pressed = pygame.key.get_pressed()
        red_controll(keys_pressed, red)
        yellow_controll(keys_pressed, yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)

        draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
        if yellow_health <= 0:
            draw_winner("Red Wins!")
            break
        if red_health <= 0:
            draw_winner("Yellow Wins!")
            break

if __name__ == "__main__":
    main()