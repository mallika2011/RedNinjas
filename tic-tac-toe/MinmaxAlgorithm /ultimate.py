import math
import numpy as np

#Implementation of Two Player Tic-Tac-Toe game in Python.

#ASSUME AGENT IS MAXIMIZER AND 
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

global BigTree 
theBoard = np.zeros((3,3),dtype=object)
checkboard= np.zeros((3,3),dtype=str)
board_keys = []
HUMAN = 'X'
AGENT = 'O'
EMPTY = ' '
TIE = 'T'
MAX_UTIL = 10

def set_up_board():
    for i in range(0,3):
        for j in range(0,3):
            smallboard=np.zeros((3,3),dtype=str)
            for m in range(0,3):
                for n in range(0,3):
                    smallboard[m][n]=EMPTY
                    # if i==0 and m==0 : 
                    #     smallboard[m][n]=HUMAN
            theBoard[i][j]=smallboard 

    for i in range(0,3):
        for j in range(0,3):
            checkboard[i][j]=EMPTY

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    for i in range(0,3): #outerrows
        sb1=board[i][0]
        sb2=board[i][1]
        sb3=board[i][2]
        for j in range(0,3): # innerrows
            print(sb1[j][0] + '|' + sb1[j][1] + '|' + sb1[j][2] + " | " ,end=" ")
            print(sb2[j][0] + '|' + sb2[j][1] + '|' + sb2[j][2] + " | " ,end=" ")
            print(sb3[j][0] + '|' + sb3[j][1] + '|' + sb3[j][2] ,)
            if j<2:
                print('-+-+-' + ' |' + '  -+-+-' + ' |' + '  -+-+-')
        if i<2:
            print("-------------------------")

def checkwin(board):
    # Cheking smallboards for win
    for i in range(0,3):
        for j in range(0,3):
            if checkboard[i][j]==EMPTY:
                smallboard=board[i][j]
                for r in range(0,3):
                    if smallboard[r][0] == smallboard[r][1] == smallboard[r][2] != EMPTY:
                        if smallboard[r][0] == AGENT:
                            checkboard[i][j]=AGENT
                        else:
                            checkboard[i][j]=HUMAN

                for c in range(0,3):
                    if smallboard[0][c] == smallboard[1][c] == smallboard[2][c] != EMPTY :
                        if smallboard[0][c] == AGENT:
                            checkboard[i][j]=AGENT
                        else:
                            checkboard[i][j]=HUMAN 

                if smallboard[0][0]==smallboard[1][1]==smallboard[2][2] != EMPTY :
                    if smallboard[0][0] == AGENT:
                        checkboard[i][j]= AGENT
                    else:
                        checkboard[i][j] = HUMAN 

                if smallboard[0][2]==smallboard[1][1]==smallboard[2][0] != EMPTY :
                    if smallboard[0][2] == AGENT:
                        checkboard[i][j]= AGENT
                    else:
                        checkboard[i][j] = HUMAN 

                #If all the cells are filled in a small box and no one has won 
                flag=0
                for m in range(0,3):
                    for n in range(0,3):
                        if smallboard[m][n]==EMPTY:
                            flag=1
                if flag==0 : 
                    checkboard[i][j]=TIE

    # checking the globalboard for win 
    for r in range(0,3):
        if checkboard[r][0] == checkboard[r][1] == checkboard[r][2] != EMPTY:
            return 1

    for c in range(0,3):
        if checkboard[0][c] == checkboard[1][c] == checkboard[2][c] != EMPTY:
            return 1

    if checkboard[0][0]==checkboard[1][1]==checkboard[2][2] != EMPTY : 
        return 1 
    
    if checkboard[0][2]==checkboard[1][1]==checkboard[2][0] != EMPTY :
        return 1 

    return 0 

def print_game_over(turn):
    print("\nGame Over.\n")                
    print(" **** " +turn + " won. ****")  

def is_moves_left(board):

    for i in range(0,3):
        for j in  range(0,3):
            if board[i][j]==EMPTY:
                return True
    return False

def calc_score(b):


    for r in range(0,3):
        if b[r][0] == b[r][1] == b[r][2] != EMPTY:
            if b[r][0] == AGENT:
                return MAX_UTIL
            else:
                return -MAX_UTIL

    for c in range(0,3):
        if b[0][c] == b[1][c] == b[2][c] != EMPTY :
            if b[0][c] == AGENT:
                return MAX_UTIL
            else:
                return -MAX_UTIL

    if b[0][0]==b[1][1]==b[2][2] != EMPTY :
        if b[0][0] == AGENT:
            return MAX_UTIL
        else:
            return -MAX_UTIL

    if b[0][2]==b[1][1]==b[2][0] != EMPTY :
        if b[0][2] == AGENT:
            return MAX_UTIL
        else:
            return -MAX_UTIL

    return 0


def minimax(board,depth,is_max):
    
    score = calc_score(board)

    if score == MAX_UTIL:
        return score

    if score == -MAX_UTIL:
        return score

    if is_moves_left(board)==False :
        return 0

    if is_max :

        best_val = -math.inf

        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]==EMPTY):
                    board[i][j] = AGENT
                    best_val = max(best_val,minimax(board,depth+1,not(is_max)))
                    board[i][j]=EMPTY

        return best_val

    else:

        best_val = math.inf

        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]==EMPTY):
                    board[i][j] = HUMAN
                    best_val = min(best_val,minimax(board,depth+1,not(is_max)))
                    board[i][j]=EMPTY

        return best_val


def choose_optimal_move(board):
    
    optimal_val = -math.inf

    for i in range(0,3):
        for j in range(0,3):
            
            if(board[i][j]==EMPTY):

                #Player move? 
                board[i][j]=AGENT
                
                move_val = minimax(board,0,False)

                #Player unmove?
                board[i][j]=EMPTY
            
                if move_val > optimal_val:

                    best_val_row = i
                    best_val_col = j
                    optimal_val = move_val

    return best_val_row, best_val_col, optimal_val
            


def human_turn(board):
    
    printBoard(theBoard)
    print("It's your turn," + HUMAN + ".Move to which place?")
            
    while(True):
        gr , gc = [int(x) for x in input("Enter Global row and coloumn: ").split()] 
        sr , sc = [int(x) for x in input("Enter small row and small coloumn: ").split()] 
        if theBoard[gr][gc][sr][sc] == EMPTY:
            theBoard[gr][gc][sr][sc] = HUMAN
            break
        else:
            print("That place is already filled.\nMove to which place?")
            continue

def agent_turn(board):
    printBoard(theBoard)
    print(AGENT + " is moving please wait ...")
    
    r,c,val = choose_optimal_move(board)
    theBoard[r][c] = AGENT

# Now we'll write the main function which has all the gameplay functionality.
def game():

    set_up_board()
    turn = HUMAN
    count = 0

    while(True):
        
        if(turn==HUMAN):
            human_turn(theBoard)
            count+=1
        else:
            agent_turn(theBoard)
            count+=1
        
        did_win = False
        did_win=checkwin(theBoard)

        if did_win :
            print_game_over(turn)
            break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        flag=0
        for m in range(0,3):
            for n in range(0,3):
                if checkboard[m][n]==EMPTY:
                    flag=1
        if flag==0 :
            print("GameOver")
            print("It's a tie ")
            break 

        # Now we have to change the player after every move.
        if turn ==HUMAN:
            turn = AGENT
        else:
            turn = HUMAN        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        game()

if __name__ == "__main__":
    game()