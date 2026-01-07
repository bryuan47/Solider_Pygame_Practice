import pygame 
pygame.init()


#making the main loop 

screen = pygame.display.set_mode((300,300))
screen.fill("white")
pygame.display.set_caption("Drawing Shapes")

pygame.draw.line(screen, "black", (0,0), (300,300), 5) #Where, color, start, stop, and width 
pygame.draw.line(screen, "orange", False, [(100,100), (200,100), (100,200)], 4 ) #multiple lines, if shape is open or close, points to start and end. 
pygame.draw.rect(screen, "red", (50,50, 100,100),7) #red rectangle, what point aand width and height, and pixels 
pygame.draw.circle(screen, "green", (200, 150), 50, 1)#width and radius of how many pixels from center and pixel thickness
pygame.draw.elipse(screen, "yellow", (300, 100, 100, 50), 4)#cordinates 300 x100. width of 100 px and height of 50px
pygame.draw.polygon(screen, "blue", ((250,75),(300,25), (350,75)), 1) # set edge width to 0 can fill with color



done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False


    pygame.display.flip()