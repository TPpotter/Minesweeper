import os
import sys

import pygame


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


class One(pygame.sprite.Sprite):
    image = load_image('one.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = One.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = One.image


class Two(pygame.sprite.Sprite):
    image = load_image('two.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Two.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Two.image


class Three(pygame.sprite.Sprite):
    image = load_image('three.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Three.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Three.image


class Four(pygame.sprite.Sprite):
    image = load_image('four.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Four.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Four.image


class Five(pygame.sprite.Sprite):
    image = load_image('five.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Five.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Five.image


class Six(pygame.sprite.Sprite):
    image = load_image('six.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Six.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Six.image


class Seven(pygame.sprite.Sprite):
    image = load_image('seven.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Seven.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Seven.image


class Eight(pygame.sprite.Sprite):
    image = load_image('eight.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Eight.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Eight.image


class Block(pygame.sprite.Sprite):
    image_open = load_image('block.png')
    image_open = pygame.transform.scale(image_open, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Block.image_open
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Empty(pygame.sprite.Sprite):
    image = load_image('empty.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Empty.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Empty.image


class Mine(pygame.sprite.Sprite):
    image_open = load_image('block.png')
    image_open = pygame.transform.scale(image_open, (30, 30))
    image = load_image('mine.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(mine_group)

        self.image = Mine.image_open
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = Mine.image


class Flag(pygame.sprite.Sprite):
    image = load_image('flagged.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Flag.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FakeFlag(pygame.sprite.Sprite):
    image = load_image('flagged.png')
    image = pygame.transform.scale(image, (30, 30))

    image_load = load_image('fake_flag.png')
    image_load = pygame.transform.scale(image_load, (30, 30))

    def __init__(self, x, y):
        super().__init__(flag_group)

        self.image = FakeFlag.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = FakeFlag.image_load


block_group = pygame.sprite.Group()
mine_group = pygame.sprite.Group()
flag_group = pygame.sprite.Group()


def getting_change(n, x, y):
    if n == 1:
        return One(x, y)
    if n == 2:
        return Two(x, y)
    if n == 3:
        return Three(x, y)
    if n == 4:
        return Four(x, y)
    if n == 5:
        return Five(x, y)
    if n == 6:
        return Six(x, y)
    if n == 7:
        return Seven(x, y)
    if n == 8:
        return Eight(x, y)

    if n == 0:
        return Empty(x, y)
