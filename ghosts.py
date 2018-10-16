import pygame
from pygame.sprite import Sprite

class Pinky(Sprite):
    def __init__(self, ai_settings, screen):
        super(Pinky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/pinky.png'))
        self.images.append(pygame.image.load('images/blinky1.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        self.x += 1
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)