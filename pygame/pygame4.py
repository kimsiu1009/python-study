import pygame, sys

pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Pacman')
fiende_time = 0
listx = []
listy = []

def walls():
 global listx, listy, original_X, original_Y
 listx = [680, 700, 720, 740, 640,640,640,640,640, 640, 660, 680, 700, 720, 740, 760, 780, 800, 660, 680, 700, 720, 740, 760, 780, 800, 640, 640, 640, 640, 640, 660, 680, 700, 720, 740, 0, 20, 40, 60, 80, 100, 120, 140, 140, 140, 140, 140, 140, 40, 60, 80, 100, 120, 140, 0, 20, 40, 60, 80, 100, 120, 140, 140, 140, 140, 40, 60, 80, 100, 120, 140, 20, 20, 20, 20, 20, 20, 20, 20, 20, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760, 20, 20, 20, 20, 20, 20, 40, 40, 40, 40, 40, 40, 480, 400, 400, 700, 220, 220 ,140, 400, 400, 400, 400, 400, 720, 740, 760, 780, 80, 60, 40, 20, 640, 300, 320, 340, 300, 300, 300, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 480, 480, 480, 480, 480, 460, 440, 480, 400, 400, 400, 400, 320, 340, 360, 380, 400, 420, 440, 460, 480, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 240,  260, 280, 300, 320, 480, 500, 520, 540, 560, 220, 220, 220, 220, 220, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560,  240, 80, 100,  260, 280, 300, 320, 480, 500, 520, 540, 560, 400, 400, 400, 400, 400, 400, 320, 340, 360, 380, 400, 420, 440, 460, 480, 560, 560, 560, 560, 560, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 100, 120, 140, 160, 180, 200, 220,  220, 220,  240, 260, 280, 300, 220, 220, 320, 340, 360, 380, 400, 420, 440, 460, 400, 400, 400, 400, 140, 140, 140, 140, 140, 120, 640, 640, 640, 640, 640, 640, 660, 680, 700, 80,  100, 120, 140, 640, 660, 680, 700, 220, 240, 260, 280, 300, 220, 220, 260, 280, 300, 80, 100, 120, 140, 80, 100, 120, 140, 480, 240, 500, 520, 540, 500, 520, 540, 660, 680, 700, 660, 660, 680, 700, 480, 480, 500, 640, 640, 560, 560 ] 
 listy = [240, 240, 240, 240, 240, 260, 280, 300, 320, 340, 340,340,340,340,340,340,340,340,400, 400, 400, 400, 400, 400, 400, 400, 400, 420, 440, 460, 480, 480, 480, 480, 480, 480, 340, 340, 340, 340, 340, 340, 340, 340, 260, 280, 300, 320, 340, 240, 240, 240, 240, 240, 240, 400, 400, 400, 400, 400, 400, 400, 400, 420, 440, 460, 480, 480, 480, 480, 480, 480, 60, 80, 100, 120, 140, 160, 180, 200, 220, 60, 80, 100, 120, 140, 160, 180, 200, 220, 660, 680, 700, 720, 740, 500, 520, 540, 560, 580, 600, 500, 520, 540, 560, 580, 600, 640, 660, 680, 700, 720, 740, 620, 640, 260, 560, 640, 680 , 100, 100, 80, 60, 40, 20, 620, 620, 620, 620, 620, 620, 620, 620, 80, 320, 320, 320, 340, 360, 380, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 380, 400, 380, 360, 340, 320, 320, 320, 240, 220, 200, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 200, 220, 240, 260, 280, 300, 320, 340, 400, 260,  260, 260, 260, 260, 260, 260, 260, 260, 260, 420, 440, 460, 480, 560, 420, 440, 460, 480, 340, 320, 300, 280, 260, 240, 220, 200, 180, 400, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 480, 500, 520, 540, 560, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 620, 640, 660, 680, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 620, 700, 700, 700, 700, 700, 660, 620, 620, 620, 620, 620, 620, 620, 620, 620, 660, 680, 700, 560, 580, 600, 620, 640, 560, 560, 560, 580, 600, 620, 640, 560, 560, 560, 180, 180, 180, 180, 180, 180, 180, 180, 100, 100, 100, 100, 100, 80,  80,  80,  80,  80, 100, 100, 100, 100, 80, 80, 80, 80, 80, 80, 80, 80, 80,  80, 100, 100, 100, 100, 100, 100, 80,  80,  80,  80, 100, 100, 100, 100, 100, 80, 100, 80 ] 
 for i in range(len(listx)):
    pygame.draw.rect(screen, (127, 127, 127), (listx[i], listy[i], 20, 20))
    # Add yellow walls on the top and bottom
 for i in range(0, 800, 20):
    pygame.draw.rect(screen, (127, 127, 127), (i, 0, 20, 20))
    pygame.draw.rect(screen, (127, 127, 127), (i, 780, 20, 20))
    # pygame.draw.rect(screen, (127, 127, 127), (i, Y, 20, 20)), (X, i, 20, 20)
 for i in range(0, 240, 20):
    pygame.draw.rect(screen, (127, 127, 127), (780, i, 20, 20))
    pygame.draw.rect(screen, (127, 127, 127), (0, i, 20, 20))
 for i in range(780, 460, -20):
              pygame.draw.rect(screen, (127, 127, 127), (780, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (0, i, 20, 20))
 for i in range(0, 160, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 480,  20, 20))
 for i in range(780, 620, -20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 480, 20, 20))
 for i in range(400, 480, 20):
              pygame.draw.rect(screen, (127, 127, 127), (140, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (640, i, 20, 20))
 for i in range(0, 140, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 400, 20, 20))
 for i in range(640, 800, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 400, 20, 20))
 for i in range(0,160, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 240, 20, 20))
 for i in range(640, 800, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 240, 20, 20))
 for i in range(240, 340, 20):
              pygame.draw.rect(screen, (127, 127, 127), (140, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (640, i, 20, 20))
 for i in range(0, 160, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 340, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (i, 340, 20, 20))
 for i in range(640, 800, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 340, 20, 20))
 for i in range(20, 780, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 760, 20, 20))
 for i in range(20, 780, 20):
              pygame.draw.rect(screen, (127, 127, 127), (i, 20, 20, 20))
 for i in range(40,240,20):
              pygame.draw.rect(screen, (127, 127, 127), (20, i, 20, 20))
 for i in range(640, 760, 20):
              pygame.draw.rect(screen, (127, 127, 127), (760, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (20, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (40, i, 20, 20))
 for i in range(40, 240,20):
              pygame.draw.rect(screen, (127, 127, 127), (760, i, 20, 20))
 for i in range(480, 620,20):
              pygame.draw.rect(screen, (127, 127, 127), (760, i, 20, 20))
              pygame.draw.rect(screen, (127, 127, 127), (20, i, 20, 20))
       

                          
positionX = 400
positionY = 300
positionFX = 400
positionFY = 380

def enemy():
    global positionFX, positionFY
    if abs(positionX-positionFX) > abs(positionY-positionFY):
        if positionX > positionFX:
            positionFX += 20
        else:
            positionFX -= 20
    else:
        if positionY > positionFY:
            positionFY += 20
        else:
            positionFY -= 20


clock = pygame.time.Clock()
GAME_SPEED = 10

last_pressed_1 = None

while True:
       fiende_time += 1
       original_FX = positionFX
       original_FY = positionFY
       original_X = positionX
       original_Y = positionY
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                 game_over = True 
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    last_pressed_1 = "right"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    last_pressed_1 = "left"
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    last_pressed_1 = "up"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    last_pressed_1 = "down"
                elif event.key == pygame.K_l:
                    last_pressed2 = "right"
                elif event.key == pygame.K_j:
                    last_pressed2 = "left"
                elif event.key == pygame.K_i:
                    last_pressed2 = "up"
                elif event.key == pygame.K_k:
                    last_pressed2 = "down"

                

       
       if last_pressed_1 is not None:
            # Spellogik
            if last_pressed_1 == "right":
                positionX += 20
            if last_pressed_1 == "left":
                positionX -= 20
            if last_pressed_1 == "up":
                positionY -= 20
            if last_pressed_1 == "down":
                positionY += 20
        
       if fiende_time >= 2:
        enemy()
        fiende_time = 0
        
    # Check for collisions with walls 
       for i in range(len(listx)):
        if positionX + 15 >= listx[i] and positionX - 15 <= listx[i] + 20 and positionY + 15 >= listy[i] and positionY - 15 <= listy[i] + 20:
              print("Collision detected")
              positionX = original_X
              positionY = original_Y
        if positionY >= 760 or positionY <= 40:
              positionY = original_Y
       for i in range(len(listx)):
        if positionFX + 15 >= listx[i] and positionFX - 15 <= listx[i] + 20 and positionFY + 15 >= listy[i] and positionFY - 15 <= listy[i] + 20:
              print("Collision detected")
              positionFX = original_FX
              positionFY = original_FY
        if positionY >= 760 or positionY <= 40:
              positionFY = original_FY

              
 
       screen.fill((0, 0, 0))
       walls()
       pygame.draw.circle(screen, (255,255, 0), (positionX, positionY), 20)
       pygame.draw.circle(screen, (255, 0, 0), (positionFX, positionFY), 20)

       pygame.display.update()

       clock.tick(GAME_SPEED)

       print(positionX, positionY)

       
