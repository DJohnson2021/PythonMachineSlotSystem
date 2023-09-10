import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# 3 wheels
ROW = 3
# The wheels themselves.
# Basically a column full of symbols and each symbol appears a number of times in the column.
COL = 3

# Dictionary for the symbols found in the wheels/columns and their frequency
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

# Collect deposit from user
# isdigit() checks if strings are positive integers. It does not 
def deposit():
    while True:
        deposit = input("Please enter the amount you want to deposit: $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Deposit must be greater than 0!")
        else:
            print("Please enter a valid number!")
    
    return deposit

# Get the number of lines the user wants to bet on
def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on: (1-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 1 and 3!")
        else:
            print("Please enter a valid number!")
    
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"bet must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a valid number!")

    return bet


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # calculate winnings
            winnings += values[symbol] * bet
            # What line user won on
            winnings_lines.append(line + 1)
    
    return winnings, winnings_lines 


# I don't like the logic used here to create the slots for the machine.
# I basically made an lists of lists to represent the columns of the slot machine
# But this approach is logically confusing
# Whenever I use brackets double brackets, I think I'm referring to the rows and columns like i and j
# But, no that is not the case. I am only referring to the cell
# in another list within the list of columns
# I honestly think just using a 2D array would've been better. 
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .items() gets the key and key value from the dictionary
    # This allows us to get both values without having to manually reference them
    for symbol, symbol_count in symbols.items():
        # we don't actually care about the elements so we can just use an _ to cycle through the range.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Create a list of columns
    columns = []
    # For every column we need to generate a number of symbols
    for _ in range(cols):
        column = []
        # create a copy of all symbols
        # It won't be possible to use the entire symbol count to fill all 3 columns because 
        # this is a 3x3 matrix. There are only 9 cells to fill
        # So, we want to randomly fill a value from the dictionary in the column
        # and then romove that item from the list of current_symbol until the column is complete
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")

        print()


def spin(balance):
    lines = get_num_of_lines()

    # get bet from user and find total bet
    # check if total bet <= balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Bet cannot be more than balance available! Current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROW, COL, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winnings == 0:
        print(f"You have won on 0 lines.")
    else:   
        print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


# this main function is not like C++
# Python is a script based language. It doesn't have a "main" function
# this function will just make it easier to allow the player to play the game again
def main(): 
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        user_answer = input("Press enter to play (q to quit).")
        if user_answer == "q":
            break
        balance += spin(balance)
        if balance <= 0:
            break

    print(f"You're left with ${balance}")

main()