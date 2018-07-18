import RPi.GPIO as GPIO
import time

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

pins = [
    [
        [14, 8, 4],
        [18, 12, 27],
        [24, 20, 10]
    ],
    [
        [15, 7, 17],
        [23, 16, 22],
        [25, 21, 9]
    ]
]

allPins = [14, 8, 4, 18, 12, 27, 24, 20, 10, 15, 7, 17, 23, 16, 22, 25, 21, 9]

def displayBoard():
    row = 0
    while row <= 2:
        column = 0
        while column <= 2:
            if board[row][column] == 1:
                GPIO.output(pins[0][row][column], GPIO.HIGH)
            elif board[row][column] == 2:
                GPIO.output(pins[1][row][column], GPIO.HIGH)
        column += 1
    row += 1

def checkBoard():
    possibilities = [[ [i[0] for i in board], [i[1] for i in board], [i[2] for i in board] ], [i for i in board], [ [board[i][2 - i] for i in [0, 1, 2]], [board[i][i] for i in [0, 1, 2]] ]]
    x = False
    for possibility in possibilities:
        for thingy in possibility:
            if thingy[0] == thingy[1] == thingy[2] and thingy[0] != 0 and thingy[1] != 0 and thingy[2] != 0:
                return "Player %i has won the game!" % (thingy[0])
                x = True
    if not x: return False
            

def makeMove(player):
    row = int(input("Player %i, choose a row (1 - 3): " % (player)))
    column = int(input("Player %i, choose a column (1 - 3): " % (player)))
    if board[row - 1][column - 1] != 0:
        print("Spot is already taken")
        makeMove(player)
    board[row - 1][column - 1] = player
    displayBoard()

def game():
    start = input("Would you like to start a new game (y/n)? ")
    if start == "y" or start == "yes":
        for i in allPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
        print("Player 1 is Blue\nPlayer 2 is Red\nLet's Begin!\n")
        for i in range(9):
            makeMove(1)
            a = checkBoard()
            if a:
                print(a)
                break
            makeMove(2)
            a = checkBoard()
            if a:
                print(a)
                break
    else:
        print("Goodbye then!")

if __name__ == "__main__":
    game()