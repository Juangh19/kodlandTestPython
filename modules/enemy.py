import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)