"""
Tic Tac Toe
By Damion Davis
"""
def main():
    x = 0
    spot = list()
    while not (win_condition(spot) or x == 9):
        board_print(spot)
        x += 1
        play_X(spot)
        if not win_condition(spot):
            board_print(spot)
            x += 1
            play_O(spot)
    if win_condition(spot):
        board_print(spot)
        print("Good game guys!")
    else:
        board_print(spot)
        print("Thats a cat!")

def list():
    spot = [0,1,2,3,4,5,6,7,8,9]
    return spot

def board_print(spot):
    print(f"{spot[1]}|{spot[2]}|{spot[3]}")
    print("-|-|-")
    print(f"{spot[4]}|{spot[5]}|{spot[6]}")
    print("-|-|-")
    print(f"{spot[7]}|{spot[8]}|{spot[9]}")

def win_condition(spot):
    return (spot[1] == spot[2] == spot[3] or
    spot[4] == spot[5] == spot[6] or
    spot[7] == spot[8] == spot[9] or
    spot[3] == spot[6] == spot[9] or
    spot[2] == spot[5] == spot[8] or
    spot[1] == spot[4] == spot[7] or
    spot[1] == spot[5] == spot[9] or
    spot[7] == spot[5] == spot[3] )
    
def play_X(spot):
    move = int(input("It is X's turn, input number here: "))
    spot[move] = "X"

def play_O(spot):
    move = int(input("It is O's turn, input number here: "))
    spot[move] = "O"

main()