import pygame
import random

class Space_Invaders:

    # Background Image
    background = pygame.image.load('background.png')

    # Player's Coordinates  
    playerX = 380
    playerY = 500
    playerX_change = 0

    # Enemy's Coordinates
    enemyX = random.randint(30,770)
    enemyY = random.randint(30,100)
    enemyX_change = 5
    enemyY_change = 0
    number_of_enemies = 5

    # Bullets Coordinates
    bulletX = 380
    bulletY = 500
    bulletX_change = 0
    bulletY_change = 0
    bullet_state = 'ready'



    def __init__(self,width,height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Space Invaders")
        
    # Player
    def player(self,x,y):

        playerImg = pygame.image.load('player.png')
        self.screen.blit(playerImg,(x,y))

    # Enemies
    def enemy(self,x,y):
        enemyImg = pygame.image.load('enemy.png')
        self.screen.blit(enemyImg,(x,y))

    # Bullet 
    def fire_bullet(self,x,y):
        bulletImg = pygame.image.load('bullet.png')
        self.screen.blit(bulletImg,(x,y))

    # Game loop
    def game_loop(self):
        running = True

        while running:
            self.screen.blit(Space_Invaders.background,(0,0))

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Space_Invaders.playerX_change = 6
                    if event.key == pygame.K_LEFT:
                        Space_Invaders.playerX_change = -6
                    if event.key ==  pygame.K_SPACE:
                        Space_Invaders.bulletY_change = -2
                        Space_Invaders.bulletX = -Space_Invaders.playerX
                        Space_Invaders.bullet_state = 'fire '
                
                if event.type == pygame.KEYUP:
                    Space_Invaders.playerX_change = 0

            # Code for Player's bullet 
            if Space_Invaders.bullet_state is 'fire':
                Space_Invaders.bulletY += Space_Invaders.bulletY_change
                self.fire_bullet(Space_Invaders.bulletX,Space_Invaders.bulletY)

                                 

            # Code for the Player 
            if Space_Invaders.playerX > 736:
                Space_Invaders.playerX = 736
            if Space_Invaders.playerX <= 0:
                Space_Invaders.playerX = 0

            Space_Invaders.playerX += Space_Invaders.playerX_change
            self.player(Space_Invaders.playerX,Space_Invaders.playerY)

            # Code for the enemy


            if Space_Invaders.enemyX <= 0:
                Space_Invaders.enemyX_change = 5

            if Space_Invaders.enemyX > 740:
                Space_Invaders.enemyX_change = -5

            Space_Invaders.enemyX += Space_Invaders.enemyX_change 
            self.enemy(Space_Invaders.enemyX,Space_Invaders.enemyY)



            # Very Important Stuff that works better at the bottom 
            pygame.display.update()


game = Space_Invaders(800,600)
game.game_loop()