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


def showCommunityLevels():
    running1 = True
    while running1:
        screen.fill((32, 230, 174))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1= False


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


button0 = Button("Create your Own Room", (x / 8.6, y / 6), font=40, bg="navy")
button1 = Button("Lobby", (2.7 * x / 3.9, y / 32), font=30, bg="light green")
button2 = Button("Community Levels", (3 * x / 4, y / 32), font=30, bg="navy")
button3 = Button("Search",(x / 1.55, y / 5.5), font=30, bg="navy")

button4 =Button("    Back    ", (x/9.5,  y/4+450), font=30, bg="navy")
label1 = Label("Available Rooms", (x/8+350, y/3.5), myfont, "navy")

label2 = Label("#1111", (x/7, y/6+150),pygame.font.SysFont("Arial", 30), "navy")
label3 = Label("usernameOfHost", (x/4, y/6+150), pygame.font.SysFont("Arial", 30), "navy")
label4 = Label("LevelPlaying", (x/2.2, y/6+150), pygame.font.SysFont("Arial", 30), "navy")
label5 = Label("NumOfPlayersConnected", (x/1.6, y/6+150), pygame.font.SysFont("Arial", 30), "navy")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button4.click(event, pygame.QUIT)
        button2.click(event,showCommunityLevels())
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
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 9.4, y / 11, 1100, 550), 2)  #big rectangle
    pygame.draw.rect(screen, "white", pygame.Rect(x / 8 + 800, y / 6 + 10, 200, 35))  #textbox
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 8, y / 2.8, 1025, 50), 2)
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 8.5, y / 2.9, 1070, 345), 2)

    pygame.draw.rect(screen, "white", pygame.Rect(x / 8+1038, y / 6 + 140, 15, 335))  #scrollbar
    pygame.draw.rect(screen, "dark grey", pygame.Rect(x / 8 + 1039, y / 6 + 140, 13, 90))  #scrollbar
    pygame.display.update()
