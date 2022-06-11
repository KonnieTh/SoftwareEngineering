import pygame
import sys

scr = pygame.display.set_mode((1910, 1060), pygame.FULLSCREEN)
x, y = scr.get_size()
#Title
pygame.display.set_caption('Area 15 Welcome!')
icon = pygame.image.load('Code\Screens\images\logo.png')

#initialise game
pygame.init()
startingImg = pygame.image.load('Code\Screens\images\logo.png')

myfont = pygame.font.SysFont("Segoe UI", 60)
label = myfont.render("Welcome to", False, (255,255,255))

def showProfile():

    running1 = True
    while running1:
        scr.fill((32, 230, 174))  
        for event in pygame.event.get():   
            button5.click(event, pygame.QUIT)
        pygame.display.update()
        button5.show()
        
class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        scr.blit(self.surface, (self.x, self.y))

    def click(self, event, func):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    func()

class Label:
    def __init__(self, text, pos, font, color):
        self.text = text
        self.x, self.y = pos
        self.font = font
        self.color = color
    
    def show(self):
        scr.blit(self.font.render(self.text, False, (self.color)), (self.x, self.y))

class Picture:
    def __init__(self, imagePath, pos) -> None:
        self.imagePath = imagePath
        self.x, self.y = pos

    def show(self) -> None:
        
        scr.blit(pygame.image.load(self.imagePath), (self.x, self.y))

label1 = Label("Welcome to", (x/2-170, y/2-420), myfont, ("navy"))
pic1 = Picture('Code\Screens\images\logo.png', (x/2-120, y/2-350))
label2 = Label("Start your escape", (x/2-230, y/2-150), myfont, ("navy"))
button1 = Button("       New Game       ",(x/2-120, y/2),font=30,bg="navy")
button2 = Button("       Load Game      ", (x/2-120, y/2+80), font=30, bg = "navy")
button3 = Button("      Online co-op      ", (x/2-120, y/2+160), font=30, bg = "navy")
button4 = Button("          Settings         ", (x/2-120, y/2+240), font=30, bg="navy")
button5 = Button("             Quit            ", (x/2-120, y/2+320), font=30, bg="navy") 
button6 = Button("   E-shop   ", (x/2+350, y/32), font=30, bg="navy")
button7 = Button("   Profile   ", (x/2+500, y/32), font=30, bg="navy")
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        button5.click(event, pygame.QUIT)
        button7.click(event, showProfile)
    scr.fill((32, 230, 174))

    button2.show()
    button1.show()
    button3.show()
    button4.show()
    button5.show()
    button6.show()
    button7.show()
    label1.show()
    label2.show()
    pic1.show()
    pygame.display.update()