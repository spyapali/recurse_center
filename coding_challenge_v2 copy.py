# Tic Tac Toe

# Logical steps to include a computer program player: 
# 1. Have the option for the player to select which option (X or O); set the computer program to the other player
# 2. X always goes first
# 3. Have the computer player be set to the other player. 
# 4. Use the minimax algorithm to choose the next possible play [STRETCH]  

import numpy
import copy 


class PerfectPlayer:

    def score(self, game, depth):
        if game.is_over() and game.currentPlayer == 'X':
            return 10 - depth 
        elif game.is_over() and game.currentPlayer == 'O':
            return depth - 10 
        else:
            return 0 
    
    def minimax(self, game, depth):
        if game.is_over():
            return self.score(game, depth) 
        
        scores, moves = [], [] 

        for possible_move in game.possible_moves:
            # need to create a new instance of the game object in the game
            possible_game = game.get_new_state(possible_move[0], possible_move[1])
            scores.append(self.minimax(possible_game, depth + 1))
            moves.append(possible_move)
        
        if game.current_player == 'X':
            max_score_index = scores.index(max(scores))
            max_score = scores[max_score_index]
            max_move = moves[max_score_index]
            game.insert_token(max_move)
            game.possible_moves.remove(max_move)
            return max_score
        else:
            min_score_index = scores.index(min(scores))
            min_score = scores[min_score_index]
            min_move = moves[min_score_index]
            game.insert_token(min_move)
            game.possible_moves.remove(min_move)
            return min_score

class Game:

    num_of_rounds = 1
    player1, player2 = 'X', 'O'
    currentPlayer = player1
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    possible_moves = [[0,0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2,2]]

    def print_board(self):
        for row in self.board:
            print(row[0] + " " + row[1] + " " + row[2])
    
    # def get_input(self):
    #     x_coord = int(input("Please pass in x coordinate: "))
    #     y_coord = int(input("Please pass in y coordinate: "))
    #     if self.validate_coord(x_coord, y_coord):
    #         return (x_coord, y_coord)
    #     else: 
    #         print("sorry! It looks like that coordinate is invalid OR is already occupied")
    #         return self.get_input()
    
    def validate_coord(self, x_coord, y_coord):
        if (self.board[x_coord][y_coord] != '-') or x_coord < 0 or x_coord > 2 or y_coord < 0 or y_coord > 2:
            return False 
        return True


    def is_over(self):
        return self.check_if_player_has_won() or self.num_of_rounds > 9

    def get_available_moves(self):
        return self.possible_moves

        
    # def play_turn(self): 
    #     while self.check_if_player_has_won() == False and self.num_of_rounds <= 9:
    #         print("it's {}'s turn!").format(self.currentPlayer)
    #         if self.currentPlayer == self.player2:
    #             x_coord, y_coord = self.get_input()
    #         else:
    #             # get move via minimax algorithm
    #         self.insert_token(x_coord, y_coord)
    #         if self.check_if_player_has_won():
    #             print("{} has won!").format(self.currentPlayer)
    #             return # get out of the game!
    #         self.num_of_rounds += 1 
    #         self.currentPlayer = self.player1 if self.num_of_rounds % 2 == 1 else self.player2
    #     # if we reach this condition, no one has won.
    #     print("Looks like it's a tie!")

    def get_new_state(self, x_coord, y_coord):
        board_copy = copy.deepcopy(self.board)
        board_copy[x_coord][y_coord] = self.currentPlayer

    def insert_token(self, x_coord, y_coord):
        self.board[x_coord][y_coord] = self.currentPlayer
        self.print_board()

    def check_if_player_has_won(self):

        # rows
        for row in range(3):
            if self.board[row][0] != "-" and self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                return True 
        # columns 
        for col in range(3):
            if self.board[0][col] != "-" and self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
                return True 

        # diagnols 
        if (self.board[0][0] != "-" and self.board[0][0] == self.board[1][1] and  self.board[1][1] == self.board[2][2]):
            return True 
        if (self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
            return True 

        return False


    
def start():
    game = Game()
    player = PerfectPlayer()
    game.print_board()
    player.minimax(game, 0)

# commands to start playing the game
start()



        




          
