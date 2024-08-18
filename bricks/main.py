import pygame
import random

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("BRICKS BREAKING")

# 배경 사이즈
size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]

# 패달 사이즈, 좌표
size_width_pedal = 100
size_height_pedal = 15

# pedal을 화면의 가운데
x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
y_pos_pedal = size_height_bg - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_width_pedal, 
size_height_pedal)

# pedal을 움직임 (x좌표값)

to_x_pedal = 0

# 공의 사이즈, 좌표

size_radius_ball = 20
x_pos_ball = size_width_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball * 
2, size_radius_ball * 2)
rect_ball.center = (x_pos_ball, y_pos_ball)

# 공의 방향과 스피드를 결정하는 변수

x_speed_ball = 0.1
y_speed_ball = 0.1

# Block 사이즈, 좌표

size_width_block = size_width_bg // 10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for _ in range(10)] 
color_block = [[] for _ in range(10)] 

for i in range(10):
    for j in range(3):
        rect_block[i].append(pygame.Rect(i * size_width_block,
        j * size_height_block, size_width_block, size_height_block))
        color_block[i].append((random.randrange(255), random.randrange
        (150, 255), random.randrange(150, 255)))

# mouse 좌표 패달 움직임

x_pos_mouse, y_pos_mouse = 0, 0

# 점수 계산

point = 0

# 시작 변수

start = True

# 글짜 쓰기

def game_text(word):
    font = pygame.font.SysFont(None, 100)
    text = font.render(word, True, (0, 255, 255))
    size_width_text = text.get_rect().size[0]
    size_height_text = text.get_rect().size[1]

    x_pos_text = size_width_bg / 2 - size_width_text / 2
    y_pos_text = size_height_bg / 2 - size_height_text / 2

    background.blit(text, (x_pos_text, y_pos_text))

# gameover 판정변수

gameover = False

# gameloop

play = True
while play:

    # clock

    if start:
        start = False
        for i in range(3, 0, -1):
            background.fill((255, 255, 255))
            game_text(str(i))
            pygame.display.update()
            pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        # mouse로 pedal move

        if event.type == pygame.MOUSEMOTION:
            x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()

            # pedal = 화면밖으로 못 나가게

            if x_pos_mouse - size_width_pedal // 2 >=  0 and x_pos_mouse + size_width_pedal // 2 <= size_width_bg:
                x_pos_pedal = x_pos_mouse - size_width_pedal // 2
                rect_pedal.left = x_pos_mouse - size_width_pedal // 2

    # 배경색
    background.fill((255, 255, 255))

    # pedal
    pygame.draw.rect(background, (90, 255, 255), rect_pedal)

    # 공 좌표

    if x_pos_ball - size_radius_ball <= 0:
        x_speed_ball = -x_speed_ball
    elif x_pos_ball >= size_width_bg - size_radius_ball:
        x_speed_ball = -x_speed_ball

    if y_pos_ball - size_radius_ball <= 0:
        y_speed_ball = -y_speed_ball
    elif y_pos_ball >= size_height_bg - size_radius_ball:
        background.fill((255, 255, 255))
        game_text("GAME OVER")
        pygame.display.update()
        pygame.time.delay
        break

    # 광 좌표 speed값 누적

    x_pos_ball += x_speed_ball
    y_pos_ball += y_speed_ball

    rect_ball.center = (x_pos_ball, y_pos_ball)

    # 공
    pygame.draw.circle(background, (255, 0, 255), (x_pos_ball, y_pos_ball)
    , size_radius_ball)

    # 공이 pedal에 닿을 때
    if rect_ball.colliderect(rect_pedal):
        y_speed_ball = -y_speed_ball

    # block

    for i in range(10):
        for j in range(3):
            if rect_block[i][j]:
                pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                rect_block[i][j].topleft = (i * size_width_block,
                j * size_height_block)

                # 공 벽돌 충돌
                if rect_ball.colliderect(rect_block[i][j]):
                    x_speed_ball = -x_speed_ball
                    y_speed_ball = -y_speed_ball
                    rect_block[i][j] = 0
                    PendingDeprecationWarning("tlan")
                    # score up
                    point += 1

    if point == 30:
        background.fill((255, 255, 255)) 
        game_text("GAME CLEAR")
        pygame.display.update()
        pygame.time.delay(2000)
        play = False

    pygame.display.update()

pygame.quit()