'''

************** started on 8/05/2022 ****************
               last modified on 11/05/2022
**************   initialization     *****************
'''
#  ******** initializations the tables row & column & width & height of each box *********
column=''
rows=5

# *************** initialization of screen ***************

from turtle import Screen, Turtle, bgcolor, color, pos, position
import button
import pygame
import random
import os
import sys
from network import Network
pygame.init()
WIDTH =1300
HEIGHT=700
global game_paused
pygame.init() 
def main():
    # ********** command to set display ********** #
    screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
    

    # ********** command to load image  ********** #

    def _resource_Path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    image_path = _resource_Path("picsart3.png")
    gun=pygame.image.load(image_path)
    clock=pygame.time.Clock()

    # ************** adding heading *************** #
    pygame.display.set_caption("dv games")

    # *************** screen colour *************** #
    color=(0,0,0)
    highlight_box =(96,163,217)
    rect_color=(5,10,48)
    cross_line_colour =(225,231,224)
    object_colour=(4,118,208)
    highlight_text1 = (14,134,212)
    highlight_text2 = (236,248,127)
    # ******** the text features ******* #

    base_font = pygame.font.SysFont('system',32)
    random_text_x = 10
    random_text_y = 5

    # ********** function for displaying text ********** #
    def _show_Text(x,y,word="",random_number ="",row_number=""):
        number = base_font.render(word+ str(random_number)+str(row_number),True,(255,255,255))
        screen.blit(number,(x,y))
        pygame.display.update()


    # ********* pause function *********** #
    def pause(game_paused):
        
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
        resume_button = button.Button(300, 710, resume, .8)
        options_button = button.Button(600, 710, option, .8)
        quit_button = button.Button(900, 710, quit1, .8)
    

        #game loop
        run = True
        while run:

            #check if game is paused 
            if game_paused  == True:
                if resume_button.draw(screen):
                    pygame.draw.rect(screen,color,pygame.Rect(300,710,200,100))
                    pygame.draw.rect(screen,color,pygame.Rect(600,710,200,100))
                    pygame.draw.rect(screen,color,pygame.Rect(900,710,200,100))
                    pygame.display.update()
                    game_paused = False
                    return
                if options_button.draw(screen):
                    game_paused = False
                    pygame.draw.rect(screen,color,pygame.Rect(300,710,200,100))
                    pygame.draw.rect(screen,color,pygame.Rect(600,710,200,100))
                    pygame.draw.rect(screen,color,pygame.Rect(900,710,200,100))
                    pygame.display.update()
                    return
                if quit_button.draw(screen):
                    run = False
                    game_paused = False
                    return -1
                
            #event handler
            for event in pygame.event.get():
                    pass
                    
                        
                        

            pygame.display.update()


    # ********** function to get total number of player ********** #

    def _get_Total_Player(x,y):
        summa = True
        while summa:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_END:
                        summa = False
                    elif event.key == pygame.K_SPACE:
                        returned_value = pause(True)
                        if returned_value == -1:
                            summa = False
                            pygame.quit()
                            exit()
                    else:
                        column = event.unicode
                        text_surface = base_font.render(column,True,(255,255,255))
                        screen.blit(text_surface,(x,y))
                        pygame.display.update()
        return column                
        
    # ********** function to get text input on the screen ********** #

    def _text_Input(x,y):
        summa = True
        user_name =''
        while summa:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_END:
                        summa = False  
                    elif event.key == pygame.K_SPACE:
                        returned_value = pause(True)
                        if returned_value == -1:
                            summa = False
                            pygame.quit()
                            exit()
                    
                    else:
                        user_name += event.unicode
                        text_surface = base_font.render(user_name,True,(255,255,255))
                        screen.blit(text_surface,(x,y))
                        pygame.display.update()
                                
        return user_name        

    # *************** creating user class ***************#
    class User():
        def __init__(self):
            self.occurrence = [[0],[0],[0],[0],[0]]
            self.death     = [[0],[0],[0],[0],[0]]
            self.win =1
    # *************** table object class initialization ********* # 
    class Tables:
        def __init__(self):
            self.width = int((WIDTH-100)/column)
            self.height = int((HEIGHT-80)/rows)
            
    #  *************** function for creating boxes *************** #
        def _create_Tabes(self):
            self.tables = []
            for r_ow in range(rows):
                box_row = []
                for col_um in range(column):
                    box_x=(col_um*self.width)+100   
                    box_y=(r_ow*self.height)+75   

    # ********* creating objects for tables rectangle and store it in a list  ********** #
                    tb=pygame.Rect(box_x,box_y,self.width,self.height) 
                    box_row.append(tb)
                self.tables.append(box_row)              

    # ********** function for display tables on the screen ********** #
        def _draw_box(self):
            for row in self.tables:
                for tb in row:
                    pygame.draw.rect(screen,rect_color,tb,3)


    #  ********** initialization  class for toy *************** #

    class Toy_Body(Tables):
    # *********** creating toys x & y coordinate to draw lines ********** #

        '''  defining the function to generate the required coordinates and display the the line '''
        def _create_Toy(self,col_um,r_ow):
                    box_x=(col_um*box_drawn.width)+100
                    box_y=(r_ow*box_drawn.height)+60  
                    self.start_x  = int(box_x+(box_drawn.width/2)-20) 
                    self.start_y  = int(box_y+(box_drawn.height/2))
                    self.end_x    = self.start_x
                    self.end_y    = box_y+box_drawn.height-20
            # *********** Command for display line *********** #
                    pygame.draw.line(screen,object_colour,(self.start_x,self.start_y),(self.end_x,self.end_y),5)
                
    # ********** creating head to the character ********** #
    class Toy_Head(Toy_Body,Tables):
        def __init__(self):
            self.RADIUS = 23
            self.EYE_RADIUS=3
        '''similar that of line 90 same action but different shape  '''

        def _create_Head(self,col_um,r_ow):
                    box_x=(col_um*box_drawn.width)+100
                    box_y=(r_ow*box_drawn.height)+60  
                    line_drawn.start_x  = int(box_x+(box_drawn.width/2)-20)
                    line_drawn.start_y  = int(box_y+(box_drawn.height/2))
                    self.X = line_drawn.start_x
                    self.Y = line_drawn.start_y - 23
                    self.EYE_X1 = self.X -9
                    self.EYE_Y = self.Y
                    self.EYE_X2 = self.X +9
    # ************ Command for display head and eyes ************ #
                    pygame.draw.circle(screen,object_colour,(self.X,self.Y),self.RADIUS,5)
                    pygame.draw.circle(screen,object_colour,(self.EYE_X1,self.EYE_Y),self.EYE_RADIUS,3)
                    pygame.draw.circle(screen,object_colour,(self.EYE_X2,self.EYE_Y),self.EYE_RADIUS,3)

    # ************ creating hands and legs for the character ************ # 
    class Toy_Hands_Legs(Toy_Body,Tables):
        def _create_Toy_Hand_R(self,col_um,r_ow):    
                    box_x=(col_um*box_drawn.width)+100
                    box_y=(r_ow*box_drawn.height)+60  
                    self.hand_R_start_x  = int(box_x+(box_drawn.width/2)-20)
                    self.hand_R_start_y  = int(box_y+(box_drawn.height/2))+5
                    self.hand_R_end_x    = self.hand_R_start_x+30
                    self.hand_R_end_y    = self.hand_R_start_y+25
                    
                    #FOR LEFT HAND
                    self.hand_L_end_x   = self.hand_R_end_x-60
                    self.hand_L_end_y   = self.hand_R_end_y

                #for legs
                    
                    self.leg_R_start_x  = int(box_x+(box_drawn.width/2)-20)
                    self.leg_R_start_y  = line_drawn.end_y-4
                    self.leg_R_end_x    = self.leg_R_start_x+30
                    self.leg_R_end_y    = self.leg_R_start_y+25
                #for left
                    self.leg_L_end_x    = self.leg_R_start_x-30
                    self.leg_L_end_y    = self.leg_R_end_y
                #up to this
            #Command for display hand and legs
                    pygame.draw.line(screen,object_colour,(self.hand_R_start_x,self.hand_R_start_y),(self.hand_R_end_x,self.hand_R_end_y),5)
                    pygame.draw.line(screen,object_colour,(self.hand_R_start_x,self.hand_R_start_y),(self.hand_L_end_x,self.hand_L_end_y),5)
                    pygame.draw.line(screen,object_colour,(self.leg_R_start_x,self.leg_R_start_y),(self.leg_R_end_x,self.leg_R_end_y),5)
                    pygame.draw.line(screen,object_colour,(self.leg_R_start_x,self.leg_R_start_y),(self.leg_L_end_x,self.leg_L_end_y),5)

    # ********** creating class for display gun ********** #
    class Toy_Gun(Tables):
        def _create_Coordinates(self,col_um,r_ow):
                    box_x=(col_um*self.width)+100   
                    box_y=(r_ow*self.height)+60   
                    self.gun_x = int(box_x+(box_drawn.width/2))
                    self.gun_y =int(box_y+(box_drawn.height/2))
            #Command for display image
                    screen.blit(gun,(self.gun_x,self.gun_y))

    # ********** function to highlight the box ********** #
    def _highlight_Box(col_um,r_ow):
                    box_x=(col_um*box_drawn.width)+100-2
                    box_y=(r_ow*box_drawn.height)+75-2
                    pygame.draw.rect(screen,highlight_box,pygame.Rect(box_x,box_y,box_drawn.width+3,box_drawn.height+3),5) 

    # ********** function to draw cross line at right box ******** #
    def _cross_Line(x,y):
        for col_um in range(column):
            for r_ow in range(rows):        
                box_x=(col_um*box_drawn.width)+100 
                box_y=(r_ow*box_drawn.height)+75
                if (x>=box_x and x<(box_x+box_drawn.width)) and (y>=box_y and y< box_y+box_drawn.height):
                    pygame.draw.line(screen,cross_line_colour,(box_x,box_y),(box_x+box_drawn.width,box_y+box_drawn.height),5)
                    pygame.draw.line(screen,cross_line_colour,(box_x+box_drawn.width,box_y),(box_x,box_y+box_drawn.height),5)
                    pygame.display.update()
                    user_list[col_um].death[r_ow][0] =1
                    break

    # ********** function to generate random numbers ********** #
    def _generate_Random_Number():
        num = random.randint(0,554)
                
        box_drawn._draw_box()
        if(num % 2 != 0):
            num = num-1
        
        pygame.draw.rect(screen,color,pygame.Rect(random_text_x,random_text_y,250,20))
        _show_Text(random_text_x,random_text_y,"random number is :",num)
        return num




    # ********** to get total number of players  ********** #
    screen.fill(color)
    _show_Text(500,100,"Welcome you to - 'DV GAMES'")
    _show_Text(100,150,"*Instruction for entering details*")
    _show_Text(100,200,"1.Use END button instead of ENTER :")
    _show_Text(400,300,"Enter the total number of players:")
    pygame.draw.rect(screen,highlight_text1,pygame.Rect(495,95,330,30),3)
    pygame.draw.rect(screen,highlight_text2,pygame.Rect(395,295,410,30),3)

    pygame.display.update()
    column=int(_get_Total_Player(780,300))

    #box object creating
    box_drawn = Tables()
    box_drawn._create_Tabes()

    #toy object creating
    line_drawn = Toy_Body()

    #head object creating
    head_drawn = Toy_Head()


    #hand object creating
    hand_R_drawn = Toy_Hands_Legs()


    #gun object creating
    gun_drawn = Toy_Gun()

    #creating user objects
    user_list =[]
    for i in range(0,column):
        user_list.append(User())


    screen.fill(color)

    # ********** to get each player name  ********** # 
    _show_Text(400,300,"enter the player name:")
    _show_Text(200,100,'1.Use END instead of ENTER:')
    _show_Text(200,150,"2.Enter each player name and press END: ")
    pygame.draw.rect(screen,highlight_text2,pygame.Rect(195,145,500,30),3)
                

    user_name =[]   # create a list to store names of the player
    for i in range(0,column):
        
        s1=(_text_Input(700,(i*50)+300))
        user_name.append(s1)

    # ********** to display necessary instructions to play the game ********** #
    def _display_Rules():
        _show_Text(200,100,'*HI.. PLAYERS*')
        _show_Text(200,150,'*Before starting the here are some rules and instruction to be followed*')
        _show_Text(200,200,'1.Use key "A" for generate random number ')
        _show_Text(200,250,'3.Use mouse to eliminate other player')
        _show_Text(200,300,'4.Make sure that you can only eliminate other player only once at one time of chance ')
        _show_Text(200,350,'4.You cannot modify the chance which is once done ')
        _show_Text(200,400,'LETS START TO PLAY : CLICK "END"')
        summa= True
        while summa:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_END:
                        summa = False
        

    screen.fill(color)
    _display_Rules()  # function call to display rules

    # ********** to display stored player name and all necessary information ********** #
    screen.fill(color)
    box_drawn._draw_box()
    for i in range(column):
            _show_Text((i*box_drawn.width)+100+int(box_drawn.width/3),50,user_name[i])

    j=0  #just to increment the value for loop
    for i  in range(0,rows):
        # ********** to display row number ********** #    
        _show_Text(50,(i*box_drawn.height)+75+int(box_drawn.height/2),'',j)
        j+=2

    # ********** Function to draw character according to the random number generated ********** #

    def DrawFunction(i,row):
        _highlight_Box(i,row)
        pygame.display.update()
        user_list[i].occurrence[row][0] = user_list[i].occurrence[row][0] + 1
        if user_list[i].death[row][0] != 0:
            pygame.draw.rect(screen,color,pygame.Rect(random_text_x,random_text_y,250,20))
            _show_Text(random_text_x,random_text_y,"sorry already lost:")
        
        elif(user_list[i].occurrence[row][0]==1):
            head_drawn._create_Head(i,row)
        elif(user_list[i].occurrence[row][0]==2):
            line_drawn._create_Toy(i,row)
            hand_R_drawn._create_Toy_Hand_R(i,row)
        elif(user_list[i].occurrence[row][0]==3):
            gun_drawn._create_Coordinates(i,row)

        elif(user_list[i].occurrence[row][0]>3):
            click = True
            while click:
                pygame.draw.rect(screen,color,pygame.Rect(random_text_x+500,random_text_y,500,30))
                _show_Text(random_text_x+500,random_text_y,"please select any box to eliminate the player:")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed():
                            position =pygame.mouse.get_pos()
                            click =_cross_Line(position[0],position[1])
            pygame.draw.rect(screen,color,pygame.Rect(random_text_x+500,random_text_y,500,30))
            pygame.display.update()

    # ********** main function ********** #


    def main_function():
        run = True
        restart = 0
        while run:
            
            for i in range(0,column):
                
                if user_list[i].death[0][0] != 0 and user_list[i].death[1][0] != 0 and user_list[i].death[2][0] != 0 and user_list[i].death[3][0] != 0 and user_list[i].death[4][0] != 0:
                    pygame.draw.rect(screen,color,pygame.Rect(random_text_x+500,random_text_y,500,30))
                    _show_Text(random_text_x+500,random_text_y,"player already loose the game:")                    
                    user_list[i].win = 0
                    continue
                pygame.draw.rect(screen,color,pygame.Rect(random_text_x+500,random_text_y,500,30))
                total_win = column
                for j in range(0,column):
                    if user_list[j].win == 0:
                        total_win = total_win-1
                if total_win == 1:
                    summa = True
                    screen.fill(color)
                    while summa:
                        _show_Text(400,300,'player is won the game')
                        _show_Text(400,400,'press "END" to exit:' )
                        _show_Text(500,500,"  ")
                        pygame.draw.rect(screen,highlight_text2,pygame.Rect(395,295,400,30),3)
                        pygame.display.update()

                        for event in pygame.event.get():
                            key = pygame.key.get_pressed()
                            if key[pygame.K_END]:                
                                summa=False
                                restart = 1
                            elif key[pygame.K_SPACE]:
                                game_paused = True
                                returned_value = pause(True)
                                if returned_value == -1:
                                    summa = False
                                    restart = 1
                                
                                

                
                if restart == 1:
                    main()         
            
                summa = True
                while summa:
                    for event in pygame.event.get():
                        key = pygame.key.get_pressed()
                        if key[pygame.K_a]:
                            num=_generate_Random_Number()               
                            summa = False 
                        elif key[pygame.K_q]:
                            run = False
                            summa=False
                        elif key[pygame.K_SPACE]:
                                game_paused = True
                                returned_value = pause(True)
                                if returned_value == -1:
                                    summa = False
                                    restart = 1
                                
                                
                if restart == 1:
                    main()                 
                        
                        
                if(num % 10 ==0):
                    row =0
                    DrawFunction(i,row)

                elif(num % 10 ==2):
                    row =1
                    DrawFunction(i,row)

                elif(num % 10 ==4):
                    row =2
                    DrawFunction(i,row)

                elif(num % 10 ==6):
                    row =3
                    DrawFunction(i,row)

                elif(num % 10 ==8):
                    row =4
                    DrawFunction(i,row)

                pygame.display.update()


            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    main_function()
main()