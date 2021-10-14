import pygame
import math
from pygame.locals import *

# initialize the game
pygame.init()
width, height = 760, 660
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []

# load images
player = pygame.image.load("icon.png")
arrow = pygame.image.load("virus.png")

# keep looping through
while 1:
    # clear the screen before drawing again
    screen.fill(0)
    # draw the screen elements
    screen.blit(player, playerpos)
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] <- 64 or bullet[1] > 640 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
        screen.blit(arrow1, (projectile[1], projectile[2]))

# update the screen
pygame.display.flip()

# loop through the events
for event in pygame.event.get():
    # check if the event is the X button
    if event.type == pygame.QUIT:
        # if it is quit the game
        pygame.quit()
        exit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == K_w:
            keys[0] = True
        if event.key == K_a:
            keys[1] = True
        if event.key == K_s:
            keys[2] = True
        if event.key == K_d:
            keys[3] = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            keys[0] = False
        if event.key == pygame.K_a:
            keys[1] = False
        if event.key == pygame.K_s:
            keys[2] = False
        if event.key == pygame.K_d:
            keys[3] = False
if keys[0]:
    playerpos[1] -= 1
elif keys[2]:
    playerpos[1] += 1
if keys[1]:
    playerpos[0] -= 1
elif keys[3]:
    playerpos[0] += 1
if event.type == pygame.MOUSEBUTTONDOWN:
    position = pygame.mouse.get_pos()
    acc[1] += 1
    arrows.append([math.atan2(position[1]-(playerpos1[1]+32), 
    position[0]-(playerpos1[0]+26)), playerpos1[0]+32, playerpos1[1]+32])