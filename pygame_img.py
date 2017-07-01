import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,480))
pygame.display.set_caption('Flick Demo')

clock = pygame.time.Clock()
Img = pygame.image.load('abc.jpg')

def disp(x,y):
    gameDisplay.blit(Img, (x,y))

#x =  (800 * 0.45)
#y = (480 * 0.8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((0,0,0))
    disp(0,0)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
