#add Welcome message
print('\t\t\t\t-----Welcome to tic tac toe-----')

#this function verify if the value is integer or not
def catch(number):
    try:
        final_value = int(number)
    except ValueError:
        try:
            final_value = int(input('\tType a correct value(Integer):\n\t'))
        except ValueError:
            final_value = catch(number)
    return final_value

#this function verify if this value is 'O' or 'X'
def xoro(letter):
    while not(letter == 'X' or letter == 'x' or letter == 'O' or letter == 'o'):
        letter = input('\tType a correct value(\'X\' or \'O\'):\n\t')
    return letter

#This function display a board
def display_board(lis):
    for i in range(len(lis)):
        print('\t', i + 1, lis[i][0], lis[i][1], lis[i][2])
    print('\t','  ', 1,' ',2,' ',3)
    print('\n')
    
#this function assign 'X' or 'Y', depend of the player1 selection
def selection(player, favourite_figure):
    if player == 'Player1':
        if favourite_figure == 'X':
            return '[X]'
        else:
            return '[O]'
    else:
        if favourite_figure == 'X':
            return '[O]'
        else:
            return '[X]'

#In this part, i make the board and display it
board = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]

#add interactivity
play = 1
while play == 1:
    print('\n\tSelect "O" if you want to play with "O", or "X" if you want to play with "X"')
    letter_select = xoro(input('\t'))
    letter_select = letter_select.capitalize()

    print('\n\tInstructions:\n\tFor fill it the squares, write two numbers that correspond to rows and columns\n\te.g.'
    ' if you write 12 you should output:')
    print(f'''
    \t1 [ ] [{letter_select}] [ ]
    \t2 [ ] [ ] [ ]
    \t3 [ ] [ ] [ ]
    \t   1   2   3
    ''')
    print('\tWarning: If you type an incorrect value, you will lost your turn e.g. 14\n\tWarning:If you type one value that someone typed before e.g. 12')

    counter = 0
    i1 = 0 #Refers to index one
    i2 = 0 #Refers to index two
    victory = False #Boolean value that i use to look at if you winner or not

    while counter < 9:
        i1 = 0
        try: 
            player1 = catch(input('\tPlayer1: '))
            while player1 >= 10:
                player1 -= 10
                i1 += 1
            i2 = player1
            if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
                print('\tInvalid value, lost your turn')
                counter -= 1
            else:
                board[i1-1][i2-1] = selection('Player1', letter_select)
        except IndexError:
            print('\tInvalid value, lost your turn')
            counter -= 1
        display_board(board)
        counter += 1
    
        if counter == 9:
            break
    
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
                victory = True
            if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
                victory = True
        
        if victory == True:
            print('\tPlayer1 win')
            break
    
        if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
            print('\tPlayer1 win')
            break
    
        i1 = 0
        try:
            player2 = catch(input('\tPlayer2: '))
            while player2 >= 10:
                player2 -= 10
                i1 += 1
            i2 = player2
            if board[i1-1][i2-1] == '[O]' or board[i1-1][i2-1] == '[X]':
                print('\tInvalid value, lost your turn')
                counter -= 1
            else:
                board[i1-1][i2-1] = selection('Player2', letter_select)
        except IndexError:
            print('\tInvalid value, lost your turn')
            counter -= 1
        display_board(board)
        counter += 1
    
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] == '[O]' or board[i][0] == board[i][1] == board[i][2] == '[X]':
                victory = True
            if board[0][i] == board[1][i] == board[2][i] == '[O]' or board[0][i] == board[1][i] == board[2][i] == '[X]':
                victory = True
        
        if victory == True:
            print('\tPlayer2 win')
            break
    
        if board[2][0] == board[1][1] == board[0][2] == '[O]' or board[0][0] == board[1][1] == board[2][2] == '[O]' or board[2][0] == board[1][1] == board[0][2] == '[X]' or board[0][0] == board[1][1] == board[2][2] == '[X]':
            print('\tPlayer2 win')
            break
    
    board = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]
    print('If you like to play again press 1 otherwise 0')
    play = int(input())
    while play < 0 or play > 1:
        play = catch(input('Type a correct value(0-1)\n'))
        