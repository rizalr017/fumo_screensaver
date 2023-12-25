import pygame, time
from pygame import mixer

pygame.init()
screenWidth, screenHeight = 800, 640
fumoSpeed = [3, 3]
backgroundColor = 0, 0, 0

file = 'super_idol.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((screenWidth,screenHeight))
picture = pygame.image.load("IMG_20210120_164439Copy.jpg")
fumo = pygame.image.load("db1713938a1239eeacead462456568c0.png")
fumo = pygame.transform.scale(fumo,(300,300))
fumoRect = fumo.get_rect()

while True:
    #for event in pygame.event.get():
        #if event.type == QUIT:

  screen.blit(picture, (0, 0))
  screen.blit(fumo,fumoRect)
  fumoRect = fumoRect.move(fumoSpeed)

  if fumoRect.left < 0 or fumoRect.right >= screenWidth:
    fumoSpeed[0] = -fumoSpeed[0]
  if fumoRect.top < 0 or fumoRect.bottom >= screenHeight:
    fumoSpeed[1] = -fumoSpeed[1]


  pygame.display.flip()
  time.sleep(10/1000)
