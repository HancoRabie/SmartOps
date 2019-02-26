import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 600


black = (0,0,0)
white = (255,255 ,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

player_width = 22
player_height = 32

gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Smart Ops')
clock = pygame.time.Clock()

playerImg = pygame.image.load('PixelMale.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def player(x,y):
    gameDisplay.blit(playerImg,(x,y))

def text_objects(text, font, color):
    textSurf = font.render(text, True, blue)
    return textSurf, textSurf.get_rect()
    
def message_display(text):
    
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, TextRect = text_objects(text, largeText, blue)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def switchScreen():
    message_display("Retry...")



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        player(x,y)

        # If player touches screen on left or right, show Retry
        if x > display_width - player_width or x < 0:
            switchScreen()
        

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
        
        # if y < thing_starty+thing_height


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
