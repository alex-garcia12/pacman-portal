import sys
import pygame

def check_keydown_events(event, pacman):
    if event.key == pygame.K_RIGHT:                                 #if the right arrow key is pressed...
        pacman.moving_right = True                                    #Set the flag = true to get the ship to move right
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_UP:                                 #if the right arrow key is pressed...
        pacman.moving_up = True                                    #Set the flag = true to get the ship to move right
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True
    #elif event.key == pygame.K_SPACE:                                #when spacebar is pressed...
        #fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

# def check_keyup_events(event, pacman):