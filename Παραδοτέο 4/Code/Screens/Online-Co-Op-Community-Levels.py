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
button0 = Button("Create your Own Level", (x / 8.6, y / 6), font=40, bg="navy")
button1 = Button("Lobby", (2.7 * x / 3.9, y / 32), font=30, bg="navy")
button2 = Button("Community Levels", (3 * x / 4, y / 32), font=30, bg="light green")
button3 = Button("Search", (x / 1.55, y / 5.5), font=30, bg="navy")

button4 =Button("    Back    ", (x/9.5,  y/4+450), font=30, bg="navy")
button5 = Button("Download", (x / 1.45, y / 2.75), font=35, bg="navy")

label1 = Label("Available Levels", (x/8+350, y/3.5), myfont, "navy")
label2 = Label("#1111", (x/7, y/6+150),pygame.font.SysFont("Arial", 30), "navy")
label3 = Label("usernameOfCreator", (x/4, y/6+150), pygame.font.SysFont("Arial", 30), "navy")
label4 = Label("Screenshots", (x/2.15, y/6+150), pygame.font.SysFont("Arial", 38), "navy")
label5 = Label("Total downloads: 9999",(x / 1.45, y / 2.40),pygame.font.SysFont("Arial", 15), "navy")

inputt=pygame.Rect(x / 8 + 800, y / 6 + 10, 200, 35)

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
    button5.show()
    label1.show()
    label2.show()
    label3.show()
    label4.show()
    label5.show()
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 9.4, y / 11, 1100, 550), 2)  #big rectangle
    pygame.draw.rect(screen, color, inputt)  #textbox
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 8, y / 2.8, 1025, 65), 2) #thin rectangle
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 2.25, y / 2.75, 240, 40), 2) # screenshots box
    pygame.draw.rect(screen, "navy", pygame.Rect(x / 8.5, y / 2.9, 1070, 345), 2)

    pygame.draw.rect(screen, "white", pygame.Rect(x / 8+1038, y / 6 + 140, 15, 335))  #scrollbar
    pygame.draw.rect(screen, "dark grey", pygame.Rect(x / 8 + 1039, y / 6 + 140, 13, 90))  #scrollbar
    text_surface = pygame.font.SysFont("Arial", 28).render(user_text, True, "black")
    inputt.w = max(250, text_surface.get_width() + 10)
    screen.blit(text_surface, (inputt.x + 5, inputt.y + 5))
    pygame.display.update()
