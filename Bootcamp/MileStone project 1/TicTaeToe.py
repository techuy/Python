#a function to display tic tac toe board

def display_board(board):
    print("\n"*100)
    #print("    |     |    ")
    print(board[7]+"|"+board[8]+"|"+board[9])
    #print("    |     |    ")
    #print("----------------")
    #print("    |     |    ")
    print(board[4]+"|"+board[5]+"|"+board[6])
    #print("    |     |    ")
    #print("----------------")
    #print("    |     |    ")
    print(board[1]+"|"+board[2]+"|"+board[3])
    #print("    |     |    ")

#Assign marker to each player
def player_input():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = input("Player 1: Please pick a marker 'X' or 'O': ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#test_board = ['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
#position = int(input("Please input number you want to place from 1-9: "))

def place_marker (board,marker,positon):
    board[positon] = marker


#check player
def win_check (board,mark):
    #check all row and check if they all share the same marker
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    #check colume
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    #diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark))

import random
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#check the board in that position is available or not
def space_check(board,position):
    return (board[position]!='X' or board[position]!="O")



#check the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board,turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(turn+" Choose a position(1-9): "))
    return position

def replay():
    choice = input("Play Again? Y/N: ")
    return choice == "Y"

    
print("Welcome to Tic Tac Toe Game")

while True:
    #set up a board
    the_board = ["#","1","2","3","4","5","6","7","8","9"]
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn+" Will go first")

    play_game = input("Ready? y/n: ")
    if(play_game=='y'):
        game_on = True
    else:
        game_on= False
    
    while game_on:
        #player 1 first
        if turn == "Player 1":
            #display the board
            display_board(the_board)
            #choose a position
            poistion = player_choice(the_board,turn)
            #place the marker on the position
            place_marker(the_board,player1_marker,poistion)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 WON")
                game_on=False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                
            #if no tie or win, next plaxyer turn
                else: turn = "Player 2"
        
        else:
             #display the board
            display_board(the_board)
            #choose a position
            poistion = player_choice(the_board,turn)
            #place the marker on the position
            place_marker(the_board,player2_marker,poistion)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 WON")
                game_on=False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                
            #if no tie or win, next player turn
                else: turn = "Player 1"
    if not replay():
        break

# a function to display tic tac toe board  
def display_board(board):
    print("\n"*100)
    #print("    |     |    ")
    print(board[7]+"|"+board[8]+"|"+board[9])
    #print("    |     |    ")
    #print("----------------")
    #print("    |     |    ")
    print(board[4]+"|"+board[5]+"|"+board[6])
    #print("    |     |    ")
    #print("----------------")
    #print("    |     |    ")
    print(board[1]+"|"+board[2]+"|"+board[3])
    #print("    |     |    ")

#Assign marker to each player
def player_input():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = input("Player 1: Please pick a marker 'X' or 'O': ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#test_board = ['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
#position = int(input("Please input number you want to place from 1-9: "))

def place_marker (board,marker,positon):
    board[positon] = marker


#check player
def win_check (board,mark):
    #check all row and check if they all share the same marker
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    #check colume
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    #diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark))

import random
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#check the board in that position is available or not
def space_check(board,position):
    return (board[position]!='X' or board[position]!="O")



#check the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board,turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(turn+" Choose a position(1-9): "))
    return position

def replay():
    choice = input("Play Again? Y/N: ")
    return choice == "Y"

    
print("Welcome to Tic Tac Toe Game")

while True:
    #set up a board
    the_board = ["#","1","2","3","4","5","6","7","8","9"]
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn+" Will go first")

    play_game = input("Ready? y/n: ")
    if(play_game=='y'):
        game_on = True
    else:
        game_on= False
    
    while game_on:
        #player 1 first
        if turn == "Player 1":
            #display the board
            display_board(the_board)
            #choose a position
            poistion = player_choice(the_board,turn)
            #place the marker on the position
            place_marker(the_board,player1_marker,poistion)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 WON")
                game_on=False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                
            #if no tie or win, next plaxyer turn
                else: turn = "Player 2"
        
        else:
             #display the board
            display_board(the_board)
            #choose a position
            poistion = player_choice(the_board,turn)
            #place the marker on the position
            place_marker(the_board,player2_marker,poistion)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 WON")
                game_on=False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                
            #if no tie or win, next player turn
                else: turn = "Player 1"
        
    if not replay():
            break