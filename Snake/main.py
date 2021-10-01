import pygame
from pygame.locals import * 
import random 

def on_grid_random():
    x = random.randint(100,300)
    y = random.randint(100,300)
    return (x//10*10, y//10*10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def cobra_colisao(x1,x2):
    return(x1[0]== x2[0]) and (x1[1]==x2[1])


def newColorSnake():
    x = random.randint (0,255)
    y = random.randint (0,255)
    z = random.randint (0,255)
    return (x,y,z)   

cima = 0
direita = 1
abaixo = 2
esquerda = 3


pygame.init()
width,height = 500,500
tela = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake')

cobra = [(200,200),(210,200),(220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill(newColorSnake()) #Cor rgb


maca = pygame.Surface((10,10))
maca.fill(newColorSnake())
maca_posicao = on_grid_random()

direcao = esquerda
clock = pygame.time.Clock()


while True:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == KEYDOWN:
        if event.key == K_UP:
            direcao = cima

    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            direcao = abaixo


    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            direcao = esquerda


    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            direcao = direita                   


    if collision(cobra[0], maca_posicao):
        maca_posicao = on_grid_random()
        cobra.append((0,0))

   
        
           

    for i in range(len(cobra) -1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if direcao == cima:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if direcao == abaixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)    
    
    if direcao == direita:
        cobra[0] = (cobra[0][0] +10, cobra[0][1])

    if direcao == esquerda:
        cobra[0] = (cobra[0][0] -10, cobra[0][1])    

    tela.fill((0,0,0))
    tela.blit(maca, maca_posicao)
    
    for pos in cobra:
        tela.blit(cobra_skin,pos)

    pygame.display.update()       