#테트리스
"""

"""
import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

#색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PINK = (255, 0, 255)
PUPPLE = (153, 0, 153)

#격자 칸
GRID_SIZE = 50
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE

#x, y
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SPEED = 10


#블록 데이터
BLOCK_DATA = (((0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0), (0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0), (0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0), (0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0)),
              ((1,0,0,1,1,1,0,0,0), (0,1,1,0,1,0,0,1,0), (0,0,0,1,1,1,0,0,1), (0,0,1,0,0,1,0,1,1)),
              ((0,0,1,1,1,1,0,0,0), (0,1,0,0,1,0,0,1,1), (0,0,0,1,1,1,1,0,0), (1,1,0,0,1,0,0,1,0)),
              ((1,1,1,1), (1,1,1,1), (1,1,1,1), (1,1,1,1)),
              ((0,0,0,0,1,1,1,1,0), (0,1,0,0,1,1,0,0,1), (0,0,0,0,1,1,1,1,0), (0,1,0,0,1,1,0,0,1)),
              ((0,0,0,0,1,0,1,1,1), (1,0,0,1,1,0,1,0,0), (1,1,1,0,1,0,0,0,0), (0,0,1,0,1,1,0,0,1)),
              ((0,0,0,1,1,0,0,1,1), (0,1,0,1,1,0,1,0,0), (0,0,0,1,1,0,0,1,1), (0,1,0,1,1,0,1,0,0)))

#번호별 색상
COLOR_DATA = (RED, BLUE, GREEN, YELLOW, ORANGE, PINK, PUPPLE, WHITE)

#번호별 rect 선 굵기
RECT_LINE = (0,0,0,0,0,0,0,1)

#격자판
GRID = [[[-1] for x in range(int(GRID_WIDTH))] for x in range(int(GRID_HEIGHT))]


class Block(object):
    def __init__(self):
        self.position = [0,0]
        
    def create(self):
        self.data = random.randint(0,6)
        self.spin = random.randint(0,3)
        self.position[0] = random.randint(0, int(GRID_WIDTH) - 1)
        self.position[1] = -1
    
    def control(self, direction):
        y = self.position[1]
        x = self.position[0]
        
        if direction == DOWN:
            self.position[1] = y

        elif direction == LEFT:
            if x == 0:
                return
            self.position[0] -= 1
        
        elif direction == RIGHT:
            if x == int(GRID_WIDTH) - 1 :
                return
            self.position[0] += 1
        
    def move_y(self):
        self.position[1] += 1
        GRID[self.position[1]][self.position[0]][0] = self.data
        

    def get_pos(self):
        return self.position

    def turn(self):
        """
        회전 가능한지 확인
        """
        self.spin = (self.spin + 1) % 4

        

#박스가 위에서 아래로 이동할 때 이전 위치의 색상을 원상 복귀(검정)함
def remove_prev(position, direction):
    y = position[1]
    x = position[0]

    if y == -1:
        return

    if direction == DOWN:
        GRID[y][x][0] = -1

    elif direction == LEFT:
        if x == 0:
            return
        GRID[y][x][0] = -1
        
    elif direction == RIGHT:
        if x == int(GRID_WIDTH) - 1 :
            return
        GRID[y][x][0] = -1



def check_crash(position, direction):
    y = position[1]
    x = position[0]

    if direction == DOWN:
        if y == int(GRID_HEIGHT) - 1: #맨 아랫줄
            return True

        next_block_data = GRID[y+1][x][0]
        
    elif direction == LEFT:
        if x == 0: #왼쪽 가장자리
            return True
        
        next_block_data = GRID[y+1][x-1][0]
        
    elif direction == RIGHT:
        if x == int(GRID_WIDTH) - 1: #오른쪽 가장자리
            return True
        
        next_block_data = GRID[y+1][x+1][0]

    if next_block_data != -1:
        return True
        
    return False


#하단 줄이 모두 메워졌을 경우 라인 삭제
def under_line():
    global GRID
    beRemove = True
    
    y = int(GRID_HEIGHT) - 1
    
    for x in range(int(GRID_WIDTH)):
        num = GRID[y][x][0]
        if num == -1:
            beRemove = False

    if beRemove == True:
        GRID.pop()
        new_line = [[-1] for x in range(int(GRID_WIDTH))]
        GRID.insert(0, new_line)



def main():
    global SCREEN, SURFACE, GRID
    
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    
    pygame.init()
    SURFACE = pygame.Surface(SCREEN.get_size())
    SCREEN.fill(BLACK)
    clock = pygame.time.Clock()

    block = Block()

    block.create()
    
    while True:
        SCREEN.fill(BLACK)
        
        #키 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    remove_prev(block.get_pos(), DOWN)
                    block.control(DOWN)
                elif event.key == K_LEFT:
                    if check_crash(block.get_pos(), LEFT) == True:
                        break;
                    remove_prev(block.get_pos(), LEFT)
                    block.control(LEFT)
                elif event.key == K_RIGHT:
                    if check_crash(block.get_pos(), RIGHT) == True:
                        break;
                    remove_prev(block.get_pos(), RIGHT)
                    block.control(RIGHT)
        
        
        if check_crash(block.get_pos(), DOWN) == True:
            block.create()
        else:
            remove_prev(block.get_pos(), DOWN)
            block.move_y()
            
        
        #GRID 로부터 판 생성
        for x in range(int(GRID_WIDTH)):
            for y in range(int(GRID_HEIGHT)):
                num = GRID[y][x][0]
                rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(SCREEN, COLOR_DATA[num], rect, RECT_LINE[num])

        under_line()
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(SPEED)

main()