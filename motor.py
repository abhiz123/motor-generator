import pygame

pygame.init()
screenWidth, screenHeight = 800, 600
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((screenWidth, screenHeight))

#heliImage = pygame.image.load("Fly.png")
backgroundImage = pygame.image.load('/Users/Abhiram/Desktop/mountain.png')
heliImage = pygame.image.load('/Users/Abhiram/Desktop/Fly.png')

heliImage = pygame.transform.scale(heliImage,(150,100))
#print(heliImage)
heliImageRect = heliImage.get_rect()

heliWidth = heliImageRect[2]-heliImageRect[0]
heliHeight = heliImageRect[3]-heliImageRect[1]

heliXCoordinate = 0
heliYCoordinate = 0
heliChangeInX = 0
heliChangeInY = 0


game_exit = False
crashed = False
screen.fill(backgroundColor)
screen.blit(heliImage, (heliXCoordinate, heliYCoordinate))
pygame.display.flip()

# Now we should make the helicopter move using arrow keys
while True:
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        heliChangeInX = -5
      if event.key == pygame.K_RIGHT:
        heliChangeInX = 5
      if event.key == pygame.K_UP:
        heliChangeInY = -5
      if event.key == pygame.K_DOWN:
        heliChangeInY = 5


    if event.type == pygame.KEYUP:

      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        heliChangeInX = 0

      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        heliChangeInY = 0



  heliXCoordinate += heliChangeInX
  if heliXCoordinate < 0:
    heliXCoordinate = 0
  if heliXCoordinate > (screenWidth-heliWidth):
    heliXCoordinate = (screenWidth-heliWidth)

  heliYCoordinate += heliChangeInY
  if heliYCoordinate < 0:
    heliYCoordinate = 0
  if heliYCoordinate>(screenHeight-heliHeight):
    heliYCoordinate = (screenHeight-heliHeight)

  screen.fill(backgroundColor)
  screen.blit(backgroundImage,(0,0))
  screen.blit(heliImage, (heliXCoordinate,heliYCoordinate))
  pygame.display.update()
