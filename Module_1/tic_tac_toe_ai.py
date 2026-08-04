import random

# this is for the 9 spaces on the board 
board = [' '] * 9

q_table = {}


def print_board(b):
    print(b[0], '|', b[1], '|', b[2])
    print('--+---+--')
    print(b[3], '|', b[4], '|', b[5])
    print('--+---+--')
    print(b[6], '|', b[7], '|', b[8])


def check_win(b, player):
    # all the possible ways to win
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False


def check_tie(b):
    # if there is no empty space left, it's a tie
    return ' ' not in b


def get_empty_cells(b):
    empty = []
    for i in range(9):
        if b[i] == ' ':
            empty.append(i)
    return empty


def get_q_value(state, action):
    key = (tuple(state), action)
    if key in q_table:
        return q_table[key]
    else:
        return 0


def choose_action(state, empty_cells, epsilon):
    # small chance to try a random move (this is how the AI explores)
    if random.random() < epsilon:
        return random.choice(empty_cells)

    # otherwise pick the move with the best known score
    best_value = -1000
    best_move = empty_cells[0]
    for move in empty_cells:
        value = get_q_value(state, move)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move


def update_q_table(history, reward):
    # give credit (or blame) to every move the AI made this game
    learning_rate = 0.5
    for state, action in history:
        key = (tuple(state), action)
        old_value = get_q_value(state, action)
        q_table[key] = old_value + learning_rate * (reward - old_value)


def play_one_game(epsilon):
    global board
    board = [' '] * 9
    ai_history = []
    current_player = 'X'   # AI is always X, random opponent is O

    while True:
        empty_cells = get_empty_cells(board)

        if current_player == 'X':
            state_before = board[:]
            move = choose_action(state_before, empty_cells, epsilon)
            ai_history.append((state_before, move))
        else:
            move = random.choice(empty_cells)

        board[move] = current_player

        if check_win(board, current_player):
            if current_player == 'X':
                update_q_table(ai_history, 1)     # AI won
            else:
                update_q_table(ai_history, -1)    # AI lost
            return current_player

        if check_tie(board):
            update_q_table(ai_history, 0)         # nobody won
            return 'tie'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


def train_ai(num_games):
    print("Training the AI by playing", num_games, "games against a random player...")
    wins = 0
    losses = 0
    ties = 0

    for i in range(num_games):
        epsilon = 1 - (i / num_games)
        if epsilon < 0.1:
            epsilon = 0.1

        result = play_one_game(epsilon)
        if result == 'X':
            wins += 1
        elif result == 'O':
            losses += 1
        else:
            ties += 1

    print("Training finished!")
    print("AI record -> Wins:", wins, "Losses:", losses, "Ties:", ties)


def play_against_human():
    global board
    board = [' '] * 9
    current_player = 'X'   

    print("\nLet's play! You are O, the AI is X.")
    print("Board positions are numbered 0-8 like this:")
    print_board(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
    print()
    print_board(board)

    while True:
        empty_cells = get_empty_cells(board)

        if current_player == 'X':
            print("\nAI is thinking...")
            move = choose_action(board, empty_cells, 0)   
        else:
            move = int(input("Enter your move (0-8): "))
            while move not in empty_cells:
                move = int(input("That spot is taken. Enter your move (0-8): "))

        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(current_player, "wins!")
            break

        if check_tie(board):
            print("It's a tie!")
            break

        # switching turns
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


def main():
    train_ai(2000)      
    play_against_human()  


main()
