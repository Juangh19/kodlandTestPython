import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))  
        self.image.fill((255, 255, 255))  
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)