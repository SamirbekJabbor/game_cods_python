import chess
import random
 
 
def play_game():
    board = chess.Board()
 
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = input("Enter your move in SAN notation (e.g. e2e4): ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move! Try again.")
                continue
        else:
            move = random.choice(list(board.legal_moves))
            board.push(move)
            print("Computer's move:", move.uci())
 
        print('\n' + str(board) + '\n')
 
    print("Game over!") 
    print("Result:", board.result())
 
 
if __name__ == '__main__':
    play_game()
