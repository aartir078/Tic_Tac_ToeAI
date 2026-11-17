
import math

board = [" "] * 9

def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_positions
    )

def is_draw():
    return " " not in board

def minimax(is_ai, depth=0):
    if check_winner("O"):
        return 10 - depth

    if check_winner("X"):
        return depth - 10

    if is_draw():
        return 0

    if is_ai:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, depth + 1)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, depth + 1)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, 0)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        print("AI chooses position:", move + 1)

def play_game():
    print("=== TIC-TAC-TOE AI ===")
    print("You are X. AI is O.")
    print("Choose a position from 1 to 9.")
    print("Position layout:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    print_board()

    while True:
        try:
            move = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid or occupied position. Try again.")
            continue

        board[move] = "X"
        print_board()

        if check_winner("X"):
            print("Congratulations! You win!")
            break

        if is_draw():
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins! Better luck next time.")
            break

        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
