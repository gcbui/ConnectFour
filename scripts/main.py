from re import S
from tkinter import Place
from unicodedata import name
import random

class Player:
    name = ""
    mode = 'D'
    piece_type = ' '

class Board:
    def __init__(self):
        self.grid = []

    def init_board(self):
        self.grid = []
        for row in range(0,6):
            current_row = []
            for col in range(0,7):
                current_row.append(' ')
            self.grid.append(current_row)

    def print_board(self):
        print("________NEW____BOARD__________")
        for row in range((len(self.grid))):
            print (self.grid[row])
        print("______________________________")
    
    def is_column_empty(self,column):
        if self.grid[0][column] == ' ':
            return True
        else:
            return False

    def place_piece(self,column,player):
        if self.is_column_empty(column) == True:
            for row in range(len(self.grid)):
                if self.grid[len(self.grid)-1][column] == ' ':
                    self.grid[len(self.grid)-1][column] = player.piece_type
                    break
                if self.grid[row][column] != ' ':
                    self.grid[row-1][column] = player.piece_type
                    break
        else:
            print ("Column is full.Retry.")

    def check_horizontal(self,player):
        for row in range(len(self.grid)):
            four_in_a_row = 0
            for col in self.grid[row]: 
                if col == player.piece_type:
                    four_in_a_row += 1
                    if four_in_a_row == 4:
                        return True
                else:
                    four_in_a_row = 0 
        return False    

    def check_vertical(self,player):
        for col in range(len(self.grid[0])):
            four_in_a_row = 0
            for row in range(len(self.grid)): 
                if self.grid[row][col] == player.piece_type:
                    four_in_a_row += 1
                    if four_in_a_row == 4:
                        return True
                else:
                    four_in_a_row = 0 
        return False    

    def check_diagonal(self,player):
        r=0
        for r in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                four_in_a_row = 0 
                i=0
                for row in range(len(self.grid)):
                    if i >= len(self.grid[row]):
                        break
                    elif self.grid[row+r][col+i] == player.piece_type:
                        four_in_a_row+=1
                        if four_in_a_row==4:
                            return True   
                    else:
                        four_in_a_row = 0
                    i+=1
            r+=1
        return False
                
    def check_tie(self):
        for col in self.grid[0]:
            if col == ' ':
                return False
        return True

    def check_game_status(self,player):
        if self.check_horizontal(player):
            print (player.name + " Wins!")
            return True
        elif self.check_vertical(player):
            print (player.name + " Wins!")
            return True
        elif self.check_diagonal(player):
            print (player.name + " Wins!")
            return True
        elif self.check_tie():
            print ("Draw!")
            return True
        else:
            return False

    def get_available_columns(self):
        available_columns = []
        for col in range(len(self.grid[0])):
            if self.is_column_empty(col) ==True:
                available_columns.append(col)
        return available_columns

def choose_column(player,board):
    available_columns = board.get_available_columns()
    if player.mode == 'A':
        return random.choice(available_columns)
    else: #player selection for real player
        print("These are the available columns: " + str(available_columns))
        while True:
            selected_columns = input("Select Column")
            if len(selected_columns) != 1:
                print("Please enter one number!")
            elif int(selected_columns) in available_columns:
                return int(selected_columns)
            else:
                print("Not a valid column! Retry!")
                
def simulate(trials):
    board = Board()
    player1 = Player()
    player2 = Player()
    #Player1 Customization
    while player1.mode == 'D':
        temp_player1_mode = input("Please enter a mode for Player1: (P) Player vs. AI or (A) AI vs. AI")
        if len(temp_player1_mode) == 0:
            continue
        player1.mode = temp_player1_mode[0].upper()
        if player1.mode == 'P':
            while player1.name == "":
                player1.name = input("Please enter your name: ").strip(' ')
            excluded_piece_types = [',','[',']',' ','#','*','\'']
            while player1.piece_type in excluded_piece_types:
                temp_piece_type = input("Please select a valid piece: ").strip(' ')
                if len(temp_piece_type) == 0:
                    continue
                else:
                    player1.piece_type = temp_piece_type[0]
            break
        elif player1.mode == 'A':
            player1.name = "AI-1"
            player1.piece_type = '*'
            print("Player1 Name: " + player1.name + " Piece type: " + player1.piece_type)
            break
        else:
            player1.mode = 'D'
    #Player2 Customization
    while player2.mode == 'D':
        temp_player2_mode = input("Please enter a mode for Player2: (P) Player vs. AI or (A) AI vs. AI")
        if len(temp_player2_mode) == 0:
            continue
        player2.mode = temp_player2_mode[0].upper()
        if player2.mode == 'P':
            while player2.name == "":
                player2.name = input("Please enter your name: ").strip(' ')
            excluded_piece_types = [',','[',']',' ','#','*',player1.piece_type,'\'']
            while player2.piece_type in excluded_piece_types:
                temp_piece_type = input("Please select a valid piece: ").strip(' ')
                if len(temp_piece_type) == 0:
                    continue
                else:
                    player2.piece_type = temp_piece_type[0]
            break
        elif player2.mode == 'A':
            player2.name = "AI-2"
            player2.piece_type = '#'
            print("Player2 Name: " + player2.name + " Piece type: " + player2.piece_type)
            break
        else:
            player2.mode = 'D'
    for trial in range(trials):
        print("Game " + str(trial) + " out of " + str(trials))
        board.init_board()
        player_ones_turn = True
        while True:
            active_player = player1
            if player_ones_turn == False:
                active_player = player2
            selected_column = choose_column(active_player,board)
            board.place_piece(selected_column,active_player)
            board.print_board()
            game_status = board.check_game_status(active_player)
            if game_status:
                break
            player_ones_turn = not player_ones_turn
  
if __name__ == "__main__":
    simulate(10)