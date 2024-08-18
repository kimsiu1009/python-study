import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))
color = (255, 255, 0)

screen.fill(color)
# pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()


running = True
color = "red"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




pygame.quit()