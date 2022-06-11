import pygame
import sys

scr = pygame.display.set_mode((1910, 1060), pygame.FULLSCREEN)
x, y = scr.get_size()
#Title
pygame.display.set_caption('Area 15 Welcome!')
clock = pygame.time.Clock()

#initialise game
pygame.init()
myfont = pygame.font.SysFont("Segoe UI", 60)
label = myfont.render("Welcome to", False, (255,255,255))

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

user_text=""
label1 = Label("Create your own offer", (x/4+80, y/32), myfont, "navy")
label2 = Label("Item to sell:", (x/8, y/6+150),pygame.font.SysFont("Arial", 30), "navy")
label3 = Label("Buyout price:", (x/8, y/6+250), pygame.font.SysFont("Arial", 30), "navy")
label4 = Label("Support biding system", (x/8, y/6+350), pygame.font.SysFont("Arial", 30), "navy")
pic1 = Picture('.\Code\Screens\images\coin.png', (x/8+210, y/6+250))
button1 = Button("              Choose From Inventory             ", (x/8+250,  y/6+150), font=30, bg="navy") 
button2 = Button("    Back    ", (x/8,  y/6+450), font=30, bg="navy")
button3 = Button("    Publish Offer    ", (x/8+900, y/6+350), font=30, bg="navy")
inputt=pygame.Rect(x/8+260,y/6+250,300,35)
check=pygame.Rect(x/8+300,y/6+350,60,35)

color_check_active= pygame.Color((31, 199, 0))
color_check_passive= pygame.Color("red")
color_check = color_check_passive
color_active = pygame.Color((250,250,250))
color_passive = pygame.Color('white')
color = color_passive
active = False
active_check=False

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        button2.click(event, pygame.QUIT)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check.collidepoint(event.pos):
                if(active_check == False):
                    active_check = True
                else:
                    active_check = False
            if inputt.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if active==True:
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string formation
                elif(event.key ==pygame.K_RETURN):
                    save_text=user_text
                    user_text=" "
                else:
                    user_text += event.unicode
    scr.fill((32, 230, 174))

    if active:
        color = color_active
    else:
        color = color_passive

    if active_check:
        color_check = color_check_active
    else:
        color_check = color_check_passive

    button2.show()
    button1.show()
    button3.show()
    label1.show()
    label2.show()
    label3.show()
    label4.show()
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-40,y/6+120,1200,300),2) #big rectangle
    pygame.draw.rect(scr,color, inputt) #buyout
    pygame.draw.rect(scr,color_check, check) #biding
    text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")
    inputt.w = max(250, text_surface.get_width()+10)
    scr.blit(text_surface, (inputt.x+5, inputt.y+5))
    pic1.show()
    pygame.display.update()
    clock.tick(60)