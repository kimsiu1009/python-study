import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Monkey banana")

fps = pygame.time.Clock()

# 이미지 로딩
image_bg = pygame.image.load("images/monkey/Blue-sky.png")
image_banana = pygame.image.load("images/monkey/bananas.png")
image_monkey = pygame.image.load("images/monkey/monkey.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

x_pos_monkey = size_bg_width / 2 - size_monkey_width / 2
y_pos_monkey = size_bg_height  - size_monkey_height

to_x = 0
# to_y = 0

x_speed_banana = 2
y_speed_banana = 2


point = 0
font_point = pygame.font.SysFont(None, 30)

font_gameover = pygame.font.SysFont(None,80)
text_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))

size_text_width = text_gameover.get_rect().size[0]
size_text_height = text_gameover.get_rect().size[1]

x_pos_text = size_bg_width / 2 - size_text_width / 2
y_pos_text = size_bg_height / 2 - size_text_height / 2

play = True


while play:

  deltaTime= fps.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x = -3
      elif event.key == pygame.K_RIGHT:
        to_x = 3

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        to_x = 0
      elif event.key == pygame.K_RIGHT:
        to_x = 0

    # if event.type == pygame.MOUSEMOTION:
    #   x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
    #   x_pos_banana = x_pos_mouse - size_banana_width / 2
    #   y_pos_banana = y_pos_mouse - size_banana_height / 2


  # 원숭이가 왼쪽, 오른쪽 밖으로 나가지 않게 함...

  if x_pos_monkey < 0:
    x_pos_monkey = 0
  elif x_pos_monkey > size_bg_width - size_monkey_width:
    x_pos_monkey = size_bg_width - size_monkey_width
  else:
    x_pos_monkey += to_x

  x_pos_banana += x_speed_banana
  y_pos_banana += y_speed_banana

  # 바나나가 벽에 부딪히는 조건을 설정

  if x_pos_banana <= 0:
    x_speed_banana = -x_speed_banana
    x_pos_banana = 0
  elif x_pos_banana >= size_bg_width - size_banana_width:
    x_speed_banana = -x_speed_banana
    x_pos_banana = size_bg_width - size_banana_width

  if y_pos_banana <= 0:
    y_speed_banana = -y_speed_banana
    y_pos_banana = 0
  elif y_pos_banana >= size_bg_height - size_banana_height:
    y_speed_banana = -y_speed_banana
    y_pos_banana = size_bg_height - size_banana_height

    background.blit(text_gameover, (x_pos_text, y_pos_text))
    pygame.display.update()
    pygame.time.delay(2000)
    play = False

  # 원숭이와 바나나가 충돌하는 조건

  # 바나나에 image의 사각형 구한다....
  rect_banana = image_banana.get_rect()
  rect_banana.left = x_pos_banana
  rect_banana.top = y_pos_banana

# 원숭이 ""

  rect_monkey = image_banana.get_rect()
  rect_monkey.left = x_pos_monkey
  rect_monkey.top = y_pos_monkey

  # 충돌

  if rect_monkey.colliderect(rect_banana):
    x_speed_banana = -x_speed_banana
    y_speed_banana = -y_speed_banana
    point += 1



  # 배경을 먼저 blit 해야 함...
  # surface 좌표는 왼쪽 상단이 0, 0, 이미지의 왼쪽 위가 0, 0

  background.blit(image_bg, (0, 0))
  background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
  background.blit(image_banana, (x_pos_banana, y_pos_banana))


  text_point = font_point.render(str(point), True, (0, 0, 0))
  background.blit(text_point, (10, 10))
  pygame.display.update()

pygame.quit()