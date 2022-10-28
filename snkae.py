import pygame
import random
from pygame.locals import *
import time
from pygame import mixer


pygame.init()
pygame.mixer.init()

screenwid = 500
screenhigh = 400
screen = pygame.display.set_mode((screenwid, screenhigh))

bgcolor = (0,128,0)

pygame.display.update()

pygame.display.set_caption(' RETRO SNAKE')
icon = pygame.image.load('E:/snkae/snakeicon.png')
pygame.display.set_icon(icon)

green = (0,128,0)
yellow = (255, 215,0)
black = (0,0,0)
white = (255, 255, 255)
red = (204,0,0)
blue = (100, 230, 220)

#initvel = 3

snksize = 15

mixer.music.load("E:/snkae/snkmusic.wav")
mixer.music.play(-1)

image = pygame.image.load('E:/snkae/bg grass.jpg')
image = pygame.transform.scale(image, (500, 400))

foodw = 10
foodh = 10

clock = pygame.time.Clock()

textx = 30
texty = 30

bgscreen = pygame.image.load('E:/snkae/bg grass.jpg')
bgscreen = pygame.transform.scale(bgscreen, (500,400))

boundary = pygame.image.load('E:/snkae/boundary.png')

replay = pygame.image.load('E:/snkae/REPLAYFINALL.png')
replay = pygame.transform.scale(replay, (250, 250))

Quit = pygame.image.load('E:/snkae/QUITBUTTON.png')
Quit = pygame.transform.scale(Quit, (250, 250))

ulost = pygame.image.load('E:/snkae/you losst.png')
ulost = pygame.transform.scale(ulost, (300, 300))

scorefonr = pygame.font.Font('E:/python_work/font/upheavtt.ttf', 20)

font = pygame.font.Font('E:/python_work/font/Pixellari.ttf', 40)

msgfont = pygame.font.Font('E:/python_work/font/baby blocks.ttf', 30)

msgboundfont = pygame.font.Font('E:/python_work/font/baby blocks.ttf', 15)

pikupsound = mixer.Sound('E:/snkae/snkaefoodpikup.wav')

movesound = mixer.Sound('E:/snkae/snkaemove.wav')

selectsound = mixer.Sound('E:/snkae/selection.wav')


def plotsnk(screen, color,  snklist, snksize):
    for x,y in snklist:
        pygame.draw.rect(screen ,white, [x, y ,snksize, snksize])
        for i in range(4):
            pygame.draw.rect(screen, black, (x-i,y-i,15,15), 1)
        

def msgbound(msg,color):
    mesg = msgboundfont .render(msg, True, color)
    screen.blit(mesg, [140, 150])


def main():
    while True:
        
        #screen.fill(green)
        screen.blit(bgscreen, (0,0))
        
        screen.blit(image,(0,0))

        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
        highscore = scorefonr.render('highscore : ' + str(hiscore), True, (0,0,0))
        screen.blit(highscore, [190, 290])
        
        play = pygame.image.load('E:/snkae/PLAYBUTTON.png')
        play = pygame.transform.scale(play, (250, 250))
        screen.blit(play, (130,  50))

        end = pygame.image.load('E:/snkae/QUITBUTTON.png')
        end = pygame.transform.scale(end, (250, 250))
        screen.blit(end, (130,  160))

        cover = pygame.image.load('E:/snkae/snake mainmenu pic.png')
        cover = pygame.transform.scale(cover, (420, 420))
        screen.blit(cover, (70,-55))

        boundary = pygame.image.load('E:/snkae/boundary.png')
        screen.blit(boundary, [0,0])

        sponsor = msgboundfont.render('Ali productions®', True, white)
        screen.blit( sponsor, [180, 380])
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                #print(mx, my)
                if my < 162 and my > 103 and mx > 205 and mx < 320:
                    gameloop()
                    selectsound.play()
                if my < 272 and my > 230 and mx > 201 and mx < 310:
                    pygame.quit()
                    selectsound.play()
                    
        clock.tick(100)
        pygame.display.update()

def gameloop():
    gameover = False
    gameclose= False

    initvel = 3

    x = screenwid / 2
    y = screenhigh / 2

    scorex = 27
    scorey = 28
    
    xchange = 0
    ychange = 0

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        
    scorevalue = 0
    def show_score(x, y):
        score = scorefonr .render('score : ' + str(scorevalue), True, (0, 0, 0))
        screen.blit(score, (x, y))
    
    def message(msg,color):
        mesg = msgfont .render(msg, True, color)
        screen.blit(mesg, [150, 150])
    
    snklist = []
    snklen = 1

    foodx = random.randint(27, 450)
    foody = random.randint(28, 350)
    
    while not gameover:
        
        while gameclose:

            screen.blit(bgscreen, (0,0))
            
            screen.blit(image,(0,0))
            
            screen.blit(boundary, [0,0])
            
            screen.blit(replay, [10, 60])

            screen.blit(Quit, [250, 60])

            screen.blit(ulost, [110, 10])

            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            show_score(190, 240)
            highscore = scorefonr.render('highscore : ' + str(hiscore), True, (0,0,0))
            screen.blit(highscore, [190, 260])
            
            sponsor = msgboundfont.render('Ali productions®', True, white)
            screen.blit( sponsor, [180, 380])

            note = font.render('press esc for main menu', True, black)
            note = pygame.transform.scale(note, (330,25))
            screen.blit(note, [90, 320])
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                        pygame.quit()
                    if event.key == pygame.K_p:
                        gameloop()
                        selectsound.play()
                    if event.key == pygame.K_ESCAPE:
                        main()
                        selectsound.play()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print(mx, my)
                    if my < 170 and my > 120 and mx > 65 and mx < 190:
                        gameloop()
                        selectsound.play()
                    if my < 180 and my > 120 and mx > 305 and mx < 430:
                        gameover = True
                        gameclose = False
                        pygame.quit()
                        selectsound.play()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and xchange != initvel:
                    xchange = -initvel
                    ychange =  0
                    movesound.play()
                elif event.key == pygame.K_RIGHT and xchange != -initvel:
                    xchange = initvel
                    ychange = 0
                    movesound.play()
                elif event.key == pygame.K_UP and ychange != initvel:
                    ychange = -initvel
                    xchange = 0
                    movesound.play()
                elif event.key == pygame.K_DOWN and ychange != -initvel:
                    ychange = initvel
                    xchange = 0
                    movesound.play()
                elif event.key == pygame.K_a:
                    xchange = -initvel
                    ychange = 1
                    movesound.play()
                elif event.key == pygame.K_d:
                    xchange = 1
                    ychange = 1
                    movesound.play()

        if x >= 468 or x < 27 or y >= 372 or y < 27:
            gameclose = True

        x += xchange
        y += ychange                   

        if abs(x - foodx) <20 and abs(y - foody) <20:
            scorevalue += 1
            foodx = random.randint(30, 465)
            foody = random.randint(30, 360)
            snklen += 5
            pikupsound.play()
            initvel += 0.02
            if scorevalue > int(hiscore):
                hiscore = scorevalue
            print(hiscore)
            
        screen.blit(bgscreen, (0,0))
        
        show_score(textx, texty)

        food = pygame.image.load('E:/snkae/apple1.png')
        food = pygame.transform.scale(food, (200,150))
        screen.blit(food, [foodx - 83, foody - 70])

        screen.blit(boundary, [0,0])

        snkhead = []
    
        snkhead.append(x)
        snkhead.append(y)
        snklist.append(snkhead)    

        if len(snklist) > snklen:
            del snklist[0]
        
        for i in snklist[:-1]:
                if i == snkhead:
                    gameclose= True
                
        plotsnk(screen, black, snklist, snksize)
 
        pygame.display.update()
        clock.tick(60)
main()
 
pygame.quit()



                

     
       

  





