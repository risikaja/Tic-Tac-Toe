import random

def display_board(board):
    """
    Displays the current board state.
    """
    row_separator = "+-------+-------+-------+"
    cell_separator = "|       |       |       |"
    print("Board current status:")
    print()
    for row in board:
        print(row_separator)
        print(cell_separator)
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print(cell_separator)
    print(row_separator)

def enter_move(board, moves_left):
    """
    Handles the player's move and updates the board.
    """
    while True:
        try:
            move = int(input("Enter the next move: "))
            if move not in moves_left:
                print("Invalid move. Please enter another move.")
            else:
                moves_left.remove(move)
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == move:
                            board[i][j] = 'O'
                            return
        except ValueError:
            print("Enter a valid move (a number).")

def make_list_of_free_fields(board):
    """
    Returns a list of free fields (tuples of row and column indices).
    """
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isinstance(board[i][j], int):  
                free_fields.append(board[i][j])  
    return free_fields

def victory_for(board, sign):
    """
    Checks if the player with the given sign ('O' or 'x') has won.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def draw_move(board, moves_left):
    """
    Handles the computer's move and updates the board.
    """
    computer_move = random.choice(moves_left)
    moves_left.remove(computer_move)  
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == computer_move:
                board[i][j] = 'x'
                return

def main():
    """
    Main function to play the game.
    """
    board = [[1, 2, 3], [4, 'x', 6], [7, 8, 9]]
    moves_left = make_list_of_free_fields(board)  

    while True:
        display_board(board)

        
        enter_move(board, moves_left)
        if victory_for(board, 'O'):
            display_board(board)
            print("Congratulations! You have won!")
            break

        if not moves_left:
            display_board(board)
            print("It's a tie!")
            break

        
        draw_move(board, moves_left)
        if victory_for(board, 'x'):
            display_board(board)
            print("The computer has won!")
            break

if __name__ == "__main__":
    main()
