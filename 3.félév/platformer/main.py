import pygame
import random
pygame.font.init()

class Game:
    WIDTH = 400
    HEIGHT = 450
    FPS = 60
    FRICTION = 0.15
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Platformer Game")

    def draw_frame(self):
        self.window.fill((200, 200, 200))

        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, sprite.rect)

        score_font = pygame.font.SysFont("Arial", 25)
        txt = score_font.render(f"Score: {self.score}", True, (0,0,0))

        self.window.blit(txt, (10, 10))
        
        pygame.display.update()

    def generate_platforms(self):
        while len(self.platforms) < 7:
            p = Platform(False, self.platforms)
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

    def run(self):
        self.player = Player()

        self.score = 0

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.main_platform = Platform()
        self.all_sprites.add(self.main_platform)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.main_platform)

        for i in range(6):
            platform = Platform(base_platform=False, platforms = self.platforms)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

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

            self.player.move(self.platforms)
            self.player.jump(self.platforms)
            
            self.draw_frame()

class Platform(pygame.sprite.Sprite):
    def __init__(self, base_platform = True, platforms = pygame.sprite.Group()):
        super().__init__()
        self.xvel = 0
        if base_platform:
            self.surf = pygame.Surface((Game.WIDTH, 20))
            self.surf.fill((230, 43, 28))
            self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT-10))
        else:
            self.surf = pygame.Surface((random.randint(50, 120), 20))
            self.surf.fill((230, 43, 28))
            self.rect = self.surf.get_rect(center=(
                random.randint(0, Game.WIDTH-10), random.randint(0, Game.HEIGHT-10)
            ))
            while pygame.sprite.spritecollideany(self, platforms):
                self.surf = pygame.Surface((random.randint(50, 120), 20))
                self.surf.fill((230, 43, 28))
                self.rect = self.surf.get_rect(center=(
                    random.randint(0, Game.WIDTH-10), random.randint(0, Game.HEIGHT-10)
                ))
            if random.randint(0,1):
                self.xvel = random.randint(-10, 10) / 5

    def move(self):
        self.rect.x += self.xvel
        if self.rect.x > Game.WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = Game.WIDTH

class Player(pygame.sprite.Sprite):
    ACC = 1
    def __init__(self):
        super().__init__() # Sprite osztály konstruktorát hívja meg
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((123, 34, 200))
        self.rect = self.surf.get_rect(center=(200, 0))

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