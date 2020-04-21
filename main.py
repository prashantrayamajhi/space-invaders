import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Inavders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')


score = 0
font = pygame.font.Font('freesansbold.ttf',32)

def show_score():
    score_value = font.render("Score : " + str(score),True,(255,255,255))
    screen.blit(score_value,(10,10))


game_over_font = pygame.font.Font('freesansbold.ttf',90)


def game_over_text():
    over_text = font.render("Game Over ",True,(255,255,255))
    screen.blit(over_text,(320,200))

# Player 
playerImg = pygame.image.load('player.png')
playerX = 380
playerY = 500
playerX_change = 0


# Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append( random.randint(64,736))
    enemyY. append(random.randint(30,100))
    enemyX_change.append(7)
    enemyY_change.append( 40)

# Bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 6
bullet_state = 'ready'

# Functions
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x + 16, y + 10))

def enemy(x,y):
    screen.blit(enemyImg[i],(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def isCollision(bulletX,bulletY,enemyY,enemyX):
    distance = math.sqrt((math.pow(bulletX-enemyX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        False
 
running = True
while running:
    
    # background image 
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key presss
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
    
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    bulletY_change = -6
                    bullet_state = 'fire'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change 

    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736 
    player(playerX,playerY)

    # Enemy movement
    

    for i in range(number_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = 7
            enemyY[i] += enemyY_change[i]
            
        if enemyX[i] >= 736:
            enemyX_change[i] = -7
            enemyY[i] += enemyY_change[i]
        
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i],enemyY[i])   
      
        # Game over
        if enemyY[i] > 440:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            
            # Collision Detection  

        collision = isCollision(bulletX,bulletY,enemyY[i],enemyX[i])
        if collision:
            bulletY = 500
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(64,736)
            enemyY[i] = random.randint(30,100)
            
        # bullet movement
    if bulletY <= 0:
        bulletY = 500
        bulletX = playerX
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY += bulletY_change

    show_score()
    pygame.display.update()