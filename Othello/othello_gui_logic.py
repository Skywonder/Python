##ID: 71018021  Name: Kuan-Ping Chang


#Reads 5 input
#1st line: Specifies the number of rows on the board even number between 4-16(inclusive)
#2nd line: Specifies the number of column on the board which will be an even interger ^
#3rd line: Specifies which player will move first (black or white)
#4th line: Specifies the arrangement of the cells on the board. (4 disc on board 2 white and 2 black at center as start)
#5th line: Winning condition: most ">" won and least "<" won
#make Classes: Pieces and OthelloGame 

class OthelloPiece():
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        
    def __repr__(self):
        return("OthelloPiece:({})".format(self.__name[0].lower()))
    def __str__(self):
        return("{:s}".format(str(self.__name[0])))

black = OthelloPiece("B")
white = OthelloPiece("W")


class OthelloGame():
    '''The game object'''
    def __init__(self, row = 0, column = 0, turn = None, condition = "", b_count = 0, w_count = 0, board = None):
        self.__row = row
        self.__column = column
        self.__turn = turn
        self.__condition = condition
        self.__b_count = b_count
        self.__w_count = w_count
        self.__board = board

    #get and set the row of the board
    def setRow(self, row):
        self.__row = row

    def getRow(self):
        return self.__row

    #get and set the column of the board
    def setColumn(self, column):
        self.__column = column

    def getColumn(self):
        return self.__column

    #get and set the turn of the game
    def setTurn(self, turn):
        self.__turn = turn

    def getTurn(self):
        return self.__turn

    #set and get win condition of the game:
    def setCondition(self, condition):
        self.__condition = condition

    def getCondition(self):
        return self.__condition
    
    #get and set the counts for b or w
    def getBcount(self):
        return self.__b_count

    def setBcount(self, x_count):
        self.__b_count = x_count

    def getWcount(self):
        return self.__w_count

    def setWcount(self, w_count):
        self.__w_count = w_count


    #get and set the board
    def setBoard(self, board):
        self.__board = board

    def getBoard(self):
        return self.__board

    def setFlip(self, flip = list()):
        self.__flip = flip

    def getFlip(self):
        return self.__getFlip

    def define_row(self, row) -> int:
        '''Return the number of row'''
        while True:
            
            try:
                row = int(row)
                if row >= 4 and row <= 16 and row%2 == 0:
                    return True
                else:
                    print("The row value has to be between 4~ 16 and even")
                    return False
            except:
                print("The row value has to be between 4 ~ 16 and even")
                return False

    def define_column(self, column) -> int:
        '''Return the number of column'''
        while True:
           
            try:
                column = int(column)
                if column >= 4 and column <= 16 and column%2 == 0:
                    return True
                else:
                    print("The column value has to be between 4~16 and even")
                    return False
            except:
                print("The column value has to be between 4 ~ 16 and even")       
                return False


    def player_start(self, starter) -> str:
        '''Return the starting piece: black or white'''
        
        if starter[0].lower() == 'b':
            starter = black
            return starter

        elif starter[0].lower() == 'w':
            starter = white
            return starter



    def win_condition(self, condition) -> str:
        '''Return the condition'''
        while True:
            if condition == ">":
                return condition
            elif condition == "<":
                return condition
            else:
                print("Please enter the valid condition: '>' or '<' ")
                return False
                


    def setPieceStart(self, position) -> [[str]]:
        '''Return the board with set pieces depending on input'''
        while True:
            if position[0].lower() == 'b' or position[0].lower() == 'w':

                for x in range(self.__row):
                    for y in range(self.__column):
                        if x == self.__row//2 - 1 and y == self.__column//2 - 1:
                            if position.lower() == 'b':
                                self.__board[x][y] = black
                            else:
                                self.__board[x][y] = white
                            #print(board[row][column], end = '')

                        elif x == self.__row//2 - 1 and y == self.__column//2:
                            if position.lower() == 'b':
                                self.__board[x][y] = white
                            else:
                                self.__board[x][y] = black
                            #print(board[row][column], end = '')

                        elif x == self.__row//2 and y == self.__column//2: 
                            if position.lower() == 'b':
                                self.__board[x][y] = black
                            else:
                                self.__board[x][y] = white
                            #print(board[row][column], end = '')

                        elif x ==self.__row//2 and y == self.__column//2 - 1:
                            if position.lower() == 'b':
                                self.__board[x][y] = white
                            else:
                                self.__board[x][y] = black
                            #print(board[row][column], end = '')                     
                return self.__board
            else:
                print("Invalid input")

        

    def game_board(self) -> [[str]]:
        '''Return a list. Create an empty board'''
        board = []
        for x in range(self.__row):
            board.append([])
            for y in range(self.__column):
                board[-1].append('.')
        return board

    def copy_board(self) -> list:
        '''Return a list of the Copied board'''
        #fix this tomorrow not exact copy
        board_copy=[]
        for x in range(self.__row):
            board_copy.append([])
            for y in range(self.__column):
                board_copy[-1].append(self.__board[x][y])
        return board_copy


    def print_board(self) -> None:
        '''Print the current board'''
     
        for row in self.__board:
            for column in row:
                print(column, end = '')
            print(end = "\n")
        
        
    def othello_logic_checker(self, point, starter, board) -> list:
        '''Return the list containing the valid points found otherwise return false.'''
        #print(point)
        if starter == black:
            other = white
        else:
            other = black

        #row and column -1 to make sure it in range (0, 1, 2, 3) not (0, 1, 2, 3, 4)
        row = self.__row - 1
        column = self.__column -1 
        check = True
        x_s, y_s = point
        #print(x_s, y_s)
        x = x_s
        y = y_s
        original = board[x_s][y_s]
        
        
        #make sure if the block is empty and outside the parameter
        if board[x_s][y_s] != '.' and not(x >= 0 and x <= row and y >= 0 and y <= column):
            return False

        #make sure if the black is empty and not preoccupied, this make sure that if previous block with range is not True, this can check.
        if board[x_s][y_s] != '.':
            return False

        #make a list to store points that can be flipped
        spotFlipping = []
        
        #set it for now
        board[x_s][y_s] = starter
        #self.print_board()

        #print_board(board)
        #check all direction increment by 1
                
        for x_dir, y_dir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x = x_s
            y = y_s
            x += x_dir
            y += y_dir
            #print("searching direction", x, y)
            #check if its within game board range
            if x >= 0 and x <= row and y >= 0 and y <= column and board[x][y] == other:
                    #continue searching for the next other piece
                    while board[x][y] == other:     
                        x += x_dir
                        y += y_dir
                        #break it if not within range or hit start
                        if not(x >= 0 and x <= row and y >= 0 and y <= column):
                           break
                        elif board[x][y] == starter:
                            break
                    #make sure to reloop if the hit point is not within range    
                    if not(x >= 0 and x <= row and y >= 0 and y <= column):
                        continue
                
                    #go reverse direction if starter is hit 
                    if board[x][y] == starter:
                        while True:
                            x -= x_dir
                            y -= y_dir
                            #if hit the starting point break
                            if x == x_s and y == y_s:
                                break
                            #print(x, y)
                            spotFlipping.append([x, y])
        board[x_s][y_s] = original # restore original item
        #print(spotFlipping)
        if len(spotFlipping) == 0: # If no tiles were flipped, this is not a valid move.
            return False

        #print(spotFlipping)
        return spotFlipping

    def new_avaliable_move(self, point, starter, board)-> bool:
        '''Return boolean and set the pieces to the board. Control flip and check if move is valid'''
        spotToflip = self.othello_logic_checker(point, starter, board)
        
        if spotToflip == False:
            
            return False

        else:
            x_s, y_s = point
            self.__board[x_s][y_s] = self.__turn

            for x, y in spotToflip:
                self.__board[x][y] = self.__turn

            return True
            

            
    def player_move(self) -> bool:
        '''Return the condition in the format: black, white, or False'''
        print("TURN: {}".format(self.__turn))
        
        while True:           
            try:
                p_row, p_column = input("").split()
                p_row, p_column = [int(p_row), int(p_column)]
                p_row = p_row - 1
                p_column = p_column - 1
                point = (p_row, p_column)
                starter = self.__turn
                board = self.__board
                validity = self.avaliable_move(point, starter, board)

                if validity == False:
                    print("INVALID")
                

                else:
                    # switch player
                    self.__turn = self.next_player_turn()
                    # check for possible moves for the player (check both white and black)
                    check_starter = self.possible_moves()
                    print("VALID")

                    return check_starter
                
            except ValueError:
                print("INVALID")
            except IndexError:
                print("INVALID")
            
        
    def next_player_turn(self) -> object:
        '''Return the switched turn'''
        if self.__turn == black:
            return white
            
        elif self.__turn == white:
            return black

            
    
    def possible_moves(self) -> object:
        '''Check if player has any valid move, if not then skip and return to the previous player'''
        starter_possibleMoves = []
        other_possibleMoves = []
        starter = self.__turn
        original_board = self.__board
        row = self.__row
        column = self.__column
        
        if starter == black:
            other = white

        elif self.__turn == white:
            other = black

            
        for x in range(row):
            for y in range(column):
                point = (x, y)
                if self.othello_logic_checker(point, starter, original_board) != False:
                    if self.__board[x][y] != white and self.__board[x][y] != black:
                        starter_possibleMoves.append([x,y])
                        
                if self.othello_logic_checker(point, other, original_board) != False:
                    if self.__board[x][y] != white and self.__board[x][y] != black:
                        other_possibleMoves.append([x,y])
                    #print("checker")

        #print(starter_possibleMoves)
        #print(other_possibleMoves)
        
        if len(starter_possibleMoves) != 0:
            return starter

        #check if both side runs out of possible moves if so return False
        if starter_possibleMoves == other_possibleMoves:
            return False

        if len(starter_possibleMoves) == 0:
            return other
        

    def end_game_checker(self) -> bool:
        '''Return False if the game board has no more empty spot possible'''
        count = 0
        for x in range(self.__row):
            for y in range(self.__column):
                if self.__board[x][y] == '.':
                    count += 1
        #print(count)
        if count > 0:
            return False
        else:
            return True
        
        
    def count(self) -> (int, int):
        ''' Return tuple count'''
        bcount = 0
        wcount = 0
        for x in range(self.__row):
            for y in range(self.__column):
                if self.__board[x][y] == black:
                    bcount += 1
                    
                if self.__board[x][y] == white:
                    wcount += 1
                    
        #set the count number
        self.__b_count = bcount
        self.__w_count = wcount
        
        return (self.__b_count, self.__w_count)



def higher_winner(bcount, wcount) -> None:
    '''Print out the winner with the greater number of pieces'''
    if bcount > wcount:
        print("WINNER: BLACK PLAYER!!")
        string = 'WINNER: BLACK PLAYER!!'
        return string
        
    elif wcount > bcount:
        print("WINNER: WHITE PLAYER!!")
        string = 'WINNER: WHITE PLAYER!!'
        return string
    
    else:
        print("WINNER: IT'S A TIE!!!")
        string = "WINNER: IT'S A TIE!!!"
        return string
    
def lower_winner(bcount, wcount) -> None:
    '''Print out the winner with the lesser number of pieces'''
    if bcount < wcount:
        print("WINNER: BLACK PLAYER!! ")
        string = 'WINNER: BLACK PLAYER!! '
        return string
        
    elif wcount < bcount:
        print("WINNER: WHITE PLAYER!!")
        string = 'WINNER: WHITE PLAYER!!'
        return string
    else:
        print("WINNER: IT'S A TIE!!!")
        string = "WINNER: IT'S A TIE!!!"
        return string
