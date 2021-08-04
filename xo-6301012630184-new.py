def displayboard():
    print("\n""[",board[0],"]""[",board[1],"]""[",board[2],"]""\n""[",board[3],"]""[",board[4],"]""[",board[5],"]""\n""[",board[6],"]""[",board[7],"]""[",board[8],"]""\n")
def cleardisplay():
    import os
    os.system('cls')
def startgame():
    cleardisplay()
    print("Welcome to the XO game! (Tic Tac Toe)")
    global board
    board = [1,2,3,4,5,6,7,8,9]
    displayboard()
    pickposition()
def pickposition():
    n = 0
    while checkwin() == False:
        try:
            number = input("Where do you want to place: ")
            if int(number) in range(1,10) and board[int(number)-1] != 'X' and board[int(number)-1] != 'O':
                if int(n) % 2 == 0:
                    board[int(number)-1] = 'X'
                if int(n) % 2 == 1:
                    board[int(number)-1] = 'O'
                displayboard()
                n+=1
            else:
                    (print('Please enter number 1-9 that is not taken'))
        except:
            (print('Please enter number 1-9 that is not taken'))
def checkwin():
    if board[0] == board[1] == board[2]:
        if board[0] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[3] == board[4] == board[5]:
        if board[3] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[6] == board[7] == board[8]:
        if board[6] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[0] == board[3] == board[6]:
        if board[0] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[1] == board[4] == board[7]:
        if board[1] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[2] == board[5] == board[8]:
        if board[2] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[0] == board[4] == board[8]:
        if board[0] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board[2] == board[4] == board[6]:
        if board[2] == 'X':
            print('X WIN')
            endgame()
        else:
            print('O WIN')
            endgame()
        return True
    if board.count('X')+board.count('O') == 9:
        print('IS A DRAW')
        endgame()
        return True
    else:
        return False

def endgame():
    global board
    again = input('\nDo you want to play again?(Y/n)')
    if again == 'Y':
        board = [1,2,3,4,5,6,7,8,9]
        startgame()
        return
    if again == 'n':
        return
    else:
        print("Please answer Y or n")
        endgame()
startgame()