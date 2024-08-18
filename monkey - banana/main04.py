import pygame 

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey-Banana")

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2


play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.MOUSEMOTION:
            # mouse가 클릭된 죄표값을 언펙킹해서, x_pos, y_pos에 할당한다.
            x_pos, y_pos = pygame.mouse.get_pos()
    background.fill((0, 0, 0))
    pygame.draw.circle(background, (255, 0, 255), (x_pos, y_pos), 10)

    pygame.display.update()
        

pygame.quit()