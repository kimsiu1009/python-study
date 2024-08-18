import pygame
import sys

pygame.init()
pygame.display.set_caption("JUMING DOG")

MAX_WIDTH = 800
MAX_HEIGHT = 400

screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
fps = pygame.time.Clock()

imgdog1 = pygame.image.load("images/dog1.png")
imgdog2 = pygame.image.load("images/dog2.png")

dog_height = imgdog1.get_size()[1]
dog_bottom = MAX_HEIGHT - dog_height

dog_x = 50
dog_y = dog_bottom


jump_top = 200
jump_top2 = 200
leg_swap = True
is_bottom = True
is_go_up = False

imgTree = pygame.image.load('images/tree.png')
tree_height = imgTree.get_size()[1]
tree_x = MAX_WIDTH
tree_y = MAX_HEIGHT - tree_height

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

    tree_x -= 12.0
    if tree_x <= 0:
        tree_x = MAX_WIDTH

    screen.blit(imgTree, (tree_x, tree_y))
    screen.blit(imgTree, (tree_x, tree_y))

    if leg_swap:
        screen.blit(imgdog1, (dog_x, dog_y))
        leg_swap = False
    else:
        screen.blit(imgdog2, (dog_x, dog_y))
        leg_swap = True



    pygame.display.update()
    fps.tick(30)