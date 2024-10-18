from itertools import product

def is_valid_tic_tac_toe_state(state):
    """
    Function to check if a given tic-tac-toe state is valid.
    """
    x_count = state.count('X')
    o_count = state.count('O')
    
    # Number of X's should either be equal to or one more than O's
    if not (x_count == o_count or x_count == o_count + 1):
        return False
    
    # Function to check if a player has won
    def check_win(player):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        return any(state[i] == state[j] == state[k] == player for i, j, k in win_positions)
    
    x_wins = check_win('X')
    o_wins = check_win('O')
    
    # Both players can't win simultaneously
    if x_wins and o_wins:
        return False
    
    # If O wins, number of X's and O's should be equal (O played last)
    if o_wins and x_count != o_count:
        return False
    
    # If X wins, number of X's should be one more than O's (X played last)
    if x_wins and x_count != o_count + 1:
        return False
    
    return True

def generate_all_tic_tac_toe_states():
    """
    Function to generate all possible valid tic-tac-toe game states.
    """
    symbols = ['X', 'O', '_']
    all_states = list(product(symbols, repeat=9))
    valid_states = []

    for state in all_states:
        if is_valid_tic_tac_toe_state(state):
            valid_states.append(state)

    return valid_states

def print_state(state):
    """
    Helper function to print a tic-tac-toe game state.
    """
    for i in range(0, 9, 3):
        print(' '.join(state[i:i+3]))
    print()

if __name__ == "__main__":
    valid_states = generate_all_tic_tac_toe_states()
    
    print(f"Number of valid states: {len(valid_states)}\n")
    
    # Print all valid states
    for state in valid_states:
        print_state(state)