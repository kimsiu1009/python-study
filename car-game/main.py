import pygame
from pygame.locals import *
import random

# pygame init
pygame.init()

width = 500
height = 500
screen_size = (width, height)
# bg
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('CAR GAME')

# color

gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Road marker size

road_width = 300
marker_width = 10
marker_height = 50

# Road center marker
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)
# game settings

gameover = False
speed = 2
score = 0

# Draw lane

left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# lane move

lane_marker_mover_y = 0

# car class

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        # car small
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_hight = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width,new_hight))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
# player's car class

class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)
# start x, y

player_x = 250
player_y = 400

# player's car appear

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# other car's image loading

image_filenames = ["pickup_truck.png", "semi_trailer.png", "taxi.png", 
"van.png"]

vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

# other car = sprout 

vehicle_group = pygame.sprite.Group()

# brick image load

crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

# clock settings

clock = pygame.time.Clock()
fps = 120

# game loop

running = True

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player's car is moving
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

            # see if car is break
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True

                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + 
                        vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + 
                        vehicle.rect.center[1]) / 2]
    # draw the graas

    screen.fill(green)

    #  Draw road
    
    pygame.draw.rect(screen, gray, road)

    #  Draw edge marker

    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # update

    # lane mark
    lane_marker_mover_y += speed * 2
    if lane_marker_mover_y >= marker_height * 2:
        lane_marker_mover_y = 0

    #  draw lane mark

    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_mover_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_mover_y, marker_width, marker_height))
    
    # draw player's car

    player_group.draw(screen)

    # draw other cars
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False

        

        if add_vehicle:
            # to random, choose lane
            lane = random.choice(lanes)
            # to random, choose car
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

        # move other cars


    for vehicle in vehicle_group:
        vehicle.rect.y += speed

        # if cars go out, move cars
        
        if vehicle.rect.top >= height:
            vehicle.kill()

            # add score

            score += 1

            if score > 0 and score % 5 == 0:
                speed += 1

        # draw other cars

    vehicle_group.draw(screen)

    # discover score

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render("SCORE : " + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center= (50, 400)
    screen.blit(text, text_rect)

    # discover break forward

    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    if gameover:
        screen.blit(crash, crash_rect)

        pygame.draw.rect(screen, red, (0, 50, width, 100))

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render("GAME OVER, PlAY AGAIN? (ENTER y or n)", True, white)
        text_rect = text.get_rect()
        text_rect.center= (width / 2, 100)
        screen.blit(text, text_rect)

    pygame.display.update()

    # if player want to continue playing? or ""
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False

            if event.type == KEYDOWN:
                if event.key == K_y:
                    # init game

                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    gameover = False
                    running = False
# pygame 종료           

pygame.quit()