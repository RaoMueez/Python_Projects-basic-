# List for positions on board :
board = [
    "1","2","3","4","5","6","7","8","9"
]

# players & symbols :
players = {
    "X" : "Player1",    # Symbol | Player_number
    "O" : "Player2"
}

# winning combinations :
combinations = (
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6),
)

# Moves :
moves = {
    0,1,2,3,4,5,6,7,8
}

# Method for displaying board :
def display_board() :
    print()
    print(board[0], "|", board[1], "|", board[2],)
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5],)
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8],)
    print()

# Winner check method :
def winner_check(symbol) :
    for combination in combinations :
        if all(board[position] == symbol for position in combination) :
            return True
    return False

# Method for user input :
def make_move(symbol) :
    while True :
        choice = input(f"\n{players[symbol]} select number(1-9) to make your move:")
        
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        position = int(choice)-1

        if position<0 or position>8 :
            print("Invalid position.")
            continue
        elif position in moves:
            board[position] = symbol                            
            # Display updated board :
            display_board()               
            moves.remove(position)
            break   
        else :
            print("Position already occupied. Please enter available position.")
            display_board()            
        

current_player = "X"
print("\n----- WELCOME TO TIC-TAC-TOE GAME -----")
display_board()
while True :
    make_move(current_player)

    # check for winner :
    if winner_check(current_player) :
        display_board()
        print(f"{players[current_player]} wins!")
        break

    # Check for draw :
    if len(moves) == 0 :
        print("It's a draw!")
        break    

    # Change player :
    current_player="O" if current_player=="X" else "X"

print("\nThanks for Playing")