
# Requirements 
# ask the user which player they want to be; computer is other player
# 'X' player always goes first 
# 9 rounds 
# Player with a streak of 3: diagnolly, vertically, or horizontally wins 
# computer plays randomly in an open position

class Game():

    player1, player2 = 'X', '0'
    current_player = player1
    board = [["x" for col in range(3)] for row in range(3)]
    num_of_rounds = 9
    computer_player = 'X' # perhaps by default, but no special preference here 


    def print_board(self):
        for row in self.board:
            print(" ".join(row))
    
    def check_if_valid(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False 
        return True 
    
    def start():
        pass 
    
    def input(self):
        # keeps asking the user to insert a token when it's their turn. Comp plays next turn
        pass 

    def check_if_player_won(self):
        for index in range(len(self.board)):
            if all(self.board[index][col] == self.current_player for col in range(index)):
                return True 
            if all(self.board[row][index] == self.current_player for row in range(index)):
                return True 
            
        # handles forward diagnol 
        if all(self.board[i][i] == self.currentPlayer for i in range(len(self.board))):
            return True 

        # backward diagnol 
        if all(self.board[row + 1][len(self.board) - 1 - row] for row in range(3)):
            return True 
        
        return False


game = Game()
game.print_board()








