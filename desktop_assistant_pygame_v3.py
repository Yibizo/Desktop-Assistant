import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()

mainClock = pygame.time.Clock()

screen_width = 800
screen_height = 600
monitor = [pygame.display.Info().current_w,pygame.display.Info().current_h]
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)

pygame.display.set_caption("Desktop Assitant")
#"Icon made by Freepik from www.flaticon.com"
icon = pygame.image.load("bot.png")
pygame.display.set_icon(icon)

def text_display(text,x,y,size):
    font = pygame.font.SysFont("Lucida Console",size)
    showText = font.render(text,True,(255,255,255))
    screen.blit(showText,(x,y))

def center_text_display(text,size):
    font = pygame.font.SysFont("Lucida Console",size)
    showText = font.render(text,True,(255,255,255))
    text_rect = showText.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(showText,text_rect)

def end_program():
    pygame.quit()
    sys.exit()

fullscreen = False

allTxt = ""
command = ""
while True:
    screen.fill((0,0,0))
    file = open("desk_text.txt","r")
    if os.stat("desk_text.txt").st_size != 0:
        allTxt = file.readlines()[0]
        tempList = allTxt.split(" ")
        command = tempList[0]
    center_text_display(command,int(screen.get_height()/20))
    file.close()
    file = open("desk_text.txt","r+")
    file.truncate(0)
    file.close()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_program()
        if event.type == pygame.VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end_program()
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor,pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),pygame.RESIZABLE)

    pygame.display.update()
    mainClock.tick(60)