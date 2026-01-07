
import pygame 
pygame.init()


#making the main loop 
w_width = 500
w_height= 500

screen = pygame.display.set_mode((w_width,w_height))
screen.fill("white")
pygame.display.set_caption("Adding Background")
x = 50
y= 435
width = 64 
height = 64
vel = 5
clock = pygame.time.Clock()
#jump variable 
is_jump = False
jump_count = 10 #jump power

done = True
bg_img = pygame.image.load("background_img.jpg")
bg_img = pygame.transform.scale(bg_img, (w_width, w_height))

#character
left = False #is person walking left or right 
right = False
walkCount = 0 

walkRight = [pygame.image.load(f'soldier/{i}.png') for i in range(1,10)]
walkLeft = [pygame.image.load(f'soldier/L{i}.png') for i in range(1,10)]
char = pygame.image.load('soldier/standing.png')

def DrawInGameLoop():
    screen.blit(bg_img,(0,0))
    clock.tick(60) #add this at the end to really affect frame rate 
    global walkCount
    if walkCount +1 >= 27:#make sure every image is display for 3 frames before other image i shows 9x3 
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    
    else: 
        screen.blit(char, (x,y))
    pygame.display.flip()

while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < w_width - width:
         x= x + vel
         right = True
         left = False
    else:
        left = False
        right = False
        walkCount = 0
    

    if not (is_jump): #if is jump is not true then player can do these 
     
        
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
    #Positive jump_count goes up, negative goes down, squaring makes it smooth
    else: #if jumping execute this part
        if is_jump:
            if jump_count >= -10: #starts at 10 and decreases by one jumps last from 10 -0 0-10
                neg = 1 #decides direction
                if jump_count < 0:#moving down > is moving up 
                    neg = -1
                y = y-(jump_count **2) * neg * 0.5 #move the chracter up or down by an amount that gets smaller over time/ **2 strong at first and strong when falling/ y=y-jumpcount to go higher
                jump_count = jump_count- 1 #each frame jump power gets weaker
            else:
                jump_count = 10 #jump is over reset jump power 
                is_jump = False


    DrawInGameLoop()