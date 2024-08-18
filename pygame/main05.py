import pygame

pygame.init()

surface = pygame.display.set_mode((400, 300))
color = (0, 0, 0)

surface.fill(color)

pygame.display.flip()
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
pygame.quit()