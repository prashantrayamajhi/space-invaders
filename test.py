import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
playerImg = pygame.image.load('player.png')
playerX = 380
playerY = 480
playerX_change = 0

bulletImage = pygame.image.load('bullet.png')
bulletX = 380
bulletY = 480
bulletX_change = 0
bulletY_change = 0
bullet_state = 'ready'
can_fire = False


def fire_bullet(x,y):
    screen.blit(bulletImage,(x + 16,y + 10))


def player(x,y):
    screen.blit(playerImg,(x,y))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_SPACE:
            bulletX = playerX 
            bulletY_change = -5
            bullet_state = 'fire'

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_LEFT:
            playerX_change = 0

            
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0
    playerX += playerX_change
    player(playerX,playerY)

    # bullet

    if bulletY <= 0:
        bulletX = playerX
        bulletY = 480
        bullet_state = 'ready'
        can_fire = True

     
    if bullet_state is 'fire' :
        bulletY += bulletY_change            
        fire_bullet(bulletX,bulletY)

        
    pygame.display.update()