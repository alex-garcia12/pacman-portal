import pygame
from pygame.sprite import Sprite

class Pacman(Sprite):
    def __init__(self, screen, ai_settings):
        super(Pacman, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/pacmanH-1.png'))
        self.images.append(pygame.image.load('images/pacmanH-2.png'))
        self.images.append(pygame.image.load('images/pacmanV-1.png'))
        self.images.append(pygame.image.load('images/pacmanV-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.orientation = "Left"

        self.rect.center = self.screen_rect.center
        #self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.image = self.images[self.index]
            self.rect.centerx += self.ai_settings.pacman_speed

        if self.moving_left and self.rect.left > 0:
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.image = self.images[self.index]
            self.rect.centerx -= self.ai_settings.pacman_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.index += 1
            if self.index > 3:
                self.index = 2
            self.image = self.images[self.index]
            self.rect.centery -= self.ai_settings.pacman_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.index += 1
            if self.index > 3:
                self.index = 2
            self.image = self.images[self.index]
            self.rect.centery += self.ai_settings.pacman_speed
        # self.rect.centerx = self.center

    def blitme(self):
        if self.orientation == "Right":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        elif self.orientation == "Left":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Up":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Down":
            self.screen.blit(pygame.transform.flip(self.image, False, True), self.rect)


    def center_pacman(self):
        self.center = self.screen_rect.center