import pygame
from imagerect import ImageRect


class Maze:
    RED = (255, 0, 0)
    # BRICK_SIZE = 13
    BRICK_SIZE = 25
    DOT_SIZE = 15
    PILL_SIZE = 20

    def __init__(self, screen, mazefile, brickfile, dotfile, powerpill):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.dots = []
        self.pills = []
        sz = Maze.BRICK_SIZE
        sz1 = Maze.DOT_SIZE
        sz2 = Maze.PILL_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.dot = ImageRect(screen, dotfile, sz1, sz1)
        self.pill = ImageRect(screen, powerpill, sz2, sz2)
        self.deltax = self.deltay = Maze.BRICK_SIZE
        self.dot_deltax = self.dot_deltay = Maze.DOT_SIZE
        self.pill_deltax = self.pill_deltay = Maze.PILL_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        d = self.dot.rect
        w, h = r.width, r.height
        w1, h1 = d.width, d.height
        dx, dy = self.deltax, self.deltay
        dx1, dy1 = self.dot_deltax, self.dot_deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'x':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.dots.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'P':
                    self.pills.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.dots:
            self.screen.blit(self.dot.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)