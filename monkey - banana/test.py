import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey banana")
# 폰트 가져오기

font_test = pygame.font.SysFont(None, 30)

play= True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    text = font_test.render("monkey banana", True,(255, 255, 255))
    background.blit(text , (100, 100))
    pygame.display.update()

pygame.quit()