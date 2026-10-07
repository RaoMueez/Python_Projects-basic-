import random

# Global Variables :
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# spin the machine :
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count) :
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols) :
        column = []
        current_symbols = all_symbols[:] 
        
        for _ in range(rows) :
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)

    return columns

# Winning method : 
def check_winnings(columns, lines, bet, values) :
    winnings = 0
    winning_lines = []
    

    for line in range(lines) :
        symbol = columns[0][line]

        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check :
                break
        else :
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

# slot machine printing :
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

# User's bet amount :
def deposit() :
    while True :
        bet_amount = input("Enter the bet amount : $")
        if bet_amount.isdigit() :
            bet_amount = int(bet_amount)
            if bet_amount>0 :
                break
            else :
                print("Bet amount should be greater than 0.")
        else :
            print("Please Enter a Number.")

    return(bet_amount)

# Lines to bet on :
def get_number_of_lines() :
    while True :
        lines = input("Enter the number of lines you want to bet on (1-3): ")
        if lines.isdigit() :
            lines = int(lines)
            if 1<=lines<=MAX_LINES :
                break
            else :
                print("Please enter number between (1-3).")
        else :
            print("Please Enter a Number.")

    return(lines)

# Bet on each line :
def get_bet(balance, lines) :
    while True :
            amount = input("How much do you want to bet on each line : $")
            if amount.isdigit() :
                amount = int(amount)
                total_amount = amount * lines
                if total_amount>balance or amount>balance :
                    print(f"Insufficient balance, Current balance: ${balance}")
                else :
                    if MIN_BET<=amount<=MAX_BET :
                        break
                    else :
                        print(f"You can bet in range: {MIN_BET} - {MAX_BET}")
            else :
                print("Please Enter a Number.")
    
    return(amount)

def play_game():
    balance = deposit()

    while True:
        print(f"\n==============================")
        print(f" Current balance is: ${balance}")

        answer = input("Press ENTER to play (or type 'q' to quit): ").lower()
        if answer == "q":
            break

        lines = get_number_of_lines()
        amount = get_bet(balance, lines)
        
        total_bet = amount * lines
        print(f"\nYou are betting ${amount} on {lines} lines. Total bet is: ${total_bet}")

        balance -= total_bet

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print("\nSpinning...")
        print_slot_machine(slots)

        winnings, winning_lines = check_winnings(slots, lines, amount, symbol_value)
        
        if winnings > 0:
            print(f"YOU WON ${winnings}! ")
            print(f"You won on lines:", *winning_lines) 
        else:
            print(" No match this time.")
            
        balance += winnings

        if balance == 0:
            print("\nYou ran out of money! Game Over.")
            break

    print(f"\nThank you for playing! You left with ${balance}")

# Start :
play_game()
