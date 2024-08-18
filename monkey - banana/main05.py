import pygame 

pygame.init()

background = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Monkey-Banana")

clock = pygame.time.Clock()

mousedown = False
mousepos = []



while True:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
        mousepos.clear()
    elif event.type == pygame.MOUSEMOTION:
        if mousedown:
            mousepos.append(event.pos)
            print(mousepos)

    background.fill((0, 0, 0))

    if len(mousepos) > 1:
        pygame.draw.lines(background, (255, 0, 0), False, mousepos)

    pygame.display.update()

pygame.quit()

        

pygame.quit()