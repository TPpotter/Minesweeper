import pygame

pygame.font.init()


def choose(n):
    if n == 1:
        return 400, 200

    if n == 2:
        return 320, 220

    if n == 3:
        return 260, 160

    if n == 4:
        return 200, 100

    if n == 5:
        return 125, 100

    if n == 6:
        return 50, 200

    if n == 10:
        return 10, 10


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("9 x 9 (16 мин)", True, 'grey')
    text_x = 10
    text_y = 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'grey', (text_x - 10, text_y - 10,
                                      text_w + 20, text_h + 20), 1)

    text = font.render("12 x 12 (27 мин)", True, 'grey')
    text_x = 10
    text_y = 120
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'grey', (text_x - 10, text_y - 10,
                                      text_w + 20, text_h + 20), 1)

    text1 = font.render("16 x 16 (40 мин)", True, 'grey')
    text1_x = 10
    text1_y = 220
    text1_w = text1.get_width()
    text1_h = text1.get_height()
    screen.blit(text1, (text1_x, text1_y))
    pygame.draw.rect(screen, 'grey', (text1_x - 10, text1_y - 10,
                                      text1_w + 20, text1_h + 20), 1)

    text2 = font.render("20 x 20 (70 мин)", True, 'grey')
    text2_x = 10
    text2_y = 320
    text2_w = text2.get_width()
    text2_h = text2.get_height()
    screen.blit(text2, (text2_x, text2_y))
    pygame.draw.rect(screen, 'grey', (text2_x - 10, text2_y - 10,
                                      text2_w + 20, text2_h + 20), 1)

    text = font.render("25 x 20 (100 мин)", True, 'grey')
    text_x = 10
    text_y = 420
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'grey', (text_x - 10, text_y - 10,
                                      text_w + 20, text_h + 20), 1)

    text = font.render("30 x 16 (99 мин)", True, 'grey')
    text_x = 10
    text_y = 520
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'grey', (text_x - 10, text_y - 10,
                                      text_w + 20, text_h + 20), 1)

    font = pygame.font.Font(None, 60)
    text = font.render("31 x 25 (300 мин)", True, 'grey')
    text_x = 400
    text_y = 250
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'grey', (text_x - 10, text_y - 10,
                                      text_w + 20, text_h + 20), 1)


pygame.init()


end_start = False

buttons_sizes = [range(10, 60), range(120, 170), range(220, 270), range(320, 370), range(420, 470), range(520, 570)]
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#
#             for i in buttons_sizes:
#                 if x in range(10, 100) and y in i:
#                     print(buttons_sizes.index(i))
#                     screen.fill((100, 100, 100))
#                     end_start = True
#                     break
#
#     if not end_start:
#         draw(screen)
#     pygame.display.flip()
# pygame.quit()
