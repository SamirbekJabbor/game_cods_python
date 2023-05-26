import numpy as np
 
 
class CheckersBoard:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.player_turn = 1
        self.selected_piece = None
        self.selected_piece_moves = None
 
        # Fill the initial board
        for i in range(0, 8, 2):
            self.board[0][i+1] = 1
            self.board[1][i] = 1
            self.board[2][i+1] = 1
 
            self.board[5][i] = -1
            self.board[6][i+1] = -1
            self.board[7][i] = -1
 
    def __str__(self):
        s = ""
        for row in self.board:
            for cell in row:
                if cell == 1:
                    s += "B "
                elif cell == -1:
                    s += "W "
                else:
                    s += ". "
            s += "\n"
        return s
 
    def select_piece(self, row, col):
        if self.board[row][col] * self.player_turn > 0:
            self.selected_piece = (row, col)
            self.selected_piece_moves = self.get_moves(row, col)
 
    def move_piece(self, row, col):
        if (row, col) in self.selected_piece_moves:
            self.board[row][col] = self.board[self.selected_piece[0]][self.selected_piece[1]]
            self.board[self.selected_piece[0]][self.selected_piece[1]] = 0
            self.selected_piece = None
            self.selected_piece_moves = None
            self.player_turn *= -1
 
    def get_moves(self, row, col):
        moves = []
        if self.board[row][col] == 1:
            if row > 0:
                if col > 0 and self.board[row-1][col-1] == 0:
                    moves.append((row-1, col-1))
                if col < 7 and self.board[row-1][col+1] == 0:
                    moves.append((row-1, col+1))
            if row > 1 and col > 1 and self.board[row-1][col-1] == -1 and self.board[row-2][col-2] == 0:
                moves.append((row-2, col-2))
            if row > 1 and col < 6 and self.board[row-1][col+1] == -1 and self.board[row-2][col+2] == 0:
                moves.append((row-2, col+2))
        elif self.board[row][col] == -1:
            if row < 7:
                if col > 0 and self.board[row+1][col-1] == 0:
                    moves.append((row+1, col-1))
                if col < 7 and self.board[row+1][col+1] == 0:
                    moves.append((row+1, col+1))
            if row < 6 and col > 1 and self.board[row+1][col-1] == 1 and self.board[row+2][col-2] == 0:
                moves.append((row+2, col-2))
            if row < 6 and col < 6 and self.board[row+1][col+1] == 1 and self.board[row+2][col+2] == 0:
                moves.append((row+2, col+2))
        return moves
board = CheckersBoard()
while True:
    print(board)
    row, col = map(int, input("Enter row and column of piece to move: ").split())
    board.select_piece(row, col)
    print(board)
    row, col = map(int, input("Enter row and column of square to move to: ").split())
    board.move_piece(row, col)
