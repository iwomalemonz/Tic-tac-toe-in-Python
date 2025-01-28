import random

SIZE = 3
COMPUTER_MOVE = 'O'
PLAYER_MOVE = 'X'

board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]

def initialize_board():
    global board
    board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]

def print_board():
    print("\n-------------")
    for i in range(SIZE):
        print("| ", end="")
        for j in range(SIZE):
            print(f"{board[i][j]} | ", end="")
        print("\n-------------")

def is_board_full():
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == '-':
                return False
    return True

def is_winner_move(player):
    for i in range(SIZE):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def game_over():
    return is_winner_move(PLAYER_MOVE) or is_winner_move(COMPUTER_MOVE) or is_board_full()

def get_player_move():
    global board
    row, col = map(int, input("\nEnter row (1-3) and column (1-3) for your move (Player X): ").split())
    row -= 1
    col -= 1
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE or board[row][col] != '-':
        print("Invalid move. Try again.")
        get_player_move()
    else:
        board[row][col] = PLAYER_MOVE

def minimax(is_maximizer):
    if is_winner_move(PLAYER_MOVE):
        return -1
    if is_winner_move(COMPUTER_MOVE):
        return 1
    if is_board_full():
        return 0

    best_score = -1000 if is_maximizer else 1000

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == '-':
                board[i][j] = COMPUTER_MOVE if is_maximizer else PLAYER_MOVE
                score = minimax(not is_maximizer)
                if is_maximizer:
                    best_score = max(score, best_score)
                else:
                    best_score = min(score, best_score)
                board[i][j] = '-'

    return best_score

def get_computer_move():
    global board
    best_move_score = -1000
    best_row, best_col = -1, -1

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == '-':
                board[i][j] = COMPUTER_MOVE
                move_score = minimax(False)
                board[i][j] = '-'

                if move_score > best_move_score:
                    best_move_score = move_score
                    best_row, best_col = i, j

    board[best_row][best_col] = COMPUTER_MOVE

def main():
    global board
    random.seed()
    initialize_board()

    print("Welcome to Tic Tac Toe!")
    choice = input("Do you want to go first? (Y/N): ").upper()

    player_turn = choice == 'Y'

    while not game_over():
        if player_turn:
            print_board()
            get_player_move()
        else:
            get_computer_move()
        player_turn = not player_turn

    print_board()

    if is_winner_move(PLAYER_MOVE):
        print("Congratulations! You win!")
    elif is_winner_move(COMPUTER_MOVE):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
