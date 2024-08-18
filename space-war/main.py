import pygame
import random

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Rocket Game")

image_bg = pygame.image.load("space-war/images/Moon.png")
image_pico = pygame.image.load("space-war/images/pico-1.png")
image_Rocket = pygame.image.load("space-war/images/Rocket-1.png")
image_star = pygame.image.load("space-war/images/star-1.png")
image_ball = pygame.image.load("space-war/images/ball-1.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_pico_width = image_pico.get_rect().size[0]
size_pico_height = image_pico.get_rect().size[1]

size_Rocket_width = image_Rocket.get_rect().size[0]
size_Rocket_height = image_Rocket.get_rect().size[1]

size_star_width = image_star.get_rect().size[0]
size_star_height = image_star.get_rect().size[1]

size_ball_width = image_ball.get_rect().size[0]
size_ball_height = image_ball.get_rect().size[1]

x_pos_pico = size_bg_width / 2 - size_pico_width / 2
y_pos_pico = size_bg_height - size_pico_height 

x_pos_Rocket = size_bg_width / 2 - size_Rocket_width / 2
y_pos_Rocket = 0

x_pos_star = size_bg_width / 2 - size_star_width / 2
y_pos_star = size_bg_height - size_pico_height - size_star_height

x_pos_ball = size_bg_width / 2 - size_ball_width / 2
y_pos_ball = size_Rocket_height

to_x_Rocket = 0
random_Rocket = random.randrange(0, size_bg_width - size_Rocket_width)

to_x_pico = 0

ball_time = 0
balls = []
stars =[]

random_time = random.randrange(100, 200)

hp_pico = 10
hp_Rocket = 10

rect_pico = image_pico.get_rect()
rect_Rocket = image_Rocket.get_rect()

rect_pico.topleft = (x_pos_pico, y_pos_pico)
rect_Rocket.topleft = (x_pos_Rocket, y_pos_Rocket)

rect_stars = []
rect_balls = []

font_hp = pygame.font.SysFont(None, 30 )
font_gameover = pygame.font.SysFont(None, 100 )

gameover = False


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x_pico = 1
            elif event.key == pygame.K_LEFT:
                to_x_pico = -1

            if event.key == pygame.K_SPACE:
                x_pos_star = x_pos_pico + size_star_width / 2
                stars.append([x_pos_star, y_pos_star])

                rect_stars.append(image_star.get_rect())
                
               

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_x_pico = 0
            elif event.key == pygame.K_LEFT:
                to_x_pico = 0

    if x_pos_pico < 0:
        x_pos_pico = 0
    elif x_pos_pico > size_bg_width - size_pico_width:
        x_pos_pico = size_bg_width - size_pico_width
    else:
        x_pos_pico += to_x_pico

    rect_pico.topleft = (x_pos_pico, y_pos_pico)


    if random_Rocket > x_pos_Rocket:
        x_pos_Rocket += 0.5
    elif random_Rocket < x_pos_Rocket:
        x_pos_Rocket -= 0.5
    else:
        random_Rocket = random.randrange(0, size_bg_width - size_Rocket_width)

    ball_time += 1
    if ball_time == random_time:
        random_time = random.randrange(100, 200)
        ball_time = 0
        x_pos_ball = x_pos_Rocket + size_ball_width / 2
        balls.append([x_pos_ball, y_pos_ball])

        rect_balls.append(image_ball.get_rect())

    background.blit(image_bg, (0, 0))
    background.blit(image_pico, (x_pos_pico, y_pos_pico))
    background.blit(image_Rocket, (x_pos_Rocket, y_pos_Rocket))

    if len(stars):
        for star in stars:
            i = stars.index(star)
            star[1] -= 1
            background.blit(image_star, (star[0], star[1]))

            rect_stars[i].topleft = (star[0], star[1])

            if rect_stars[i].colliderect(rect_Rocket):
                stars.remove(star)
                rect_stars.remove(rect_stars[i])
                hp_Rocket -= 1
                if hp_Rocket == 0:
                    gameover = "PICO WIN"

            if star[1] <= 0:
                stars.remove(star)
                rect_stars.remove(rect_stars[i])

    if len(balls):
        for ball in balls:
            i = balls.index(ball)
            ball[1] += 1
            background.blit(image_ball,(ball[0], ball[1]))
    
            rect_balls[i].topleft = (ball[0], ball[1])
            
            if rect_balls[i].colliderect(rect_pico): 
                balls.remove(ball)
                rect_balls.remove(rect_balls[i])
                hp_pico -= 1

                if hp_pico == 0:
                    gameover = "ROCKET WIN"

            if ball[1] >= size_bg_height:
                balls.remove(ball)
                rect_balls.remove(rect_balls[i])

    text_hp_pico = font_hp.render('pico'+ str(hp_pico), True, (255, 255, 0))
    background.blit(text_hp_pico, (10, 10))

    text_hp_Rocket = font_hp.render('Rocket'+ str(hp_Rocket), True, (255, 255, 0))
    background.blit(text_hp_Rocket, (380, 10))

    if gameover:
        text_gameover = font_gameover.render(gameover, True, (255, 255, 0))

        size_text_width = text_gameover.get_rect().size[0]
        size_text_height = text_gameover.get_rect().size[1]

        x_pos_text = size_bg_width / 2 - size_text_width / 2
        y_pos_text = size_bg_height / 2 - size_text_height / 2

        background.blit(text_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(3000)
        play = False

    print(hp_Rocket, hp_pico)
    pygame.display.update()  

pygame.quit()