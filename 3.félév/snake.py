import pygame
import random
import requests
import time
import getpass
pygame.font.init()

class Food:
    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.random_pos()

    def random_pos(self, banned_positions = []):
        self.x = random.randint(0, self.width) // self.pixel_size * self.pixel_size
        self.y = random.randint(0, self.height) // self.pixel_size * self.pixel_size
        while (self.x, self.y) in banned_positions:
            self.x = random.randint(0, self.width) // self.pixel_size * self.pixel_size
            self.y = random.randint(0, self.height) // self.pixel_size * self.pixel_size

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window, pixel_size, color = (20, 190, 20)):
        pygame.draw.rect(window, color, pygame.Rect(self.x, self.y, pixel_size, pixel_size))

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1
        self.x_vel = 0
        self.y_vel = 0
        self.body = [(self.x, self.y)] # (10, 15)
        self.length = 1

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.body.append((self.x, self.y))

    def remove_tail(self):
        if len(self.body) > self.length:
            self.body.pop(0)

    def increase_length(self):
        self.length += 1

    def is_touching(self, food: Food):
        return food.x == self.x and food.y == self.y
    
    def is_self_bitten(self):
        return (self.x, self.y) in self.body[:-1]

    def draw(self, window, pixel_size, color = (0,0,0)):
        for pixel in self.body:
            pygame.draw.rect(window, color, pygame.Rect(pixel[0], pixel[1], pixel_size, pixel_size))

    def __len__(self):
        return self.length
        

class SnakeGame:
    WHITE = (255,255,255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)
    YELLOW = (255, 255, 0)
    BLACK = (0,0,0)
    clock = pygame.time.Clock()
    URL = "https://snake-kedd-default-rtdb.europe-west1.firebasedatabase.app/highscores.json"

    def __init__(self, rows=20, cols=30, pixel_size = 30, speed = 10):
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.speed = speed
        self.WIDTH = cols * pixel_size
        self.HEIGHT = rows * pixel_size
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")

    def get_top_10(self):
        response = requests.get(SnakeGame.URL)

        if response.status_code == 200:
            highscores = response.json()
            highscores_list = list(highscores.items())
            highscores_list.sort(key=lambda x: x[1]["score"], reverse=True)
            highscores_list = highscores_list[:10]
            return dict(highscores_list)

        else:
            raise ConnectionError("Could not connect to Firebase database.")

    def post_highscore(self):
        data = {
            "name": getpass.getuser(),
            "score": self.snake.length - 1,
            "timestamp": int(time.time())
        }
        response = requests.post(SnakeGame.URL, json=data)

        if response.status_code != 200:
            raise ConnectionError("Could not connect to Firebase database.")

    def draw_frame(self):
        self.window.fill(SnakeGame.BLUE)

        self.snake.draw(self.window, self.pixel_size, SnakeGame.BLACK)
        self.food.draw(self.window, self.pixel_size, SnakeGame.GREEN)

        pygame.display.update()

    def draw_game_over_screen(self):
        self.window.fill(SnakeGame.BLUE)

        game_over_font = pygame.font.SysFont("Arial", self.pixel_size)
        score_font = pygame.font.SysFont("Arial", round(self.pixel_size * 1.25))

        game_over_text = game_over_font.render("R: Újraindítás | Q: Kilépés", True, SnakeGame.RED)
        score_text = score_font.render(f"Score: {self.snake.length - 1}", True, SnakeGame.WHITE)
        highscore_text = score_font.render("HIGHSCORES:", True, SnakeGame.BLACK)

        self.window.blit(game_over_text,
                         [self.WIDTH//2 - game_over_text.get_width() // 2,
                          game_over_text.get_height()])
        self.window.blit(score_text,
                         [self.WIDTH//2 - score_text.get_width() // 2,
                          game_over_text.get_height() + score_text.get_height()])
        self.window.blit(highscore_text,
                         [self.WIDTH//2 - highscore_text.get_width() // 2,
                          highscore_text.get_height() +game_over_text.get_height() + score_text.get_height()])
        
        start_y = highscore_text.get_height() +game_over_text.get_height() + score_text.get_height()
        i = 1
        for highscore in self.get_top_10().values():  # {"name": "Dani", "score": 10, "timestamp": 1234213}
            text = game_over_font.render(f"{i}. {highscore['name']}: {highscore['score']}", True, SnakeGame.WHITE)
            self.window.blit(text,
                             [self.WIDTH // 2 - text.get_width() // 2,                                 
                             start_y + i * self.pixel_size * 1.5])
            i += 1
        pygame.display.update()

    def game_loop(self):
        game_over = False
        application_close = False

        self.snake = Snake(
            x = round(self.WIDTH // 2 / self.pixel_size) * self.pixel_size,
            y= round(self.HEIGHT // 2 / self.pixel_size) * self.pixel_size
        )

        self.food = Food(self.WIDTH, self.HEIGHT, self.pixel_size)

        while not application_close:
            SnakeGame.clock.tick(self.speed)

            while game_over:
                self.draw_game_over_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        application_close = True
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_r:
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    application_close = True
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.x_vel != self.pixel_size:
                        self.snake.x_vel = -self.pixel_size
                        self.snake.y_vel = 0
                    if event.key == pygame.K_RIGHT and self.snake.x_vel != -self.pixel_size:
                        self.snake.x_vel = self.pixel_size
                        self.snake.y_vel = 0
                    if event.key == pygame.K_UP and self.snake.y_vel != self.pixel_size:
                        self.snake.x_vel = 0
                        self.snake.y_vel = -self.pixel_size
                    if event.key == pygame.K_DOWN and self.snake.y_vel != -self.pixel_size:
                        self.snake.x_vel = 0
                        self.snake.y_vel = self.pixel_size
            
            self.snake.move()

            if self.snake.x < 0 or self.snake.x > self.WIDTH or self.snake.y < 0 or self.snake.y > self.HEIGHT:
                game_over = True
                self.post_highscore()

            if self.snake.is_touching(self.food):
                self.snake.increase_length()
                self.food.random_pos()
                
            self.snake.remove_tail()

            if self.snake.is_self_bitten():
                game_over = True
                self.post_highscore()
            
            self.draw_frame()


game = SnakeGame()
game.game_loop()