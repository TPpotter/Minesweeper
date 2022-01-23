import os
import random
import sys

import pygame

screen_rect = (0, 0, 1000, 800)


def load_image(name):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    return image


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]

    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(part_sprite)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = 1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 50
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


part_sprite = pygame.sprite.Group()
boom_sprite = pygame.sprite.Group()


class Boom(pygame.sprite.Sprite):
    fire = load_image("boom.png")

    def __init__(self, pos):
        super().__init__(boom_sprite)
        self.image = Boom.fire
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = pos

    def update(self):
        if self.image.get_width() - 10 <= 10 or self.image.get_height() - 10 <= 10:
            self.kill()

        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() - 10,
             self.image.get_height() - 10)
        )
        self.rect.x += 5
        self.rect.y += 5

# size = width, height = 1000, 800
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # создаём частицы по щелчку мыши
#             for i in range(100, 850, 100):
#                 create_particles((i, 10))
#                 create_particles((i, 100))
#
#     part_sprite.update()
#     screen.fill((0, 0, 0))
#     part_sprite.draw(screen)
#     pygame.display.flip()
#     clock.tick(50)
#
# pygame.quit()
