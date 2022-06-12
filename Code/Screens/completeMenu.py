
import pygame
import sys

pathToImages = 'Code\Screens\images\\'

color_active = pygame.Color((250,250,250))
color_passive = pygame.Color('white')
color = color_passive
color_check_active= pygame.Color((31, 199, 0))
color_check_passive= pygame.Color("red")
color_check = color_check_passive
active_check=False

clock = pygame.time.Clock()

def quitP():
    pygame.quit()
    sys.exit()

scr = pygame.display.set_mode((1910, 1060), pygame.FULLSCREEN)
x, y = scr.get_size()


'''Global Variables'''
pagesInputts = [None, pygame.Rect(x/2+260,y/10+30,300,35), pygame.Rect(x/8+800, y/5-50, 200, 35), pygame.Rect(x/8+800, y/5-50, 200, 35), pygame.Rect(x/2-395,y/10+392,50,25), pygame.Rect(x/8+260,y/6+250,300,35), None]
pageSelectors = [True, False, False, False, False, False, False]

check=pygame.Rect(x/8+300,y/6+350,60,35)

#Title
pygame.display.set_caption('Area 15 Welcome!')
icon = pygame.image.load(pathToImages+'logo.png')

#initialise game
pygame.init()
startingImg = pygame.image.load(pathToImages+'logo.png')

myfont = pygame.font.SysFont("Segoe UI", 60, bold = True)
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

    def click(self, event, func, attr = None):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if func is not None:
                        func()
                    elif attr is not None:
                        global pageSelectors
                        for i in range(len(pageSelectors)):
                            pageSelectors[i] = False
                        pageSelectors[attr] = True
                        global inputt
                        inputt = pagesInputts[attr]



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


#starting screen
label1 = Label("Welcome to", (x/2-170, y/2-420), myfont, ("navy"))
pic1 = Picture(pathToImages+'logo.png', (x/2-120, y/2-350))
label2 = Label("Start your escape", (x/2-230, y/2-150), myfont, ("navy"))
button1 = Button("       New Game       ",(x/2-120, y/2),font=30,bg="navy")
button2 = Button("       Load Game      ", (x/2-120, y/2+80), font=30, bg = "navy")
button3 = Button("      Online co-op      ", (x/2-120, y/2+160), font=30, bg = "navy")
button4 = Button("          Settings         ", (x/2-120, y/2+240), font=30, bg="navy")
button5 = Button("          Exit         ", (x/2-100, y/2+320), font=30, bg="navy") 
button6 = Button("   E-shop   ", (x/2+350, y/32), font=30, bg="navy")
button7 = Button("   Profile   ", (x/2+500, y/32), font=30, bg="navy")
user_text=""

#profile page


label21 = Label("Profile", (x/2-100, y/10-50), myfont, "navy")
label22 = Label("Username: .......", (x/2-100, y/10+320),pygame.font.SysFont("Arial", 30), "navy")
label23 = Label("Search for players", (x/2+270, y/10), pygame.font.SysFont("Arial", 20), "navy")
pic21 = Picture(pathToImages+'\\anonymous.jpg', (x/2-140, y/10+30))
button21 = Button("              Friends             ", (x/2-140,  y/10+380), font=30, bg="navy") 
button22 = Button("    Back    ", (x/2-600,  y/10+600), font=30, bg="navy")
button23 = Button("             Trophies            ", (x/2-140, y/10+450), font=30, bg="navy")



#online co-op lobby
user_text=""
button30 = Button("Create your Own Room", (x/8, y/5-50), font=40, bg="navy")
button31 = Button("        Lobby        ", (x/8+630, y/5-120), font=30, bg="light green")
button32 = Button("Community Levels", (x/8+850, y/5-120), font=30, bg="navy")
button33 = Button("  Search  ", (x/8+700, y/5-50), font=30, bg="navy")
button34 =Button("    Back    ", (x/8-40,  y/5+500), font=30, bg="navy")

label31 = Label("Available Rooms", (x/8+350, y/5+10), myfont, "navy")
label32 = Label("#1111", (x/8+80, y/5+105),pygame.font.SysFont("Arial", 30), "navy")
label33 = Label("usernameOfHost", (x/8+180, y/5+105), pygame.font.SysFont("Arial", 30), "navy")
label34 = Label("LevelPlaying", (x/8+500, y/5+100), pygame.font.SysFont("Arial", 30), "navy")
label35 = Label("NumOfPlayersConnected",(x/5+600, y/5+100),pygame.font.SysFont("Arial", 30), "navy")



#online co-op comm levels
user_text=""
button40 = Button("Create your Own Level", (x/8, y/5-50), font=40, bg="navy")
button41 = Button("        Lobby        ", (x/8+630, y/5-120), font=30, bg="navy")
button42 = Button("Community Levels", (x/8+850, y/5-120), font=30, bg="light green")
button43 = Button("  Search  ", (x/8+700, y/5-50), font=30, bg="navy")

button44 =Button("    Back    ", (x/8-40,  y/5+500), font=30, bg="navy")
button45 = Button("   Download   ", (x/5+670, y/5+95), font=35, bg="navy")

label41 = Label("Available Levels", (x/8+350, y/5+10), myfont, "navy")
label42 = Label("#1111", (x/8+80, y/5+105),pygame.font.SysFont("Arial", 30), "navy")
label43 = Label("usernameOfCreator", (x/8+180, y/5+105), pygame.font.SysFont("Arial", 30), "navy")
label44 = Label("Screenshots", (x/8+500, y/5+100), pygame.font.SysFont("Arial", 38), "navy")
label45 = Label("Total downloads: 9999",(x/5+700, y/5+135),pygame.font.SysFont("Arial", 15), "navy")



#e-shop
user_text=""
label51 = Label("E-shop", (x/2-100, y/10-50), myfont, "navy")
label52 = Label("Item_name", (x/2-560, y/10+160),pygame.font.SysFont("Arial", 30), "navy")
label53 = Label("Today's Offers", (x/2-570, y/10+110), pygame.font.SysFont("Arial", 30), "navy")
label54 = Label("Item_name by @username", (x/2-570, y/10+360), pygame.font.SysFont("Arial", 24), "navy")
label55 = Label("Players' Offers", (x/2-570, y/10+310), pygame.font.SysFont("Arial", 30), "navy")
label56 = Label("Cost:       99/2", (x/2-560, y/10+220),pygame.font.SysFont("Arial", 25), "navy")
label57 = Label("Winning Bid:        80", (x/2-570, y/10+390), pygame.font.SysFont("Arial", 24), "navy")
label58 = Label("Buyout Price:       99/150", (x/2-570, y/10+420), pygame.font.SysFont("Arial", 24), "navy")

pic51 = Picture('.\\'+pathToImages+'coin.png', (x/2-505, y/10+220))
pic52 = Picture('.\\'+pathToImages+'coin.png', (x/2-450, y/10+389))
pic53 = Picture('.\\'+pathToImages+'coin.png', (x/2-450, y/10+422))

button51 = Button("              Create your own offer             ", (x/2-230,  y/10+550), font=30, bg="navy") 
button52 = Button("    Back    ", (x/8,  y/10+600), font=30, bg="navy")
inputt=pygame.Rect(x/2-395,y/10+392,50,25)



#e-shop Offer
user_text=""
label61 = Label("Create your own offer", (x/4+80, y/32), myfont, "navy")
label62 = Label("Item to sell:", (x/8, y/6+150),pygame.font.SysFont("Arial", 30), "navy")
label63 = Label("Buyout price:", (x/8, y/6+250), pygame.font.SysFont("Arial", 30), "navy")
label64 = Label("Support biding system", (x/8, y/6+350), pygame.font.SysFont("Arial", 30), "navy")
pic61 = Picture('.\\'+pathToImages+'coin.png', (x/8+210, y/6+250))
button61 = Button("              Choose From Inventory             ", (x/8+250,  y/6+150), font=30, bg="navy") 
button62 = Button("    Back    ", (x/8,  y/6+450), font=30, bg="navy")
button63 = Button("    Publish Offer    ", (x/8+900, y/6+350), font=30, bg="navy")


#game loop
running = True
while running:

    for event in pygame.event.get():
        button22.click(event, None, 0)
        button62.click(event, None, 4)   
        button3.click(event, None, 2)
        button7.click(event, None, 1)
        button6.click(event, None, 4)  
        button32.click(event, None, 3)    
        button44.click(event, None, 0)    
        button52.click(event, None, 0)  
        button51.click(event, None, 5) 
        button34.click(event, None, 0)
        button41.click(event, None, 2)
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        button5.click(event, pygame.QUIT) 

    if pageSelectors[0]:#starting screen
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
    
    elif pageSelectors[1]:#profile
        scr.fill((32, 230, 174))

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
        if active:
            color = color_active
        else:
            color = color_passive

        button22.show()
        button21.show()
        button23.show()
        label21.show()
        label22.show()
        label23.show()

        pygame.draw.rect(scr, color, inputt) #input      
        text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")
        inputt.w = max(250, text_surface.get_width()+10)
        scr.blit(text_surface, (inputt.x+5, inputt.y+5))
        pic21.show()

    elif pageSelectors[2]: #OnlineCo-op-Lobby
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputt.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string formation
                elif (event.key == pygame.K_RETURN):
                    save_text = user_text
                    user_text = " "
                else:
                    user_text += event.unicode


        scr.fill((32, 230, 174))

        button30.show()
        button31.show()
        button32.show()
        button33.show()
        button34.show()
        label31.show()
        label32.show()
        label33.show()
        label34.show()
        label35.show()
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-40, y/5-60, 1100, 550), 2)  #big rectangle
        pygame.draw.rect(scr, color, inputt)  #textbox
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-10, y/5+90, 1025, 50), 2)
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-20,y/5+80, 1070, 345), 2)
        pygame.draw.rect(scr, "white", pygame.Rect(x/8+ 1030, y/5+83, 15, 335))  #scrollbar
        pygame.draw.rect(scr, "dark grey", pygame.Rect(x/8+1031, y/5+85, 13, 90))  #scrollbar
        text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")


        inputt.w = max(250, text_surface.get_width() + 10)
        scr.blit(text_surface, (inputt.x + 5, inputt.y + 5))


    elif pageSelectors[3]:
        scr.fill((32, 230, 174))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputt.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string formation
                elif (event.key == pygame.K_RETURN):
                    save_text = user_text
                    user_text = " "
                else:
                    user_text += event.unicode

        button40.show()
        button41.show()
        button42.show()
        button43.show()
        button44.show()
        button45.show()
        label41.show()
        label42.show()
        label43.show()
        label44.show()
        label45.show()
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-40, y/5-60, 1100, 550), 2)  #big rectangle
        pygame.draw.rect(scr, color, inputt)  #textbox
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-10, y/5+90, 1025, 65), 2) #thin rectangle
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8+460, y/5+105, 240, 40), 2) # screenshots box
        pygame.draw.rect(scr, "navy", pygame.Rect(x/8-20,y/5+80, 1070, 345), 2)

        pygame.draw.rect(scr, "white", pygame.Rect(x/8+ 1030, y/5+83, 15, 335))  #scrollbar
        pygame.draw.rect(scr, "dark grey", pygame.Rect(x/8+1031, y/5+85, 13, 90))  #scrollbar
        text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")

        inputt.w = max(250, text_surface.get_width() + 10)
        scr.blit(text_surface, (inputt.x + 5, inputt.y + 5))

    elif pageSelectors[4]: #E-shop

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

        button52.show()
        button51.show()
        label51.show()
        label52.show()
        label53.show()
        label54.show()
        label55.show()
        label56.show()
        label57.show()
        label58.show()

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
        pic51.show()
        pic52.show()
        pic53.show()

    elif pageSelectors[5]:

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

        button62.show()
        button61.show()
        button63.show()
        label61.show()
        label62.show()
        label63.show()
        label64.show()

        pygame.draw.rect(scr,"navy", pygame.Rect(x/8-40,y/6+120,1200,300),2) #big rectangle
        pygame.draw.rect(scr,color, inputt) #buyout
        pygame.draw.rect(scr,color_check, check) #biding
        text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")
        inputt.w = max(250, text_surface.get_width()+10)
        scr.blit(text_surface, (inputt.x+5, inputt.y+5))
        pic61.show()

    pygame.display.update()
    clock.tick(60)