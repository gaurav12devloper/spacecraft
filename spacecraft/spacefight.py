import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
# caption and icon
pygame.display.set_caption("fight")
icon = pygame.image.load("war.png")
pygame.display.set_icon(icon)
# backgroundimage
background = pygame.image.load("background.png")
# plyer and icon
playerimag = pygame.image.load("war.png")
playerx = 370
playery = 500
playerx_chng = 0
# enemy icon
enemyimag = []
enemyx = []
enemyy = []
enemyx_chng = []
enemyy_chng = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyimag.append(pygame.image.load("virus.png"))
    enemyx.append(random.randint(0, 780))
    enemyy.append(random.randint(50, 150))
    enemyx_chng.append(3)
    enemyy_chng.append(20)
# bullet image
bulletimag = pygame.image.load("bullet.png")
bulletx = 0
bullety = 500
bulletx_chng = 0
bullety_chng = 40
bullet_state = 'ready'
# score
player_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
game_over = pygame.font.Font('freesansbold.ttf', 70)
fontx = 10
fonty = 10


def score(x, y):
    score = font.render("score" + str(player_score), True, (255, 255, 255))
    screen.blit(score,(x, y))

def player(x, y):
    screen.blit(playerimag, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimag[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimag, (x, y))

def text_over():
    over = game_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over,(240,300))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if distance < 27:
        return True


running = True
while running:
    # screen.fill((255 , 0 , 0))
    # backgroundimage
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # function call here
    player(playerx, playery)
    # movemoment of spacecraft
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerx_chng = -8
        if event.key == pygame.K_RIGHT:
            playerx_chng = 8
        if event.key == pygame.K_SPACE:
            if bullet_state is 'ready':
                bulletx = playerx
                fire_bullet(bulletx, bullety)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_chng = 0
    # changing postion of spacecrft
    playerx += playerx_chng
    if playerx <= 0:
        playerx = 760
    elif playerx >= 760:
        playerx = 0
    # changing postion of enemy
    for i in range(num_of_enemy):
        #make game over
        if enemyy[i]>450:
            for j in range(num_of_enemy):
                enemyy[j] = 2000
            text_over()

        enemyx[i] += enemyx_chng[i]
        if enemyx[i] <= 0:
            enemyx_chng[i] = 8
            enemyy[i] += enemyy_chng[i]
        elif enemyx[i] >= 760:
            enemyx_chng[i] = -8
            enemyy[i] += enemyy_chng[i]
        # collision
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = 'ready'
            player_score += 1
            enemyx[i] = random.randint(0, 780)
            enemyy[i] = random.randint(50, 150)
        # function call
        enemy(enemyx[i], enemyy[i], i)
    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletx, bullety)
        bullety += -30
    score(fontx,fonty)
    pygame.display.update()
