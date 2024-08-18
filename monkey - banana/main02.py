import pygame 

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey-Banana")

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.MOUSEMOTION:
            print("MOUSEMOTION")
            print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MOUSEBUTTONDOWN")
            print(pygame.mouse.get_pos())

            if event.button == 1:
                print("왼쪽 버튼 클릭")
            if event.button == 2:
                print("휠 버튼 클릭")
            if event.button == 3:
                print("오른쪽 버튼 클릭")
            if event.button == 3:
                print("휠 올리기")
            if event.button == 3:
                print("휠 내리기")

        if event.type == pygame.MOUSEBUTTONUP:
            print("MOUSEBUTTONUP")
            print(pygame.mouse.get_pos())

pygame.quit()