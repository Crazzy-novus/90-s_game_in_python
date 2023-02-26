import os
import sys
import pygame
import button
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colors
TEXT_COL = (255,255,255)

#load button images
def _resource_Path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

resume_img = _resource_Path("button_resume.png")
resume = pygame.image.load(resume_img)
clock=pygame.time.Clock()

options_img = _resource_Path("button_options.png")
option = pygame.image.load(options_img)
clock=pygame.time.Clock()

quit_img = _resource_Path("button_quit.png")
quit1 = pygame.image.load(quit_img)
clock=pygame.time.Clock()


#create button instances
resume_button = button.Button(304, 125, resume, 1)
options_button = button.Button(297, 250, option, 1)
quit_button = button.Button(336, 375, quit1, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
draw_text("press SPACE to pause", font, TEXT_COL,160,50)
pygame.display.update()
#game loop
run = True
while run:

    #screen.fill((52, 78, 91))

    #check if game is paused 
    if game_paused  == True:
        if resume_button.draw(screen):
            game_paused = False
        if options_button.draw(screen):
            game_paused = False
        if quit_button.draw(screen):
            run = False
            pygame.quit()
        #display menu
    else:
        draw_text("press SPACE to pause", font, TEXT_COL,160,250)
    #event handler
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
            exit()

    pygame.display.update()

pygame.quit()