import sys
import pygame


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return

    @staticmethod
    def check_events(pacman):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event, pacman)
            if event.type == pygame.KEYUP:
                EventLoop.check_keyup_events(event, pacman)

    def check_keydown_events(event, pacman):
        if event.key == pygame.K_RIGHT:  # if the right arrow key is pressed...
            pacman.moving_right = True  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = True
        elif event.key == pygame.K_UP:  # if the right arrow key is pressed...
            pacman.moving_up = True  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = True
            # elif event.key == pygame.K_SPACE:                                #when spacebar is pressed...
            # fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(event, pacman):
        if event.key == pygame.K_RIGHT:  # if the right arrow key is pressed...
            pacman.moving_right = False  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = False
        elif event.key == pygame.K_UP:  # if the right arrow key is pressed...
            pacman.moving_up = False  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = False
