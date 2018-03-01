import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Conversation')

#icon = pygame.image.load('Apple.png')
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (0,155,0)
light_green = (0,255,0)


clock = pygame.time.Clock()


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
medlarfont = pygame.font.SysFont("comicsansms", 60)
largefont = pygame.font.SysFont("comicsansms", 80)

#img = pygame.image.load('SnakeHead.png')
#appleimg = pygame.image.load('Apple.png')


def score(score):
    
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0, 0])
    

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "medlar":
        textSurface = medlarfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
                       

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def game_controls():
    
    gcont = True

    while gcont == True:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: Up and Down arrows", black, 10)
        message_to_screen("Move Tank: Left and Right arrows", black, 50)
        message_to_screen("Pause: P", black, 90)


        button("play",150,500,100,50, green, light_green, action="play")
        button("Main",350,500,100,50, yellow, light_yellow, action="main")
        button("quit",550,500,100,50, red, light_red, action="quit")


        
        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
                
            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)


def pause():

    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

            elif event.key == pygame.K_q:
                pygame.quit()
                quit()



        clock.tick(5)


def game_intro():

    intro = True

    while intro == True:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to 'Pygame Conversation'", green, -100, "medlar")
        message_to_screen("This program is supposed to simulate", black, -30)
        message_to_screen("a, somewhat, realistic converstaion with another human being.", black, 10)
        message_to_screen("All you have to do to succeed in this simulation is to.", black, 50)
        message_to_screen("avoid annoying the robot.", black, 90)
        message_to_screen("Good Luck:)", black, 130, "medium")
        #message_to_screen("Press C to play, P to pause, or Q to quit", black, 180)


        button("play",display_width/2 -100,700,100,50, green, light_green, action="play")
        #button("controls",350,700,100,50, yellow, light_yellow, action="controls")
        button("quit",display_width/2 +25,700,100,50, red, light_red, action="quit")


        
        pygame.display.update()

        clock.tick(15)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
    
    while not gameExit:

        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",red,y_displace=-50,size="large")
            message_to_screen("Press C to play again or Q to quit",black,50,size="medium")
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                
                elif event.key == pygame.K_ENTER:
                    pass
                    
                elif event.key == pygame.K_UP:
                    pass
                    
                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)
        tank(mainTankX,mainTankY)


        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()

