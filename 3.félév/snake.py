import pygame

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1
        self.x_vel = 0
        self.y_vel = 0
        self.body = []

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel



class SnakeGame:
    WHITE = (255,255,255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)
    YELLOW = (255, 255, 0)
    BLACK = (0,0,0)
    clock = pygame.time.Clock()

    def __init__(self, rows=20, cols=30, pixel_size = 30, speed = 10):
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.speed = speed
        self.WIDTH = cols * pixel_size
        self.HEIGHT = rows * pixel_size
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")

    def draw_frame(self):
        self.window.fill(SnakeGame.BLUE)

        pygame.display.update()

    def game_loop(self):
        game_over = False
        application_close = False

        snake = Snake(
            x = round(self.WIDTH // 2 / self.pixel_size) * self.pixel_size,
            y= round(self.HEIGHT // 2 / self.pixel_size) * self.pixel_size
        )

        while not application_close:
            SnakeGame.clock.tick(self.speed)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    application_close = True
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake.x_vel = -1
                        snake.y_vel = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_vel = 1
                        snake.y_vel = 0
                    if event.key == pygame.K_UP:
                        snake.x_vel = 0
                        snake.y_vel = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_vel = 0
                        snake.y_vel = 1
            
            snake.move()
                
            self.draw_frame()


game = SnakeGame()
game.game_loop()