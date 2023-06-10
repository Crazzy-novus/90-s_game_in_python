import socket,threading,json,time

# ----------------------------------------------------------------------------------------- #

# socket constants to be used and Altered

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

# Define pygame constants to be used and Altered

ROOM_SIZE = 400
PLAYER_SIZE = 20
ROUND_TIME = 45
FPS = 60
TOTAL_PLAYERS = 8


# Room must be divisible by player size for correct game play, adjust as needed

while ROOM_SIZE % PLAYER_SIZE !=0:
    PLAYER_SIZE += 1


# Maximum number of players allowed is 8!

if TOTAL_PLAYERS > 8:
    TOTAL_PLAYERS = 8
# --------------------------------------------------------------------------------------------#

# ````````````````````````````````````````````````````````````````````````````````````````````#

# Define class

class Connection():
    '''A socket connection class to be used as a sever'''
    def __init__(self):
        '''Initialization of the Connection class'''
        pass


class Player():
    '''A class to store a connected clients player information'''

    def __init__(self,number):
        '''Initialization of the player class'''
        pass

    def set_Player_Info(self,player,player_info):
        '''Set the player info to the given info from the client(coordinates and status)'''
        pass

    def reset_Player(self):
        '''Rest player values for a new round on the server side'''
        pass


class Game():
    '''A class to handle all operation of game play'''

    def __init__(self,connection):
        '''Initialization of the Game class'''
        pass

    def connect_Player(self):
        '''Connect ANY incoming player to the game'''
        pass

    def broadCast(self):
        '''Broadcast information to all players'''
        pass

    def ready_Game(self,player,player_socket):
        '''Ready the game to be player for a SPECIFIC player '''
        pass


    def reset_Game(self,player):
        '''Reset the game and wipe information for a SPECIFIC player'''
        pass


    def send_Player_Info(self,player,player_socket):
        '''Send SPECIFIC player information about this player to the given client'''
        pass

    def receive_Player_Info(self,player,player_socket):
        '''Receive specific info about This Player pregame'''
        pass

    def receive_Game_Player_Info(self,player,player_socket):
        '''Receive specific info about This player during the game'''
        pass

    def process_Game_State(self,player,player_socket):
        '''Process the given info and update the game status'''
        pass

    def send_Game_State(self,player_socket):
        '''Send teh current game statue of All players to THIS diven player'''
        pass

# ***************** START SERVER ****************** #

my_connection = Connection()
my_game = Game(my_connection)

# ***************** LISTEN FOR IN-COMING CONNECTION ****************** #

print(("Sever is listing for incoming connections....\n"))
my_game.connect_Player()
