import pygame
from modules.player import Player
from modules.enemy import Enemy
from modules.bullet import Bullet

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Shooter")

        self.clock = pygame.time.Clock()
        self.running = True

        self.game_over_state = False

        self.player = Player(self.width // 2, self.height - 50)
        self.enemies = []

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        if self.game_over_state and keys[pygame.K_SPACE]:
            self.reset_game()

    def update(self):
        if not self.game_over_state: 
            self.player.update()

            if pygame.time.get_ticks() % 100 == 0:
                enemy = Enemy(pygame.time.get_ticks() % self.width, 0)
                self.enemies.append(enemy)

            for bullet in self.player.bullets:
                for enemy in self.enemies:
                    if bullet.rect.colliderect(enemy.rect):
                        
                        self.enemies.remove(enemy)

            for enemy in self.enemies:
                enemy.update()

                if enemy.rect.y > self.height:
                    self.game_over_state = True  

    def game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over - Press SPACE to restart", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

    def reset_game(self):
        self.game_over_state = False
        self.player = Player(self.width // 2, self.height - 50)
        self.enemies = []

    def render(self):
        self.screen.fill((200, 200, 200))
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        if self.game_over_state:
            self.game_over()

        pygame.display.flip()