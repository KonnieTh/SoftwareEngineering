import glob
import math
import pygame
from Item import *
from sys import exit
from User import *
from Being import *

pathToImages = 'Code\Screens\images\\'

pygame.init()
scr = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Area 15')
clock = pygame.time.Clock()
basic_font=pygame.font.Font(None, 50)

bg_surface = pygame.image.load(pathToImages+'GameBackground.jpg').convert()
bg_surface = pygame.transform.scale(bg_surface, (1280, 720))
alien_solid = pygame.image.load(pathToImages+'Alien.png').convert_alpha()
alien_solid = pygame.transform.scale(alien_solid, (200, 200))
scientist_solid = pygame.image.load(pathToImages+'BasicScientistAggroState_reverse.png').convert_alpha()
scientist_solid = pygame.transform.scale(scientist_solid, (200, 200))
cables_solid = pygame.image.load(pathToImages+'Cables.png').convert_alpha()
cables_solid = pygame.transform.scale(cables_solid, (100, 100))
inv = pygame.image.load(pathToImages+"inventoryScreen.png").convert_alpha()
inv = pygame.transform.scale(inv, (1200, 750)) 
cables2 = pygame.image.load(pathToImages+'Cables.png').convert_alpha()
cables2 = pygame.transform.scale(cables_solid, (100, 100))
bag = pygame.image.load(pathToImages+'inventoryBag.png').convert_alpha()
bag = pygame.transform.scale(bag, (50, 50))



cables = Item(5, 'Cables', 'material to construct useful items',290, 460, cables_solid)
pressA = pygame.image.load(pathToImages+'Press-A.png').convert_alpha()
pressA = pygame.transform.scale(pressA, (200, 100))


user = User('Kostas', '1234', 'kostas@gmail.com')
user.inventory.materialDict['cables'] = 0

alien = Alien(100)
scientist = Scientist()

alien_x_pos=100
scientist_x_pos=1000
scientist.speed = 1.2
scientist_speed = scientist.speed


class imButton:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback

    def on_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)

blitInvArr = []
blitInv = False
pressed = True

def buttonPushed(button):
    global pressed
    if pressed:
        global inInvArr
        inInvArr = []
        global inv
        inv = pygame.image.load(pathToImages+"inventoryScreen.png").convert_alpha()
        inv = pygame.transform.scale(inv, (1200, 750)) 
        global blitInvArr
        blitInvArr = True
        global alien_speed
        alien_speed = 0
        global scientist_speed
        scientist_speed = 0
        global blitInv
        blitInv = True       
        pressed = not pressed

    else:       
        if cables.inInv:
            cables.pic.fill((0,0,0,0))
        scientist_speed = 1.2  
        alien_speed = alien.speed
        blitInv = False             
        pressed = not pressed 
        inv.fill((0,0,0,0)) 

        

button = imButton(bag, (1200, 650), buttonPushed)

start_x = 260
start_y = 200

while True:
    for event in pygame.event.get():
        collItem = cables.collided(alien_x_pos)       
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # In event loop see if button is trigger. Under pygame.MOUSEBUTTONDOWN.    
        button.on_click(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if collItem and (not cables.inInv):
                    user.inventory.materialDict['cables'] += 1                    
                    cables_solid.fill((0,0,0,0))
                    cables.inInv = True
                    


    # In main loop draw area.

    scr.blit(bg_surface,(0,0)) #(0,0) is the position up left
    scr.blit(button.image, button.rect) 

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

    #collisions
    collision = alien.isDamaged(scientist_x_pos,alien_x_pos)

    if collision:
        alien.speed = 0
        scientist_speed = 0




    #boundaries
    if(alien_x_pos>1200):
        alien_x_pos=20
    scr.blit(alien_solid,(alien_x_pos,340))
    scr.blit(scientist_solid,(scientist_x_pos,320))
    scr.blit(cables_solid, (cables.x_pos, cables.y_pos))
    #scr.blit()

    if collItem:
        if not cables.inInv:
            scr.blit(pressA, (cables.x_pos, cables.y_pos-100))

    if blitInv:
        scr.blit(inv, (130, 0))

        if cables.inInv:
            scr.blit(cables2, (start_x, start_y))

    pygame.display.update()
    clock.tick(60)