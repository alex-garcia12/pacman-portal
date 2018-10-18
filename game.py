import pygame
from maze import Maze
from pacman import Pacman
from ghosts import Pinky
from settings import Settings
from eventloop import EventLoop
from pygame.sprite import Group
from menu import Menu
import game_functions as gf


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        ai_settings = Settings()
        self.ai_settings = ai_settings
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("PacMan Portal")

        self.menu = Menu(self.screen, 'PAC-MAN')

        self.maze = Maze(self.screen, 'images/maze.txt', 'brick', 'dot', 'powerpill')

        self.pacman = Pacman(self.screen, self.ai_settings)
        self.ghost = Pinky(self.screen, self.ai_settings)
        self.ghosts = Group()
        self.ghosts.add(self.ghost)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(self.ai_settings.finished)

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu, self.pacman)
            self.update_screen()
            self.pacman.check_wall_collision(self.maze.bricks)
            self.pacman.update()
            self.ghosts.update()

    def update_screen(self):
        self.screen.fill(Game.BLACK)

        if not self.ai_settings.finished:
            self.menu.draw_menu()
        else:
            self.ghosts.draw(self.screen)
            self.maze.blitme()
            self.pacman.blitme()

        pygame.display.flip()


game = Game()
game.play()