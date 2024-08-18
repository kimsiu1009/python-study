import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

running = True
color = "red"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(color)
    pygame.display.flip()

    if color == "red":
        print(color)
        color = "green"
    else:
        print(color)
        color = "red"

pygame.quit()