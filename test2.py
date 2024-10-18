import copy

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    symbols = {1: 'X', 0: 'O', -1: ' '}
    i = 0
    for row in board:
        print(' | '.join([symbols[cell] for cell in row]))
        if (i < 2):
            print('-' * 9)
            i += 1
    print()

def get_user_input(board):
    # Function to get the user's move (X)
    while True:
        try:
            row, col = map(int, input("Enter row and column to place 'X' (0-2) separated by a space: ").split())
            if board[row][col] == -1:
                board[row][col] = 1  # Place 'X'
                break
            else:
                print("That spot is already taken, please choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column between 0 and 2.")

def generate_possible_boards(board, player):
    # Function to generate all possible boards for player 'O' (0)
    possible_boards = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:  # If the cell is empty
                new_board = copy.deepcopy(board)  
                new_board[i][j] = player
                possible_boards.append(new_board)
    return possible_boards

def get_user_selection(possible_boards):
    # Function to ask user to select one of the possible boards for 'O'
    while True:
        try:
            selection = int(input(f"Choose a possible board (1-{len(possible_boards)}): "))
            if 1 <= selection <= len(possible_boards):
                return possible_boards[selection - 1]
            else:
                print(f"Please enter a number between 1 and {len(possible_boards)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def is_board_full(board):
    # Function to check if the board is full
    return all(cell != -1 for row in board for cell in row)

def main():
    # Initial empty board
    board = [[-1 for _ in range(3)] for _ in range(3)]
    
    while not is_board_full(board):
        # Show current board
        print("Current board:")
        print_board(board)
        
        # User's turn (place 'X')
        get_user_input(board)
        
        # Check if the board is full after 'X'
        if is_board_full(board):
            print("Final board:")
            print_board(board)
            break
        
        # Generate all possible boards for placing 'O'
        possible_boards = generate_possible_boards(board, 0)
        
        # Show all possible boards for 'O'
        print("Possible boards for 'O':")
        for idx, pb in enumerate(possible_boards, 1):
            print(f"Option {idx}:")
            print_board(pb)
        
        # User selects one of the possible boards
        board = get_user_selection(possible_boards)
        
        # Check if the board is full after 'O'
        if is_board_full(board):
            print("Final board:")
            print_board(board)
            break

if __name__ == "__main__":
    main()