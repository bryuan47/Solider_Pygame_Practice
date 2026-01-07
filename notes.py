'''import pygame, sys
from pygame.locals import *

clock= pygame.time.Clock()

#setting up pygame 
pygame.init()

#setting up colors 
BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)

#set up window 
windowSurface = pygame.display.set_mode((500,400))
pygame.display.set_caption("Hello World")

#set up fonts 
basic_font = pygame.font.SysFont(None,48)

#set up the text 
text= basic_font.render("Hello World", True, BLUE, RED)

#location of text 
textRect = text.get_rect()
pygame.draw.rect(windowSurface, (0,255,255), textRect )
windowSurface.blit(text, textRect)'''











''''
#Test 
run = True 
while run:
    clock.tick(60)
    windowSurface.fill((255,255,255))



    text= basic_font.render("Hello World", True, BLUE, RED)
    textRect = text.get_rect()
    textRect.topleft = (0,0)
    pygame.draw.rect(windowSurface, (0,255,255), textRect )
    windowSurface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    pygame.display.flip()'''

