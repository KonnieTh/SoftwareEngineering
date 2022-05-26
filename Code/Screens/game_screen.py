import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Area 15')
clock = pygame.time.Clock()
basic_font=pygame.font.Font(None,50)

bg_surface = pygame.image.load('code\screens\images\GameBackground.jpg').convert()
bg_surface = pygame.transform.scale(bg_surface, (1280, 720))
alien_solid = pygame.image.load('code\screens\images\Alien.png').convert_alpha()
alien_solid = pygame.transform.scale(alien_solid, (200, 200))
text_surface = basic_font.render('Ready to run?', False , 'White') 
#surface=pygame.Surface((100,200))
#surface.fill('Red')
alien_x_pos=100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface,(0,0)) #(0,0) is the position up left
    screen.blit(text_surface,(500,100))
    #draw elements and update
    alien_x_pos+=1
    if(alien_x_pos>1200):
        alien_x_pos=20
    screen.blit(alien_solid,(alien_x_pos,340))
    pygame.display.update()
    clock.tick(60)