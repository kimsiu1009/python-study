import pygame
from pygame.rect import *
import random

###################################################################
###################################################################
def restart():
    global isGameOver, score
    isGameOver = False
    score = 0
    for i in range(len(star)):
        recStar[i].y = -1    
###################################################################
###################################################################
def eventProcess():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_LEFT:
                move.x = -1
            if event.key == pygame.K_RIGHT:
                move.x = 1
            if event.key == pygame.K_UP:
                move.y = -1
            if event.key == pygame.K_DOWN:
                move.y = 1
            if event.key == pygame.K_r:
                restart()
###################################################################
###################################################################
def movePlayer():
    if not isGameOver:
        recPlayer.x += move.x
        recPlayer.y += move.y
    if recPlayer.x < 0:
        recPlayer.x = 0
    if recPlayer.x > SCREEN_WIDTH-recPlayer.width:
        recPlayer.x = SCREEN_WIDTH-recPlayer.width
    if recPlayer.y < 0:
        recPlayer.y = 0
    if recPlayer.y > SCREEN_HEIGHT-recPlayer.height:
        recPlayer.y = SCREEN_HEIGHT-recPlayer.height        
    SCREEN.blit(player, recPlayer)
###################################################################
###################################################################
def timeDelay500ms():
    global time_delay_500ms
    if time_delay_500ms > 5:
        time_delay_500ms = 0
        return True    
    time_delay_500ms += 1
    return False
    
def makeStar():
    if isGameOver:
        return
    if timeDelay500ms():
        idex = random.randint(0, len(star)-1)
        if recStar[idex].y == -1:
            recStar[idex].x = random.randint(0, SCREEN_WIDTH)
            recStar[idex].y = 0

def moveStar():
    makeStar()
    for i in range(len(star)):
        if recStar[i].y == -1:
            continue
        if not isGameOver:
            recStar[i].y += 1
        if recStar[i].y > SCREEN_HEIGHT:
            recStar[i].y = 0
        SCREEN.blit(star[i], recStar[i])
###################################################################
###################################################################
def CheckCollision():   
    global score, isGameOver
    if isGameOver:
        return
    for rec in recStar:
        if rec.y == -1:
            continue
        if rec.top < recPlayer.bottom \
            and recPlayer.top < rec.bottom \
            and rec.left < recPlayer.right \
            and recPlayer.left < rec.right:
            print('충돌')
            isGameOver = True
            break
    score += 1
###################################################################
###################################################################
def blinking():
    global time_dealy_4sec, toggle
    time_dealy_4sec += 1
    if time_dealy_4sec > 40:
        time_dealy_4sec = 0
        toggle = ~toggle    
    return toggle

def setText():
    mFont = pygame.font.SysFont("arial",20, True, False)
    SCREEN.blit(mFont.render(
        f'score : {score}', True, 'green'), (10, 10, 0, 0))

    if isGameOver and blinking():
        SCREEN.blit(mFont.render(
            'Game Over!!', True, 'red'), (150, 300, 0, 0))
        SCREEN.blit(mFont.render(
            'press R - Restart', True, 'red'), (140, 320, 0, 0))
###################################################################
###################################################################
#1.변수초기화
isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
move = Rect(0,0,0,0)
time_delay_500ms = 0
time_dealy_4sec = 0
toggle = False
score = 0
isGameOver = False

#2.스크린생성
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CodingNoew!!')

#3. player 생성
player = pygame.image.load('images/player.png')
player = pygame.transform.scale(player,(20,30))
recPlayer = player.get_rect()
recPlayer.centerx = (SCREEN_WIDTH/2)
recPlayer.centery = (SCREEN_HEIGHT/2)

#4. 유성 생성
star = [pygame.image.load('images/star.png') for i in range(40)]
recStar = [None for i in range(len(star))]
for i in range(len(star)):
    star[i] = pygame.transform.scale(star[i], (20, 20))
    recStar[i] = star[i].get_rect()
    recStar[i].y = -1
    
#5. 기타
clock = pygame.time.Clock()

#####반복####
while isActive:
    #1.화면 지움
    SCREEN.fill((0,0,0))
    #2.이벤트처리
    eventProcess()
    #3.플레이어 이동
    movePlayer()
    #4.유성 생성 및 이동
    moveStar()
    #5.충돌 확인
    CheckCollision()
    #6.text업데이트
    setText()
    #7.화면 갱신
    pygame.display.flip()
    clock.tick(100)

#########################################################
def restart():
    global score, isGameOver
    for i in range(len(star)):
        rectStar[i].y = -1
    score = 0
    isGameOver = False

def eventProcess(move):
    global isActive
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                isActive = False
            if event.key == pygame.K_LEFT:
                move.x = -1
            if event.key == pygame.K_RIGHT:
                move.x = 1
            if event.key == pygame.K_UP:
                move.y = -1
            if event.key == pygame.K_DOWN:
                move.y = 1
            if event.key == pygame.K_r:
                restart()
#########################################################
def movePlayer(player, current, move, isGameOver):
    global SCREEN_WIDTH, SCREEN_HEIGHT
    if not isGameOver:
        current.x += move.x
        current.y += move.y
#### limit
    if current.y > SCREEN_HEIGHT - current.height:
        current.y = SCREEN_HEIGHT - current.height
    if current.x > SCREEN_WIDTH-current.width:
        current.x = SCREEN_WIDTH - current.width
    if current.y < 0:
        current.y = 0
    if current.x < 0:
        current.x = 0
    SCREEN.blit(player, current)
#########################################################
def timeUpdate50ms():
    global time500ms
    time500ms += 1
    if time500ms > 5:
        time500ms = 0
        return True
    return False

def makeStar(rec):
    if timeUpdate50ms():
        idex = random.randint(0, len(star)-1)
        if rec[idex].y == -1:
            rec[idex].x = random.randint(0, SCREEN_WIDTH)
            rec[idex].y = 0

def moveStar(star, current, isGameOver):
    global SCREEN_HEIGHT
    for i in range(len(star)):    
        if current[i].y == -1:
            continue
        if not isGameOver:
            current[i].y += 1
        if current[i].y > SCREEN_HEIGHT:
            current[i].y = -1
        SCREEN.blit(star[i], current[i])
#########################################################
def CheckCollision(player, star):
    global isGameOver, score
    if isGameOver:
        return
    for rec in star:
        if rec.top < player.bottom \
                and player.top < rec.bottom \
                and rec.left < (player.right-8) \
                and (player.left+8) < rec.right:
            isGameOver = True
            break
    score += 1
#########################################################
def timeUpdate4sec(isGameOver):
    global time4Sec, time4SecToggle
    if not isGameOver:
        return False
    time4Sec += 1
    if time4Sec > 40:
        time4Sec = 0
        time4SecToggle = (~time4SecToggle)
    return time4SecToggle

def setText(isupdate=False):
    global score
    myFont = pygame.font.SysFont("arial", 20, True, False)

    SCREEN.blit(myFont.render(
        f'score : {score}', True, 'green'), (10, 10, 0, 0))

    if isupdate:
        SCREEN.blit(myFont.render(
            f'Game Over!!', True, 'red'), (150, 300, 0, 0))
        SCREEN.blit(myFont.render(
            f'press R - Restart', True, 'red'), (140, 320, 0, 0))
#########################################################
#########################################################


##1. 변수 선언
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
score = 0
isActive = True
isGameOver = False
move = Rect(0, 0, 0, 0)
time500ms = 0
time4Sec = 0
time4SecToggle = False
#########################################################
##2. 스크린
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CodingNow!!")
#########################################################
##3. player
player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (20, 30))
rectPlayer = player.get_rect()
rectPlayer.centerx = (SCREEN_WIDTH / 2)
rectPlayer.centery = (SCREEN_HEIGHT / 2)
#########################################################
##4. 유성
star = [pygame.image.load("star.png") for i in range(20)]
rectStar = [None for i in range(len(star))]
for i in range(len(star)):
    star[i] = pygame.transform.scale(star[i], (20, 20))
    rectStar[i] = star[i].get_rect()
    rectStar[i].y = -1
#########################################################
##5. time
clock = pygame.time.Clock()

while isActive:
#1. 화면 검정색으로 지우기
    SCREEN.fill((0, 0, 0))
#2. 이번트처리
    eventProcess(move)    
#3. 플레이어
    movePlayer(player, rectPlayer,move,isGameOver)
#4. 유성만들기    
    makeStar(rectStar)
    moveStar(star, rectStar,isGameOver)
#5. 충돌
    CheckCollision(rectPlayer, rectStar)
#6. Text 업데이트
    setText(timeUpdate4sec(isGameOver))    
#7.화면업데이트    
    pygame.display.flip()
    clock.tick(100)    



