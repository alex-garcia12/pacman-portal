import sys
import pygame
from maze import Maze
from pacman import Pacman
from settings import Settings
from ghosts import Pinky
import game_functions as gf
from pygame.sprite import Group
from eventloop import EventLoop

class Game():
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        ai_settings = Settings()
        self.ai_settings = ai_settings

        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile = 'images/maze.txt', brickfile = 'brick',
                         portalfile = 'portal', shieldfile = 'shield', powerpill = 'powerpill')
        self.pacman = Pacman(self.screen, ai_settings)
        self.ghosts = Group()
        self.ghost = Pinky(self.screen, ai_settings)
        self.ghosts.add(self.ghost)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished = False)


        while not eloop.finished:
            eloop.check_events(self.pacman)
            self.update_screen()
            self.pacman.update()
            self.ghosts.update()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        # self.pacman.update()

        self.maze.blitme()
        self.pacman.blitme()
        self.ghosts.draw(self.screen)
        pygame.display.flip()

game = Game()
game.play()

# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Pacman Portal")


#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#             screen.fill(ai_settings.BLACK)
#
#             pygame.display.flip()
#
# run_game()