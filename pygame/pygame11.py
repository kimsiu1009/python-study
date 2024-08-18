
from tkinter import CENTER
from numpy import number
import pygame
from random import *

# 레벨
def setup(level): # 레벨 당 숫자 개수

    # 얼마동안 시간을 보여줄지
    global display_time
    display_time = 5 - (level//3)
    display_time = max(display_time, 1) # 최소 1초

    number_count = (level//3) + 5
    number_count = min(number_count, 20) # 최대 숫자 20

    shuffle_grid(number_count)

# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5 # 줄이 5행
    colums = 9 # 칸이 9개

    cell_size = 130 # 각 Grid cell 별 가로 세로 크기
    button_size = 110 # Gird cell 내 그려질 버튼 크기
    screen_left_margin = 55
    screen_top_margin = 20


    grid = [[0 for col in range(colums)] for row in range(rows)]

    number = 1 # 시작 숫자부터 number_count까지
    while number <= number_count:
        row_idx = randrange(0, rows) # 0~4까지 랜덤으로 뽑기
        col_idx = randrange(0, colums) # 0~8까지 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number # 숫자 지정
            number += 1

            # 현재 그리드 cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size/2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size/2)

            # x, y 위치에 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


# 시작 화면
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

    msg = game_font.render("{0}".format(curr_level), True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)

# 게임 화면
def dispaly_game_screen(): # 게임 화면 표시

    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> sec
        if elapsed_time >= display_time:
            hidden = True


    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 그리드 내 숫자 그리기
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)



# pos 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() # 타이머 시작



def check_number_buttons(pos):
    global hidden, start, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
            break
    
    # 레벨 클리어 했을 경우
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

# 게임 종료 처리
def game_over():
    global running
    msg = game_font.render("Your level is {0}".format(curr_level), True, YELLOW)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    running = False
    

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height-120)

# 색상
BLACK = (0, 0, 0) # Black
WHITE = (255, 255, 255) # White
GRAY = (50, 50, 50) # Gray
YELLOW = (255, 255, 0) # YELLOW

# 현재 레벨
curr_level = 1

# 숫자를 보여주는 시간
display_time = None # 숫자를 보여주는 시간
start_ticks = None # 시간 계산

# 플레이어가 눌러야 할 버튼 리스트
number_buttons = []

# 게임 시작 여부
start = False

# 숫자 숨김 여부
hidden = False

# 게임 시작 전 함수 수행
setup(curr_level)

# 루프
running = True
while running:
    click_pos = None

# 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            
    # 화면 전체를 까맣게
    screen.fill(BLACK)

    if start == True:
        dispaly_game_screen() # 게임 화면 표시
    else:
        display_start_screen() # 게임 시작 화면

    # 사용자가 클릭한 좌표 값이 있다면
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()


# 종료 전 딜레이
pygame.time.delay(1000)

# 게임 종료
pygame.quit()