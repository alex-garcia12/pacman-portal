import pygame
from pygame.sprite import Sprite

class Pinky(Sprite):
    def __init__(self, screen, ai_settings):
        super(Pinky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/pinkyH-1.png'))
        self.images.append(pygame.image.load('images/pinkyH-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
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