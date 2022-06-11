import pygame
import sys

screen = pygame.display.set_mode((1910, 1060),pygame.FULLSCREEN)
x, y = screen.get_size()
# Title
pygame.display.set_caption('Online Co-Op')

# initialise game
pygame.init()

myfont = pygame.font.SysFont("Arial", 45, bold=True)
label = myfont.render("Welcome to", False, (255, 255, 255))

class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

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
        screen.blit(self.font.render(self.text, False, (self.color)), (self.x, self.y))


class Picture:
    def __init__(self, imagePath, pos) -> None:
        self.imagePath = imagePath
        self.x, self.y = pos

    def show(self) -> None:
        screen.blit(pygame.image.load(self.imagePath), (self.x, self.y))

user_text=""
button0 = Button("Create your Own Room", (x/8, y/5-50), font=40, bg="navy")
button1 = Button("        Lobby        ", (x/8+630, y/5-120), font=30, bg="light green")
button2 = Button("Community Levels", (x/8+850, y/5-120), font=30, bg="navy")
button3 = Button("  Search  ", (x/8+700, y/5-50), font=30, bg="navy")
button4 =Button("    Back    ", (x/8-40,  y/5+500), font=30, bg="navy")

label1 = Label("Available Rooms", (x/8+350, y/5+10), myfont, "navy")
label2 = Label("#1111", (x/8+80, y/5+105),pygame.font.SysFont("Arial", 30), "navy")
label3 = Label("usernameOfHost", (x/8+180, y/5+105), pygame.font.SysFont("Arial", 30), "navy")
label4 = Label("LevelPlaying", (x/8+500, y/5+100), pygame.font.SysFont("Arial", 30), "navy")
label5 = Label("NumOfPlayersConnected",(x/5+600, y/5+100),pygame.font.SysFont("Arial", 30), "navy")

inputt=pygame.Rect(x/8+800, y/5-50, 200, 35)

color_active = pygame.Color((250,250,250))
color_passive = pygame.Color('white')
color = color_passive
active = False
active_check=False

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button4.click(event, pygame.QUIT)
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

    screen.fill((32, 230, 174))

    button0.show()
    button1.show()
    button2.show()
    button3.show()
    button4.show()
    label1.show()
    label2.show()
    label3.show()
    label4.show()
    label5.show()
    pygame.draw.rect(screen, "navy", pygame.Rect(x/8-40, y/5-60, 1100, 550), 2)  #big rectangle
    pygame.draw.rect(screen, color, inputt)  #textbox
    pygame.draw.rect(screen, "navy", pygame.Rect(x/8-10, y/5+90, 1025, 50), 2)
    pygame.draw.rect(screen, "navy", pygame.Rect(x/8-20,y/5+80, 1070, 345), 2)
    pygame.draw.rect(screen, "white", pygame.Rect(x/8+ 1030, y/5+83, 15, 335))  #scrollbar
    pygame.draw.rect(screen, "dark grey", pygame.Rect(x/8+1031, y/5+85, 13, 90))  #scrollbar
    text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")


    inputt.w = max(250, text_surface.get_width() + 10)
    screen.blit(text_surface, (inputt.x + 5, inputt.y + 5))
    pygame.display.update()
