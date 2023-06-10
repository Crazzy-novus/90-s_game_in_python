#  Online Multiplayer Game Client

import pygame, socket, threading, json


# -------------------------------------------------------------------- #

# Define socket constraints to be used and ALTERED 
# DEST_IP should be of the form '192.168.1.*' or other address

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345

# -------------------------------------------------------------------- #

# Define classes 

class Connection():
    '''A socket connection class for players to connect to ta server'''
    def __init__(self):
        '''Initialization of the Connection class'''
        pass


class Player():
    '''A Player class the client can control'''
    def __init__(self,connection):
        '''Initialization of the player class'''
        pass


    def set_Player_Info(self,player,player_info):
        '''Set the player info to the given info from the sever(coordinates and status)'''
        pass


    def update(self):
        '''Update the player by changing their coordinates in the game'''
        pass


    def reset_Player(self):
        '''Rest player values for a new round on the client side'''
        pass


class Game():
    '''A class to handle all operation of game play'''
    def __init__(self,connection,player,total_players):
        '''Initialization of the Game class'''
        pass


    def ready_Game(self):
        '''Ready the game to be played'''
        pass


    def start_Game(self):
        '''Start the game'''
        pass


    def reset_Game(self):
        '''Reset the game'''
        pass


    def send_Player_Info(self):
        '''Send SPECIFIC player information about this player to the given sever'''
        pass


    def receive_Player_Info(self):
        '''Receive specific info about This Player from the server'''
        pass


    def receive_Pregame_State(self):
        '''Receive all information about ALL players from the server before the game starts'''
        pass


    def receive_Game_State(self):
        '''Receive ALL information  about ALL players from the server during the game'''
        pass


    def process_Game_State(self,player,player_socket):
        '''Process the game state to update scores, winning player, and time ], etc ...'''
        pass


    def update(self):
        '''Draw the game and all game assets to the window'''
        pass


# Create a connection and get game window information from the server

my_connection = Connection()

#Initialize pygame
pygame.init()

# Set game constants

WINDOW_WIDTH =1300
WINDOW_HEIGHT=700
ROUND_TIME = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
MAGENTA = (155,0,155)
FPS = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont("gabriola",28)


# Create a game window 

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("~~Color Collide~~")

# Create player and game objects
my_player = Player(my_connection)
my_game = Game(my_connection,my_player,4)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_END]:                
                running = False
                
    
    # Fill the surface
    display_surface.fill(BLACK)

    #Update and draw classes
    my_player.update()
    my_game.update()
    #my_game.draw()

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)