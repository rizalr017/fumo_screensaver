import pygame, time

pygame.init()
screenWidth, screenHeight = 1270, 720
fumoSpeed = [3, 3]
backgroundColor = 0, 0, 0
pygame.mixer.music.load('super_idol.wav')
pygame.mixer.music.play(loops=-1)
screen = pygame.display.set_mode((screenWidth,screenHeight))

if not screen:
    pygame.quit()
    sys.exit()

picture = pygame.image.load("luant-s-artworks-reimucirnothinkmeme.jpg")
fumo = pygame.image.load("fumo.png")
fumo = pygame.transform.scale(fumo,(180,250))
fumoRect = fumo.get_rect()

font = pygame.font.Font(None, 36)
score = 0

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  screen.fill(backgroundColor)
  screen.blit(picture, (0, 0))
  screen.blit(fumo,fumoRect)
  fumoRect = fumoRect.move(fumoSpeed)

  if fumoRect.left < 0 or fumoRect.right > screenWidth:
    fumoSpeed[0] = -fumoSpeed[0]
    score += 1
  if fumoRect.top < 0 or fumoRect.bottom > screenHeight:
    fumoSpeed[1] = -fumoSpeed[1]
    score += 1

  scoreText = font.render("Score: " + str(score), True, (255, 255, 255))
  screen.blit(scoreText, (10, 10))

  pygame.display.flip()
  clock.tick(60)
