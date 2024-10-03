import pygame
import numpy as np
import os


pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()


rect = pygame.Rect(0, 0, 200, 100)
rect1 = pygame.Rect(251, 0, 200, 100)
rect2 = pygame.Rect(501, 0, 200, 100)
rect3 = pygame.Rect(751,0,200,100)

brect = pygame.Rect(0, 150, 800, 100)


player = pygame.Rect(0, 100, 50, 50)

bound1 = pygame.Rect(0, 0, 800, 10)

mult = 1
                #num
win = pygame.Rect(450,0,50,30) #edit the first num if you wanna chnage the square to another path

moves = np.array([])
if os.path.exists('moves.npy'):
    mv = np.load("moves.npy")[0]

while True:
    
   
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    pygame.draw.rect(screen, "red", rect)
    pygame.draw.rect(screen, "red", rect1) #walls
    pygame.draw.rect(screen, "red", rect2)
    pygame.draw.rect(screen, "red", rect3)


    pygame.draw.rect(screen,"green",win)


    pygame.draw.rect(screen, "red", brect)
    pygame.draw.rect(screen,"grey",bound1)
 


    pygame.draw.rect(screen, "blue", player)
    
    
    
    if os.path.exists('moves.npy'):


        if mv >= 1:
            player.x += 1
            mv -= 1
        elif mv < 1:
            player.y -= 1

        if player.colliderect(win):
            player.y += 1



    else:
        player.y -= 1 * mult
            
        if player.colliderect(rect) or player.colliderect(rect1) or player.colliderect(rect2) or player.colliderect(rect3):
        
            player.y += 1
            player.x += 1
            mult = 1
        
        elif player.colliderect(brect):
            player.y -= 1
            player.x += 2
            mult = 1
            u = False
            f = True
        
        if player.colliderect(bound1):
            mult = -1


        if player.colliderect(win):
            moves = np.append(moves,player.x)
            np.save("moves.npy",moves)
            pygame.quit()

    pygame.display.update()
    clock.tick(60)