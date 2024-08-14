board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentPlayer='X'
winner=None
gameRunning=True

#printing the game board
def printBoard(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print("---------")
    print(board[3]+' | '+board[4]+' | '+board[5])
    print("---------")
    print(board[6]+' | '+board[7]+' | '+board[8])
printBoard(board)
#take player input
def playerInput(board):
    inp = int(input("Enter a number 1 through 9: "))
    if inp>=1 and inp<=9 and board[inp-1] == "-":
        board[inp-1]=currentPlayer
    else:
        print("Oops Player is already in that spot!")
#check for win or tie
def checkWin(board):
    global winner
    win_conditions =[
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8],#columns
        [0,4,8],[2,4,6] #diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            winner = board[condition[0]]
            return True
    return False

def checkTie(board):
    if "-" not in board and winner is None:
        return True
    return False
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)

    if checkWin(board):
        printBoard(board)
        print(f"player {winner} wins!")
        gameRunning=False
    elif checkTie(board):
        printBoard(board)
        print("It's a tie!")
        gameRunning=False
    else:
        switchPlayer()

