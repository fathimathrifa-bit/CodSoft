import math
import sys

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print("\n")

def check_winner(board):
    # Winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY:
            return board[condition[0]]
            
    if EMPTY not in board:
        return 'Tie'
        
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    # Base cases for recursion
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    board = [EMPTY] * 9
    print("==================================================")
    print("      🎮 UNBEATABLE TIC-TAC-TOE AI (MINIMAX) 🎮     ")
    print("      You are 'X' (Goes First) | AI is 'O'        ")
    print("   Positions are numbered 1 to 9 (Top to Bottom)  ")
    print("==================================================")
    
    # Showcase standard board reference positions
    print("Board Positions reference:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")
    
    print_board(board)

    while True:
        try:
            # Human Turn
            while True:
                move_input = input("Enter your move (1-9): ").strip()
                if move_input.isdigit() and 1 <= int(move_input) <= 9:
                    move = int(move_input) - 1
                    if board[move] == EMPTY:
                        board[move] = HUMAN
                        break
                    else:
                        print("That position is already taken!")
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            
            print_board(board)
            
            # Check if Human won or tied
            if check_winner(board):
                break

            # AI Turn
            print("AI is calculating its move...")
            ai_move = find_best_move(board)
            if ai_move != -1:
                board[ai_move] = AI
                
            print_board(board)
            
            # Check if AI won or tied
            if check_winner(board):
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nGame closed. Goodbye!")
            sys.exit()

    # Final Result
    game_result = check_winner(board)
    if game_result == 'Tie':
        print("🏁 It's a perfect tie! Well played.")
    elif game_result == AI:
        print("🤖 The AI wins! Better luck next time.")
    elif game_result == HUMAN:
        print("🎉 Incredible! You beat the unbeatable AI!") # This shouldn't happen mathematically!

if __name__ == "__main__":
    main()