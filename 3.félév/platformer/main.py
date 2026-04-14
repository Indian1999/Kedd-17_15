import pygame

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
        
        pygame.display.update()

    def run(self):
        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.main_platform = Platform()
        self.all_sprites.add(self.main_platform)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.main_platform)

        while True:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.player.move(self.platforms)
            
            self.draw_frame()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((Game.WIDTH, 20))
        self.surf.fill((230, 43, 28))
        self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT-10))

class Player(pygame.sprite.Sprite):
    ACC = 0.5
    def __init__(self):
        super().__init__() # Sprite osztály konstruktorát hívja meg
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((123, 34, 200))
        self.rect = self.surf.get_rect(center=(200, 0))

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
        if hits:
            self.pos.y = hits[0].rect.top
            self.vel.y = 0
            self.jumping = False
        self.rect.bottomleft = self.pos

    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15



game = Game()
game.run()