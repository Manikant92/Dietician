import pygame
from pygame.locals import *
import os


# Game Initialization
pygame.init()

# Center the Game Application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Game Resolution
screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Text Renderer


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "assets/font/HyFWoolBall-2.ttf"

# Main Menu image

picture = pygame.image.load("assets/image/foods/background.png")
picture = pygame.transform.scale(picture, (screen_width, screen_height))
screen.blit(picture, (0, 0))


# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Main Menu


def startGameMenu():

    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected != "back":
                    selected = "start"
                elif event.key == pygame.K_DOWN and selected != "start":
                    selected = "back"
                elif event.key != pygame.K_RETURN:
                    selected = "practice"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        # start the game
                        print("Start")

                    if selected == "back":
                        print("back")

                    if selected == "practice":
                        # 给出记录
                        print("practice")

        # Main Menu UI

        title = text_format("Please Start The Game", font, 90, white)
        menu = text_format("Menu", font, 85, white)

        # select start in the menu
        if selected == "start":
            text_start = text_format(
                "Start" + " " * 16 + "1", font, 75, yellow)
        else:
            text_start = text_format("Start" + " " * 16 + "1", font, 75, white)

        # select practice in the menu
        if selected == "practice":
            text_practice = text_format(
                "Practice" + " " * 12 + "2", font, 75, yellow)
        else:
            text_practice = text_format(
                "Practice" + " " * 12 + "2", font, 75, white)

        # select back in the menu
        if selected == "back":
            text_back = text_format("Back" + " " * 17 + "3", font, 75, yellow)
        else:
            text_back = text_format("Back" + " " * 17 + "3", font, 75, white)

        title_rect = title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 20))
        screen.blit(text_start, (screen_width / 6, 180))
        screen.blit(text_practice, (screen_width / 6, 280))
        screen.blit(text_back, (screen_width / 6, 380))
        pygame.display.update()
        clock.tick(FPS)

        pygame.display.set_caption("Dietician-Expert")


# Initialize the Game
startGameMenu()
