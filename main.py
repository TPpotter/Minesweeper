import cboard
import pygame
import numbers

info = 0


size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
board = cboard.Minesweeper(31, 25, 300)
board.set_view(10, 10, 30)
board.start()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                board.get_click(event.pos)
            if pygame.mouse.get_pressed()[2]:
                board.get_click(event.pos, r=True)

    screen.fill((200, 200, 200))
    board.render(screen)
    numbers.block_group.draw(screen)
    numbers.mine_group.draw(screen)
    numbers.flag_group.draw(screen)
    pygame.display.update()
    pygame.display.flip()
