import pygame
import random
import os
import time
pygame.font.init()

class Game:
    WIDTH = 400
    HEIGHT = 450
    FPS = 60
    FRICTION = 0.15
    ASSETS = os.path.join(os.path.dirname(__file__), "assets")
    BACKGROUND_IMAGE = pygame.image.load(os.path.join(ASSETS, "background.png"))
    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH+50, HEIGHT+50))
    COIN_IMAGE = pygame.image.load(os.path.join(ASSETS, "coin.png"))
    PLATFORM_IMAGE = pygame.image.load(os.path.join(ASSETS, "platform.png"))
    PLAYER_IMAGE = pygame.image.load(os.path.join(ASSETS, "player.png"))

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Platformer Game")

    def draw_frame(self):
        self.window.blit(self.BACKGROUND_IMAGE, (-25,-20))

        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, sprite.rect)

        score_font = pygame.font.SysFont("Arial", 25)
        txt = score_font.render(f"Score: {self.score}", True, (0,0,0))

        self.window.blit(txt, (10, 10))
        
        pygame.display.update()

    def generate_platforms(self):
        while len(self.platforms) < 7:
            p = Platform(False, self.platforms)
            self.generate_coin(p.rect.x + p.surf.get_width()//2, p.rect.y - 10, p.xvel)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def check_death(self):
        if self.player.pos.y > Game.HEIGHT + 20:
            return True
        return False
    
    def move_platforms(self):
        for platform in self.platforms:
            platform.move()
        if self.player.rect.top <= Game.HEIGHT // 3:
            move_value = abs(self.player.vel.y)
            self.player.pos.y += move_value
            for platform in self.platforms:
                platform.rect.y += move_value
                if platform.rect.top >= Game.HEIGHT:
                    self.score += 1
                    platform.kill()
        self.move_coins()

    def move_coins(self):
        for coin in self.coins:
            coin.move()
            
        if self.player.rect.top <= Game.HEIGHT // 3:
            move_value = abs(self.player.vel.y)
            for coin in self.coins:
                coin.rect.y += move_value
                if coin.rect.top >= Game.HEIGHT:
                    coin.kill()
        

    def generate_coin(self, x, y, xvel, chance = 0.15):
        if random.random() < chance:
            c = Coin(x, y, xvel)
            self.coins.add(c)
            self.all_sprites.add(c)

    def check_coins(self):
        coin = pygame.sprite.spritecollideany(self.player, self.coins)
        if not coin:
            return
        self.score += 5
        coin.kill()


    def run(self):
        self.player = Player()

        self.score = 0

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.main_platform = Platform()
        self.all_sprites.add(self.main_platform)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.main_platform)
        
        self.coins = pygame.sprite.Group()

        self.generate_platforms()

        while True:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pass
                        #self.player.jump(self.platforms)

            if self.check_death():
                pygame.quit()
                quit()

            self.move_platforms()

            self.generate_platforms()
            self.check_coins()

            self.player.move(self.platforms)
            self.player.jump(self.platforms)
            
            self.draw_frame()

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, xvel):
        super().__init__()
        self.sprite_frames = []
        for img in os.listdir(os.path.join(Game.ASSETS, "coin")):
            path = os.path.join(Game.ASSETS, "coin", img)
            frame = pygame.image.load(path)
            frame = pygame.transform.scale(frame, (30, 30))
            self.sprite_frames.append(frame)
        self.surf = self.sprite_frames[0]
        self.frame_last_changed = time.time()
        self.current_frame = 0
        self.rect = self.surf.get_rect(center=(x, y))
        self.xvel = xvel

    def next_frame(self):
        if time.time() < self.frame_last_changed + 0.05:
            return
        self.current_frame += 1
        self.current_frame %= len(self.sprite_frames)
        self.surf = self.sprite_frames[self.current_frame]
        self.frame_last_changed = time.time()

    def move(self):
        self.rect.x += self.xvel
        if self.rect.x > Game.WIDTH + 60:
            self.rect.x = -60
        if self.rect.x < -60:
            self.rect.x = Game.WIDTH + 60
        self.next_frame()

class Platform(pygame.sprite.Sprite):
    def __init__(self, base_platform = True, platforms = pygame.sprite.Group()):
        super().__init__()
        self.xvel = 0
        if base_platform:
            self.surf = pygame.transform.scale(Game.PLATFORM_IMAGE, (Game.WIDTH, 20))
            self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT-10))
        else:
            self.surf = pygame.transform.scale(Game.PLATFORM_IMAGE, (random.randint(50, 120), 20))
            self.rect = self.surf.get_rect(center=(
                random.randint(0, Game.WIDTH-10), random.randint(0, Game.HEIGHT-10)
            ))
            while pygame.sprite.spritecollideany(self, platforms):
                self.surf = pygame.transform.scale(Game.PLATFORM_IMAGE, (random.randint(50, 120), 20))
                self.rect = self.surf.get_rect(center=(
                    random.randint(0, Game.WIDTH-10), random.randint(0, Game.HEIGHT-10)
                ))
            if random.randint(0,1):
                self.xvel = random.randint(-10, 10) / 5

    def move(self):
        self.rect.x += self.xvel
        if self.rect.x > Game.WIDTH + 60:
            self.rect.x = -60
        if self.rect.x < -60:
            self.rect.x = Game.WIDTH + 60

class Player(pygame.sprite.Sprite):
    ACC = 1
    def __init__(self):
        super().__init__() # Sprite osztály konstruktorát hívja meg
        self.surf = pygame.transform.scale(Game.PLAYER_IMAGE, (50, 50))
        self.rect = self.surf.get_rect(center=(Game.WIDTH // 2, Game.HEIGHT - 50))

        self.jumping = False
        self.pos = self.rect.bottomleft
        self.pos = pygame.Vector2(self.pos[0], self.pos[1])
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)

    def move(self, platforms):
        self.acc = pygame.Vector2(0, 0.98)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.acc.x = -Player.ACC
        if keys_pressed[pygame.K_RIGHT]:
            self.acc.x = Player.ACC

        self.acc.x -= self.vel.x * Game.FRICTION
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x < 0:
            self.pos.x = Game.WIDTH
        if self.pos.x > Game.WIDTH:
            self.pos.x = 0

        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and self.vel.y >= 0:
            self.pos.y = hits[0].rect.top
            self.vel.y = 0
            self.jumping = False
        self.rect.bottomleft = self.pos

    def jump(self, platforms):
        keys_pressed = pygame.key.get_pressed()
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping and keys_pressed[pygame.K_UP]:
            self.jumping = True
            self.vel.y = -22

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3



game = Game()
game.run()