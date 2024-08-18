import pygame, random

pygame.init()

# 게임화면 설정
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("지렁이 게임")

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 지렁이 초기 설정
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)

# 메시지 출력 함수
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# 게임 루프
def gameLoop():
    game_over = False
    game_close = False
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # 먹이 생성 함수
    def food():
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

    # 지렁이 생성 함수
    def snake(snake_block, snake_List):
        for x in snake_List:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

    while not game_over:

        while game_close == True:
            screen.fill(white)
            message("게임이 끝났습니다. 다시 하려면 Q를, 종료하려면 X를 누르세요.", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameLoop()
                    elif event.key == pygame.K_x:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 지렁이 이동
        x1 += x1_change
        y1 += y1_change

        # 벽 충돌 검사
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # 지렁이 그리기
        screen.fill(white)
        
        # 먹이 먹기
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # 지렁이 길이 추가
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 지렁이 충돌 검사
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # 지렁이와 먹이 그리기
        snake(snake_block, snake_List)
        food()
        pygame.display.update()

        # 게임 속도 설정
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # 게임 종료
    pygame.quit()
    quit()

# 게임 실행
gameLoop()