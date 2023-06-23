import tkinter
import pygame
import random
import time
from pygame import mixer
root = tkinter.Tk()
root.withdraw()
width,height = root.winfo_screenwidth(),root.winfo_screenheight()











pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
rocket = pygame.image.load("rocket.png")
bullet = pygame.image.load("bullet.png")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")
enemy3 = pygame.image.load("enemy3.png")
enemy4 = pygame.image.load("enemy4.png")
menup = pygame.image.load("menu.png")
arrow = pygame.image.load("arrow.png")
quitb = pygame.image.load("quit.png")
replay = pygame.image.load("replay.png")
limit = pygame.image.load("limit.png")
run = True
x=500
y=630
left,right,stop = 0,1,2
dirr = stop
skin_list = [enemy1,enemy1,enemy2,enemy3,enemy4]
bullet_list = []
enemy_list = [[200,0],[400,0],[600,0],[800,0],[1000,0]]
enemy_dirr_list = []
for i in range(len(enemy_list)):
    enemy_dirr_list.append(left)
b_x = 0
b_y = 0
b_count = 0
enemy_dirr = left
scores = 0
MENU,GAME = 0,1
mode = GAME
m_x = 100
m_y = 100
clock = pygame.time.Clock()
mixer.init()
mixer.music.load("music.mpeg")
beep = pygame.mixer.Sound("beep.wav")
attack = pygame.mixer.Sound("attack.wav")
esc = pygame.mixer.Sound("esc.mp3")
mixer.music.play()
while run:
    screen.fill((0,0,0))
    pygame.mouse.set_visible(False)
    mousex,mousey = pygame.mouse.get_pos()
    screen.blit(limit,(0,504))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and mode == GAME:
                mode = MENU
                pygame.mixer.Sound.play(esc)
                pygame.mixer.music.pause()
            elif event.key == pygame.K_ESCAPE and mode == MENU and not enemy_list[i][1] > 404:
                mode = GAME
                pygame.mixer.Sound.play(esc)
                pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                dirr = left
            if event.key == pygame.K_RIGHT:
                dirr = right
            if event.key == pygame.K_SPACE:
                if b_count < 1:
                    pygame.mixer.Sound.play(beep)
                    b_x = x
                    b_y = y
                    bullet_list.append([b_x,b_y])
                    b_count += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dirr = stop
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex,mousey = pygame.mouse.get_pos()
            mouseleft,mousemiddle,mouseright = pygame.mouse.get_pressed()
            if mouseleft and mode == MENU:
                if mousey > 378 and mousey < 486 and mousex > 578 and mousex < 931:
                    run = False
            if mouseleft and mode == MENU:
                if mousey > 387 and mousey < 488 and mousex > 133 and mousex < 490:
                    scores = 0
                    enemy_list = [[200,0],[400,0],[600,0],[800,0],[1000,0]]
                    mode = GAME
                    pygame.mixer.music.play()
                    pygame.mixer.music.rewind()
            
    
    
    for pos in bullet_list:
        screen.blit(bullet,pos)
    if mode == GAME:
        for i in range(len(bullet_list)):
            bullet_list[i][1] -= 5
        for i in range(len(enemy_list)):
            if enemy_dirr_list[i] == left:
                enemy_list[i][0] -= 3
            if enemy_dirr_list[i] == right:
                enemy_list[i][0] += 3
            if enemy_list[i][0] < 0:
                enemy_list[i][1] += 100
                enemy_dirr_list[i] = right
            if enemy_list[i][0] > width-100:
                enemy_list[i][1] += 100
                enemy_dirr_list[i] = left
        if dirr == left:
            x-=3
        elif dirr == right:
            x+=3
        if x < 0:
            x = 0
        if x > width-100:
            x=width-100
    for i in range(len(skin_list)):
        screen.blit(skin_list[i],enemy_list[i])
    for i in range(len(enemy_list)):
        if enemy_list[i][1] > 404:
            mode = MENU
    if len(enemy_list) > len(skin_list):
        choose = random.randint(1,4)
        if choose == 1:
            skin_list.append(enemy1)
        if choose == 2:
            skin_list.append(enemy2)
        if choose == 3:
            skin_list.append(enemy3)
        if choose == 4:
            skin_list.append(enemy4)
    for i in range(b_count):
        if bullet_list[i][1] < 0:
            del bullet_list[i]
            b_count -= 1
            break
    for b_pos in range(len(bullet_list)):
        for e_pos in range(len(enemy_list)):
            if enemy_list[e_pos][1]+100 > bullet_list[b_pos][1] and bullet_list[b_pos][1]+100 > enemy_list[e_pos][1] and bullet_list[b_pos][0]+37 > enemy_list[e_pos][0] and bullet_list[b_pos][0]+61 < enemy_list[e_pos][0]+100:
                del enemy_list[e_pos]
                del bullet_list[b_pos]
                del skin_list[e_pos]
                b_count -= 1
                enemy_list.append([random.randrange(0,1000,100),random.randrange(-500,0,100)])
                scores += 1
                pygame.mixer.Sound.play(attack)
                break
    
    screen.blit(rocket,(x,630))
    font = pygame.font.SysFont("Ravie",30)
    scoretxt = font.render(str(scores),True,(127,127,127))
    labeltxt = font.render("score :",True,(127,127,127))
    screen.blit(labeltxt,(0,0))
    screen.blit(scoretxt,(200,0))
    if mode == MENU:
        screen.blit(menup,(m_x,m_y))
        screen.blit(scoretxt,(650,285))
        if mousey > 378 and mousey < 486 and mousex > 578 and mousex < 931:
            screen.blit(quitb,(578,378))
        if mousey > 387 and mousey < 488 and mousex > 133 and mousex < 490:
            screen.blit(replay,(133,387))
    screen.blit(arrow,[mousex,mousey])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
