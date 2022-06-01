import math
import pygame
from sys import exit

from Being import *

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Area 15')
clock = pygame.time.Clock()
basic_font=pygame.font.Font(None,50)

bg_surface = pygame.image.load('code\screens\images\GameBackground.jpg').convert()
bg_surface = pygame.transform.scale(bg_surface, (1280, 720))
alien_solid = pygame.image.load('code\screens\images\Alien.png').convert_alpha()
alien_solid = pygame.transform.scale(alien_solid, (200, 200))
scientist_solid = pygame.image.load('code\screens\images\BasicScientistAggroState_reverse.png').convert_alpha()
scientist_solid = pygame.transform.scale(scientist_solid, (200, 200))

alien = Alien(100)
scientist = Scientist()

alien_x_pos=100
scientist_x_pos=1000
scientist.speed = 1.2
scientist_speed = scientist.speed




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface,(0,0)) #(0,0) is the position up left
    
    #keyboard movement
    alien_speed = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            alien_speed = -alien.speed
        if event.key == pygame.K_RIGHT:
            alien_speed = alien.speed    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            alien_speed = 0        
    alien_x_pos += alien_speed

    #scientist movement
    
    scientist_x_pos-= scientist_speed

    #collision
    collision = alien.isDamaged(scientist_x_pos,alien_x_pos)
    if collision:
        alien.speed = 0
        scientist_speed = 0

    #boundaries
    if(alien_x_pos>1200):
        alien_x_pos=20
    screen.blit(alien_solid,(alien_x_pos,340))
    screen.blit(scientist_solid,(scientist_x_pos,320))

    pygame.display.update()
    clock.tick(60)