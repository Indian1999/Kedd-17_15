import pygame # pip install pygame
import os
import random
import math
pygame.mixer.init()
pygame.font.init()

WIDTH = 1280
HEIGHT = 720

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

SPACESHIP_WIDTH = WIDTH // 11
SPACESHIP_HEIGHT = HEIGHT // 7

METEOR_WIDTH = WIDTH // 19
METEOR_HEIGHT = HEIGHT // 10

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


METEOR = pygame.image.load(os.path.join(ASSETS, "meteor.png"))
METEOR = pygame.transform.scale(METEOR, (METEOR_WIDTH, METEOR_HEIGHT))

BORDER = pygame.Rect(WIDTH // 2 - 7, 0, 14, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("arial", 40)

class Bullet:
    def __init__(self, x, y, direction = 1):
        self.rect= pygame.Rect(x, y, 10, 5)
        self.dire = direction

    def handle_movement(self, player):
        self.rect.x += self.dire * (VELOCITY+3)
        if self.rect.x < -50 or self.rect.x > WIDTH+50:
            player.bullets.remove(self)

class Yellow:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH - SPACESHIP_WIDTH - 20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.health = 10
        self.bullets = []

    def controll(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.x > WIDTH // 2 + 5:
            self.rect.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < WIDTH - SPACESHIP_WIDTH - 5:
            self.rect.x += VELOCITY
        if keys_pressed[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and self.rect.y < HEIGHT - SPACESHIP_HEIGHT - 5:
            self.rect.y += VELOCITY

    def shoot(self):
        if len(self.bullets) < 3:
            start_x = self.rect.x - 10
            start_y = self.rect.y + SPACESHIP_HEIGHT // 2
            bullet = Bullet(start_x, start_y, -1)
            self.bullets.append(bullet)

class Red:
    def __init__(self):
        self.rect = pygame.Rect(20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.health = 10
        self.bullets = []

    def controll(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= VELOCITY
        if keys_pressed[pygame.K_d] and self.rect.x < WIDTH // 2 - SPACESHIP_WIDTH:
            self.rect.x += VELOCITY
        if keys_pressed[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= VELOCITY
        if keys_pressed[pygame.K_s] and self.rect.y < HEIGHT - SPACESHIP_HEIGHT - 5:
            self.rect.y += VELOCITY

    def shoot(self):
        if len(self.bullets) < 3:
            start_x = self.rect.x + SPACESHIP_WIDTH - 5
            start_y = self.rect.y + SPACESHIP_HEIGHT // 2
            bullet = Bullet(start_x, start_y, 1)
            self.bullets.append(bullet)

class Meteor:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, METEOR_WIDTH, METEOR_HEIGHT)
        self.direction = (0, 0)
        self.setup()
    
    def setup(self):
        area = random.randint(1, 4)
        if area == 1:
            x = random.randint(-100, WIDTH + 100)
            y = random.randint(-100, -50)
        elif area == 2:
            x = random.randint(-100, -50)
            y = random.randint(0, HEIGHT)
        elif area == 3:
            x = random.randint(WIDTH + 50, WIDTH + 100)
            y = random.randint(0, HEIGHT)
        else:
            x = random.randint(-100, WIDTH + 100)
            y = random.randint(HEIGHT+50, HEIGHT+100)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        x_goal = random.randint(50, WIDTH - 50)
        y_goal = random.randint(50, HEIGHT - 50)
        d = ((x_goal-x)**2 + (y_goal-y)**2)**0.5
        self.direction = ((x_goal-x)/d, (y_goal-y)/d)

    def handle_movement(self):
        self.x += self.direction[0] * (VELOCITY - 1)
        self.y += self.direction[1] * (VELOCITY - 1)
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x < -50 or self.rect.x > WIDTH + 50:
            self.setup()
            return
        if self.rect.y < -50 or self.rect.y > HEIGHT + 50:
            self.setup()

def draw_frame(red, yellow, meteors):
    WINDOW.blit(BACKGROUND, (0,0))

    pygame.draw.rect(WINDOW, BLACK, BORDER)

    WINDOW.blit(RED_SPACESHIP, (red.rect.x, red.rect.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.rect.x, yellow.rect.y))

    for bullet in red.bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow.bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    for meteor in meteors:
        WINDOW.blit(METEOR, (meteor.rect.x, meteor.rect.y))

    red_health_text = HEALTH_FONT.render(f"Health: {red.health}", True, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Health: {yellow.health}", True, WHITE)
    WINDOW.blit(red_health_text, (10, 10))
    WINDOW.blit(yellow_health_text, (WIDTH-yellow_health_text.get_width()-10, 10))

    pygame.display.update()
  
def draw_winner(text):
    font = pygame.font.SysFont("Arial", 100)
    rendered = font.render(text, True, WHITE)
    left = WIDTH // 2 - rendered.get_width() // 2
    top = HEIGHT // 2 - rendered.get_height() // 2
    WINDOW.blit(rendered, (left, top))
    pygame.display.update()
    pygame.time.delay(5000) # 5mp

def check_meteor_damage(meteors, red, yellow):
    for meteor in meteors:
        if meteor.rect.colliderect(red.rect):
            meteor.setup()
            pygame.event.post(pygame.event.Event(RED_HIT))
        if meteor.rect.colliderect(yellow.rect):
            meteor.setup()
            pygame.event.post(pygame.event.Event(YELLOW_HIT))

def check_bullet_damage(red, yellow):
    for bullet in red.bullets:
        if bullet.rect.colliderect(yellow.rect):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red.bullets.remove(bullet)
    for bullet in yellow.bullets:
        if bullet.rect.colliderect(red.rect):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow.bullets.remove(bullet)

def main():
    red = Red()
    yellow = Yellow()

    meteors = [Meteor() for i in range(3)]

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
                if event.key == pygame.K_LCTRL:
                    red.shoot()
                    LASER_SOUND.play()
                if event.key == pygame.K_RCTRL:
                    yellow.shoot()
                    LASER_SOUND.play()
            if event.type == RED_HIT:
                red.health -= 1
                EXPLOSION_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow.health -= 1
                EXPLOSION_SOUND.play()

        keys_pressed = pygame.key.get_pressed()
        red.controll(keys_pressed)
        yellow.controll(keys_pressed)
        for bullet in yellow.bullets:
            bullet.handle_movement(yellow)
        for bullet in red.bullets:
            bullet.handle_movement(red)
        for meteor in meteors:
            meteor.handle_movement()

        check_meteor_damage(meteors, red, yellow)
        check_bullet_damage(red, yellow)

        draw_frame(red, yellow, meteors)
        
        if yellow.health <= 0:
            draw_winner("Red Wins!")
            break
        if red.health <= 0:
            draw_winner("Yellow Wins!")
            break

if __name__ == "__main__":
    main()