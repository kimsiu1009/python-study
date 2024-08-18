import pygame

pygame.init()

background = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Monkey-Banana")

x = background.get_size()[0] // 2
y = background.get_size()[1] // 2

play = True

while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.fill((255, 255, 255))

    pygame.draw.circle(background, (5, 45, 67), (240, 180), 50, 5)
    pygame.draw.rect(background, (5, 45, 67), (240, 180, 100, 50), 5)
    pygame.draw.ellipse(background, (5, 45, 67), (240, 180, 100, 50), 5)

    pygame.display.update()

pygame.quit()