import pygame
import sys
import time
import random

pygame.init()
pygame.display.set_caption("JUMING DOG")

MAX_WIDTH = 800
MAX_HEIGHT = 400

screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
fps = pygame.time.Clock()

imgdog1 = pygame.image.load("images/dog1.png")
imgdog2 = pygame.image.load("images/dog2.png")
crash = pygame.image.load('images/crash.png')

dog_height = imgdog1.get_size()[1]
dog_bottom = MAX_HEIGHT - dog_height

dog_x = 50
dog_y = dog_bottom


jump_top = 200
leg_swap = True
is_bottom = True
is_go_up = False

imgTree = pygame.image.load('images/tree.png')
imgTree2 = pygame.image.load('images/tree_copy.png')
tree_height = imgTree.get_size()[1]

tree_x = MAX_WIDTH
tree_y = MAX_HEIGHT - tree_height    

score = 0

gameover = False
while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

    if  is_go_up:
        dog_y -= 10.0
    elif not is_go_up and not is_bottom:
        dog_y += 10.0

    if is_go_up and dog_y <= jump_top:
        is_go_up = False


    if not is_bottom and dog_y >= dog_bottom:
        is_bottom = True
        dog_y = dog_bottom

    tree_copy_x = 15.0
    tree_x -= 12.0
    if tree_x <= 0:
        tree_x = MAX_WIDTH
    if tree_copy_x <= 0:
        tree_copy_x = MAX_WIDTH

    screen.blit(imgTree, (tree_x, tree_y))

    if leg_swap:
        screen.blit(imgdog1, (dog_x, dog_y))
        dog_rect = imgdog1.get_rect()
        leg_swap = False
    else:
        screen.blit(imgdog2, (dog_x, dog_y))
        dog_rect = imgdog2.get_rect()
        leg_swap = True

    dog_rect.left = dog_x
    dog_rect.top = dog_y

    tree_rect = imgTree.get_rect()
    tree_rect.left = tree_x
    tree_rect.top = tree_y

    # 점수 나타내기
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render("SCORE : " + str(int(score / 2)), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (50, 50)
    screen.blit(text, text_rect)

    if tree_rect.colliderect(dog_rect):
        crash_rect = crash.get_rect()
        crash_rect.left = dog_x 
        crash_rect.top = dog_y 
        screen.blit(crash, (dog_x, dog_y - 30))

        font = pygame.font.Font(pygame.font.get_default_font(), 100)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (400, 200)
        screen.blit(text, text_rect)

        pygame.display.update()
        time.sleep(3)
        break
    else:
        tree_pass_x = tree_x + imgTree.get_rect().width
        if tree_pass_x < dog_x:
            score += 1


    pygame.display.update()
    fps.tick(30)
