import pygame
from pygame.locals import *
from modules.bullet import Bullet

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

        self.bullets = []

    def handle_input(self, keys):
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 800 - self.rect.width:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600 - self.rect.height:
            self.rect.y += self.speed
        if keys[K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        self.bullets.append(bullet)

        self.bullets = [bullet for bullet in self.bullets if bullet.rect.y > 0]

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

        for bullet in self.bullets:
            bullet.draw(screen)

    