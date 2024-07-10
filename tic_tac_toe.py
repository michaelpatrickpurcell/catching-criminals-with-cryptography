import random

class GameBoard(object):
    def __init__(self, n=3):
        self.n = n
        self.game_board = [[0 for j in range(n)] for i in range(n)]
    def update_board(self, player_number, location):
        self.game_board[location[0]][location[1]] = player_number
    def check_win_condition(self, player_number):
        win_flag = False
        for row in range(self.n):
            if all([self.game_board[row][j] == player_number for j in range(self.n)]):
                win_flag = True
        for column in range(self.n):
            if all([self.game_board[i][column] == player_number for i in range(self.n)]):
                win_flag = True
        if all([self.game_board[i][i] == player_number for i in range(self.n)]):
            win_flag = True
        if all([self.game_board[i][self.n-1-i] == player_number for i in range(self.n)]):
            win_flag=True
        return win_flag
    def __str__(self):
        for row in range(self.n):
            print(''.join(['%i' % x for x in self.game_board[row]]))
    
class Opponent(object):
    def __init__(self, player_number=2, n=3):
        self.n = n
        self.player_number = player_number
    def make_random_move(self, game_board):
        valid_moves = []
        for i in range(self.n):
            for j in range(self.n):
                if game_board[i][j] == 0:
                    valid_moves.append((i,j))
        location = random.choice(valid_moves)
        game_board.update_board(self.player_number, location)
    
if __name__ == "__main__":
    board = GameBoard(n=3)
    print(board)
    opponent = Opponent(player_number=2, n=3)
    winner = 0

