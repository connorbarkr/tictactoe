import random

exampleBoard = ['1', '2', '3',
                '4', '5', '6',
                '7', '8', '9']

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

def intro():
    first = fiftyFifty()
    print("Here's what the board will look like:")
    drawBoard(exampleBoard)
    print("To select a tile to place your marker on, type the corresponding number when it's your turn!")
    if first == 0:
        print("You go first!")
    else:
        print("The computer goes first!")
    return first;

def fiftyFifty():
    return random.randint(0, 1)

def oneToNine():
    return random.randint(1, 9)

def teamChoice():
    while True:
        choice = input("Would you like to be x's or o's? (Type 'x' or 'o')").upper()
        if (choice != 'X' and choice != 'O'):
            print("I'm sorry, you'll have to input a valid choice")
            continue
        else:
            print("Great! You're team " + choice + "s.")
            return choice
            break

def playerMoveChoice(selection):
    while True:
        choice = input("Enter the number of the square you'd like to select: ")
        if choice.isalpha() or int(choice) < 1 or int(choice) > 9:
            print("Please enter a valid number between 1 and 9.")
            continue
        elif board[int(choice) - 1] != " ":
            print("That space is already taken! Pick a valid one.")
            continue
        else:
            board[(int(choice) - 1)] = selection
            drawBoard(board)
            break

def computerMoveChoice(computerSelection):
    print("It's the computer's turn!")
    while True:
        choice = oneToNine()
        if board[choice - 1] != ' ':
            continue
        board[choice - 1] = computerSelection;
        drawBoard(board)
        break

def winnerCheck(board, symbol):
    if (board[0] == symbol and board[4] == symbol and board[8] == symbol):
        return 1
    elif (board[2] == symbol and board[4] == symbol and board[6] == symbol):
        return 1
    elif (board[0] == symbol and board[3] == symbol and board[6] == symbol):
        return 1
    elif (board[1] == symbol and board[4] == symbol and board[7] == symbol):
        return 1
    elif (board[2] == symbol and board[5] == symbol and board[8] == symbol):
        return 1
    elif (board[0] == symbol and board[1] == symbol and board[2] == symbol):
        return 1
    elif (board[3] == symbol and board[4] == symbol and board[5] == symbol):
        return 1
    elif (board[6] == symbol and board[7] == symbol and board[8] == symbol):
        return 1
    else:
        return 0

def drawBoard(boardVals):
    print("\t" + boardVals[0] + "\t|\t" + boardVals[1] + "\t|\t" + boardVals[2] + "\t")
    print("------------------------------------------------")
    print("\t" + boardVals[3] + "\t|\t" + boardVals[4] + "\t|\t" + boardVals[5] + "\t")
    print("------------------------------------------------")
    print("\t" + boardVals[6] + "\t|\t" + boardVals[7] + "\t|\t" + boardVals[8] + "\t")

def main():
    selection = teamChoice()
    if selection == "X":
        computerSelection = "O"
    else:
        computerSelection = "X"
    first = intro()
    if first == 0:
        while True:
            playerMoveChoice(selection)
            if winnerCheck(board, selection) == 1:
                print("You win!")
                break
            computerMoveChoice(computerSelection)
            if winnerCheck(board, computerSelection) == 1:
                print("You lose!")
                break
    else:
        while True:
            computerMoveChoice(computerSelection)
            if winnerCheck(board, computerSelection) == 1:
                print("You lose!")
                break
            playerMoveChoice(selection)
            if winnerCheck(board, selection) == 1:
                print("You win!")
                break

main()
