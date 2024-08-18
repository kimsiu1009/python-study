# pygame library를 import 한다.
import pygame

# pygame library를 초기화 한다.
pygame.init()

# pygame window
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey likes banana")

fps = pygame.time.Clock()

# x, y 좌표값은 정수로 나타내기 위해서 //을 사용한다.
x_pos = background.get_size()[0] // 2
print(x_pos)
y_pos = background.get_size()[1] // 2
print(y_pos)

to_x = 0 
to_y = 0 

# game loop
running = True
while running:

    delaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -1
                print('up')
            elif event.key == pygame.K_DOWN:
                print("Down")
                to_y = 1
            elif event.key == pygame.K_LEFT:
                print("Left")
                to_x = -1
            elif event.key == pygame.K_RIGHT:
                print("Right")
                to_x = 1
        if event.type == pygame.KEYUP:
            to_x = 0
            to_y = 0

    x_pos += to_x
    y_pos += to_y

    # 배경 색깔
    background.fill((255, 0, 0))
    # 원
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.display.update()

# pygame을 종료한다.
pygame.quit()