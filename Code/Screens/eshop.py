import pygame
import sys

scr = pygame.display.set_mode((1910, 1060), pygame.FULLSCREEN)
x, y = scr.get_size()
#Title
pygame.display.set_caption('Area 15 Welcome!')
clock = pygame.time.Clock()

#initialise game
pygame.init()
myfont = pygame.font.SysFont("Segoe UI", 60,bold=True)
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
label1 = Label("E-shop", (x/2-100, y/10-50), myfont, "navy")
label2 = Label("Item_name", (x/2-560, y/10+160),pygame.font.SysFont("Arial", 30), "navy")
label3 = Label("Today's Offers", (x/2-570, y/10+110), pygame.font.SysFont("Arial", 30), "navy")
label4 = Label("Item_name by @username", (x/2-570, y/10+360), pygame.font.SysFont("Arial", 24), "navy")
label5 = Label("Players' Offers", (x/2-570, y/10+310), pygame.font.SysFont("Arial", 30), "navy")
label6 = Label("Cost:       99/2", (x/2-560, y/10+220),pygame.font.SysFont("Arial", 25), "navy")
label7 = Label("Winning Bid:        80", (x/2-570, y/10+390), pygame.font.SysFont("Arial", 24), "navy")
label8 = Label("Buyout Price:       99/150", (x/2-570, y/10+420), pygame.font.SysFont("Arial", 24), "navy")

pic1 = Picture('.\Code\Screens\images\coin.png', (x/2-505, y/10+220))
pic2 = Picture('.\Code\Screens\images\coin.png', (x/2-450, y/10+389))
pic3 = Picture('.\Code\Screens\images\coin.png', (x/2-450, y/10+422))

button1 = Button("              Create your own offer             ", (x/2-230,  y/10+550), font=30, bg="navy") 
button2 = Button("    Back    ", (x/8,  y/10+600), font=30, bg="navy")
inputt=pygame.Rect(x/2-395,y/10+392,50,25)

color_active = pygame.Color((250,250,250))
color_passive = pygame.Color('white')
color = color_passive
active = False

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        button2.click(event, pygame.QUIT)
        if event.type == pygame.MOUSEBUTTONDOWN:
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

    button2.show()
    button1.show()
    label1.show()
    label2.show()
    label3.show()
    label4.show()
    label5.show()
    label6.show()
    label7.show()
    label8.show()
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-40,y/10+80,1200,600),2) #big rectangle
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-12,y/10+150,1150,120),2) #medium1 rectangle
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-12,y/10+350,1150,120),2) #medium2 rectangle
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-6,y/10+155,250,110),2) #small1 rectangle
    pygame.draw.rect(scr,"navy", pygame.Rect(x/8-6,y/10+355,250,110),2) #small2 rectangle

    pygame.draw.rect(scr, "white", pygame.Rect(x/8-10, y/10+280, 1140, 15))  #scrollbar
    pygame.draw.rect(scr, "dark grey", pygame.Rect(x/8-9, y/10+281, 90, 13))  #scrollbar

    pygame.draw.rect(scr, "white", pygame.Rect(x/8-10, y/10+480, 1140, 15))  #scrollbar
    pygame.draw.rect(scr, "dark grey", pygame.Rect(x/8-9, y/10+481, 90, 13))  #scrollbar

    pygame.draw.rect(scr,color, inputt) #buyout
    text_surface = pygame.font.SysFont("Arial", 20).render(user_text, True, "black")
    inputt.w = max(40, text_surface.get_width()+10)
    scr.blit(text_surface, (inputt.x+5, inputt.y+5))
    pic1.show()
    pic2.show()
    pic3.show()
    pygame.display.update()
    clock.tick(60)