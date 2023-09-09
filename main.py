MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        bet = input("Please enter the amount you want to bet: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"bet must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a valid number!")

    return bet



# this main function is not like C++
# Python is a script based language. It doesn't have a "main" function
# this function will just make it easier to allow the player to play the game again
def main(): 
    balance = deposit()
    lines = get_num_of_lines()
    bet = get_bet()



main()