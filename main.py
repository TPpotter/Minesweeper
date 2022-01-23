import cboard
import pygame
import numbers
import start
import particles

info = [9, 9, 16, 1]
pygame.font.init()
pygame.init()
CHOOSE = [[9, 9, 16, 1], [12, 12, 27, 2], [16, 16, 40, 3], [20, 20, 70, 4], [25, 20, 100, 5], [30, 16, 99, 6]]
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
start_running = True


def main_menu():
    global screen, board
    screen.fill((0, 0, 0))
    board = ''

    for i in numbers.block_group:
        i.kill()
    for i in numbers.mine_group:
        i.kill()

    start.draw(screen)
    global info, start_running
    while start_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_running = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if x in range(390, 750) and y in range(240, 295):
                    info = [31, 25, 300, 10]
                    screen.fill((100, 100, 100))
                    start.end_start = True
                    start_running = False
                    break

                for i in start.buttons_sizes:
                    if x in range(10, 280) and y in i:
                        info = CHOOSE[start.buttons_sizes.index(i)]
                        screen.fill((100, 100, 100))
                        start.end_start = True
                        start_running = False
                        break

            if not start.end_start:
                start.draw(screen)
        pygame.display.flip()
    runtime()


def runtime():
    global board, screen, boom, win
    board = cboard.Minesweeper(info[0], info[1], info[2])
    board.set_view(start.choose(info[3])[0], start.choose(info[3])[1], 30)
    boom = True
    win = False
    board.start()

    pygame.draw.rect(screen, 'red', (950, 760, 50, 40), 5)

    return


board = cboard.Minesweeper(info[0], info[1], info[2])
main_menu()
running = True
clock = pygame.time.Clock()
pygame.init()
boom = True
win = False

while running:
    pygame.draw.rect(screen, 'red', (950, 760, 49, 38))
    pygame.display.update()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(950, 1000) and event.pos[1] in range(760, 800):
                main_menu()
                start_running = True
                start.end_start = False

            if pygame.mouse.get_pressed()[0]:
                board.get_click(event.pos)

            if pygame.mouse.get_pressed()[2]:
                board.get_click(event.pos, r=True)

        win = True

        for cell in numbers.block_group:
            if cell.__class__.__name__ == 'Block':
                win = False
                break

        if win and not board.locked:
            sound1 = pygame.mixer.Sound('sound/win_sound.mp3')
            sound1.play()
            win = True

            for i in range(100, 850, 150):
                particles.create_particles((i, 10))

            while particles.part_sprite:
                particles.part_sprite.update()
                particles.part_sprite.draw(screen)
                pygame.display.flip()
                pygame.display.update()
                clock.tick(60)

            print('YOU WIN')
            board.locked = True

        if board.locked and boom and not win:
            boom = False
            sound2 = pygame.mixer.Sound('sound/boom_sound.mp3')
            sound2.play()
            print('YOU LOSE')

            bomb = particles.Boom((200, 150))

            while particles.boom_sprite:
                particles.boom_sprite.draw(screen)
                pygame.display.flip()
                pygame.display.update()
                particles.boom_sprite.update()
                clock.tick(60)

    screen.fill((200, 200, 200))
    board.render(screen)
    numbers.block_group.draw(screen)
    numbers.mine_group.draw(screen)
