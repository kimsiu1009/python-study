import pygame 

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey-Banana")

x_pos = 0
y_pos = 0

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.MOUSEMOTION:
            # mouse가 클릭된 죄표값을 언펙킹해서, x_pos, y_pos에 할당한다.
            x_pos, y_pos = pygame.mouse.get_pos()
            pygame.draw.circle(background, (255, 0, 255), (x_pos, y_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                background.fill((0, 0, 0))

    pygame.display.update()
        

pygame.quit()