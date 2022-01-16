import time

import pygame
import random

import numbers

pygame.font.init()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scr):
        for x in range(self.width):
            for y in range(self.height):
                x1 = self.left + x * self.cell_size
                y1 = self.top + y * self.cell_size
                size = self.cell_size
                pygame.draw.rect(scr, 'white', (x1, y1, size, size))
                pygame.draw.rect(scr, 'black', (x1 + 1, y1 + 1, size - 2, size - 2))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)

    def get_cell(self, coords):
        if coords[0] in range(self.left, self.left + self.width * self.cell_size) and \
                coords[1] in range(self.top, self.top + self.height * self.cell_size):
            return (coords[0] - self.left) // self.cell_size, (coords[1] - self.top) // self.cell_size

        return None


class Minesweeper(Board):
    def __init__(self, width, height, mines):
        self.mines = mines
        self.locked = False
        super().__init__(width, height)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scr):
        for x in range(self.width):
            for y in range(self.height):
                x1 = self.left + x * self.cell_size
                y1 = self.top + y * self.cell_size
                size = self.cell_size
                pygame.draw.rect(scr, 'white', (x1, y1, size, size))

                pygame.draw.rect(scr, 'black', (x1 + 1, y1 + 1, size - 2, size - 2))

    def get_click(self, mouse_pos, r=False):
        if not self.locked:
            cell = self.get_cell(mouse_pos)
            self.open_cell(cell, r) if cell else None

    def open_cell(self, coords, r):
        x2, y2 = coords[0], coords[1]
        cell = self.board[y2][x2]
        if r and cell.__class__.__name__ == 'Block':
            self.board[y2][x2] = numbers.Flag(self.board[y2][x2].rect.x,
                                              self.board[y2][x2].rect.y)
            return
        if r and cell.__class__.__name__ == 'Mine':
            self.board[y2][x2] = numbers.FakeFlag(self.board[y2][x2].rect.x,
                                                  self.board[y2][x2].rect.y)
            return
        if r:
            return
        if cell.__class__.__name__ == 'Empty':
            return
        if cell.__class__.__name__ == 'Mine':
            for i in numbers.mine_group:
                i.update()
            for i in numbers.flag_group:
                i.update()
            self.locked = True
            return
        if cell.__class__.__name__ == 'Block':
            self.board[y2][x2] = numbers.getting_change(self.count_neighbours(x2, y2),
                                                        self.board[y2][x2].rect.x,
                                                        self.board[y2][x2].rect.y)

        if self.board[y2][x2].__class__.__name__ == 'Empty':
            round_ = self.find_neighbours((x2, y2))
            for i in round_:
                k = i
                self.open_cell((i[1], i[0]))

    def count_neighbours(self, x, y):
        if x == 0 and y == 0:
            return len(list(filter(lambda z: z.__class__.__name__ == 'Mine',
                                   [self.board[1][0], self.board[0][1], self.board[1][1]])))

        if x == 0 and y == self.height - 1:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine',
                                    [self.board[y - 1][0], self.board[y][1], self.board[y - 1][1]]))))

        if x == self.width - 1 and y == 0:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine',
                                    [self.board[1][x], self.board[0][x - 1], self.board[1][x - 1]]))))

        if x == self.width - 1 and y == self.height - 1:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine',
                                    [self.board[y - 1][x], self.board[y - 1][x - 1], self.board[y][x - 1]]))))

        if x == 0:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine', [self.board[y - 1][x],
                                                                               self.board[y + 1][x],
                                                                               self.board[y - 1][x + 1],
                                                                               self.board[y][x + 1],
                                                                               self.board[y + 1][x + 1]]))))

        if x == self.width - 1:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine', [self.board[y - 1][x],
                                                                               self.board[y + 1][x],
                                                                               self.board[y - 1][x - 1],
                                                                               self.board[y][x - 1],
                                                                               self.board[y + 1][x - 1]]))))

        if y == 0:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine', [self.board[y][x - 1],
                                                                               self.board[y][x + 1],
                                                                               self.board[y + 1][x - 1],
                                                                               self.board[y + 1][x],
                                                                               self.board[y + 1][x + 1]]))))

        if y == self.height - 1:
            return len(list((filter(lambda z: z.__class__.__name__ == 'Mine', [self.board[y][x - 1],
                                                                               self.board[y][x + 1],
                                                                               self.board[y - 1][x - 1],
                                                                               self.board[y - 1][x],
                                                                               self.board[y - 1][x + 1]]))))

        return len(list((filter(lambda z: z.__class__.__name__ == 'Mine', [self.board[y - 1][x],
                                                                           self.board[y - 1][x + 1],
                                                                           self.board[y][x + 1],
                                                                           self.board[y + 1][x + 1],
                                                                           self.board[y + 1][x],
                                                                           self.board[y + 1][x - 1],
                                                                           self.board[y][x - 1],
                                                                           self.board[y - 1][x - 1]]))))

    def find_neighbours(self, coords):
        x2, y2 = coords[0], coords[1]

        if x2 == 0 and y2 == 0:
            return [(1, 0), (0, 1), (1, 1)]

        elif x2 == 0 and y2 == self.height - 1:
            return [(y2 - 1, 0), (y2, 1), (y2 - 1, 1)]

        elif x2 == self.width - 1 and y2 == 0:
            return [(1, x2), (0, x2 - 1), (1, x2 - 1)]

        elif x2 == self.width - 1 and y2 == self.height - 1:
            return [(y2 - 1, x2), (y2 - 1, x2 - 1), (y2, x2 - 1)]

        elif x2 == 0:
            return [(y2 - 1, x2), (y2 + 1, x2), (y2 - 1, x2 + 1), (y2, x2 + 1), (y2 + 1, x2 + 1)]

        elif x2 == self.width - 1:
            return [(y2 - 1, x2), (y2 + 1, x2), (y2 - 1, x2 - 1), (y2, x2 - 1), (y2 + 1, x2 - 1)]

        elif y2 == 0:
            return [(y2, x2 - 1), (y2, x2 + 1), (y2 + 1, x2 - 1), (y2 + 1, x2), (y2 + 1, x2 + 1)]

        elif y2 == self.height - 1:
            return [(y2, x2 - 1), (y2, x2 + 1), (y2 - 1, x2 - 1), (y2 - 1, x2), (y2 - 1, x2 + 1)]

        else:
            return [(y2 - 1, x2), (y2 - 1, x2 + 1), (y2, x2 + 1), (y2 + 1, x2 + 1), (y2 + 1, x2),
                    (y2 + 1, x2 - 1), (y2, x2 - 1), (y2 - 1, x2 - 1)]

    def start(self):
        for m in range(self.mines):
            x1 = random.randint(0, self.width - 1)
            y1 = random.randint(0, self.height - 1)

            while True:
                x1 = random.randint(0, self.width - 1)
                y1 = random.randint(0, self.height - 1)

                if self.board[y1][x1].__class__.__name__ != 'Block' or self.board[y1][x1] == -1:
                    break

            x2 = self.left + x1 * self.cell_size
            y2 = self.top + y1 * self.cell_size

            self.board[y1][x1] = numbers.Mine(x2, y2)

        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x].__class__.__name__ == 'Mine':
                    continue
                x1 = self.left + x * self.cell_size
                y1 = self.top + y * self.cell_size
                self.board[y][x] = numbers.Block(x1, y1)
