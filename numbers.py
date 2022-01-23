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


class Two(pygame.sprite.Sprite):
    image = load_image('two.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Two.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Three(pygame.sprite.Sprite):
    image = load_image('three.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Three.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Four(pygame.sprite.Sprite):
    image = load_image('four.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Four.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_flag = False


class Five(pygame.sprite.Sprite):
    image = load_image('five.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Five.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_flag = False


class Six(pygame.sprite.Sprite):
    image = load_image('six.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Six.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Seven(pygame.sprite.Sprite):
    image = load_image('seven.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Seven.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Eight(pygame.sprite.Sprite):
    image = load_image('eight.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Eight.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Block(pygame.sprite.Sprite):
    image = load_image('block.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Block.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_flag = False

    def update(self, r=False, end=False):
        if r:
            self.is_flag = not self.is_flag

        if self.is_flag and not end:
            self.image = Flag.image

        if self.is_flag and end:
            self.image = FakeFlag.image

        if not self.is_flag:
            self.image = Block.image


class Empty(pygame.sprite.Sprite):
    image = load_image('empty.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y):
        super().__init__(block_group)

        self.image = Empty.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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
        self.is_flag = False

    def update(self, r=False, end=False):
        if r:
            self.is_flag = not self.is_flag
        if not self.is_flag and end:
            self.image = Mine.image
        if self.is_flag:
            self.image = Flag.image
        if not self.is_flag and not end:
            self.image = Mine.image_open


class Flag(pygame.sprite.Sprite):
    image = load_image('flagged.png')
    image = pygame.transform.scale(image, (30, 30))


class FakeFlag(pygame.sprite.Sprite):
    image = load_image('fake_flag.png')
    image = pygame.transform.scale(image, (30, 30))


block_group = pygame.sprite.Group()
mine_group = pygame.sprite.Group()



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
