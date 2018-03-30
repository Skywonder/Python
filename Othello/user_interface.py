##ID: 71018021  Name: Kuan-Ping Chang

from logics import *

def myName() -> ((int, str)):
    return ((71018021, "Kuan-Ping Chang"))

def user_interface():
    game = OthelloGame(0, 0, None , False, 0, 0, None)
    
    game.setRow(game.define_row())
    game.setColumn(game.define_column())
    game.setTurn(game.player_start())
    game.setBoard(game.game_board())
    
    game.setPieceStart()
    game.setCondition(game.win_condition()) 

    
    win = False
    
    while win != True:
        b_count, w_count = game.count()
        print("B:{} W:{}".format(b_count, w_count))
        game.print_board()
        
        game.setTurn(game.player_move())

        
        if game.getTurn() == False:
            win = True
            
        else:    
            win = game.end_game_checker()

        
    b_count, w_count = game.count()
    print("B:{} W:{}".format(game.getBcount(), game.getWcount()))
    game.print_board()    
    if game.getCondition() == '>':
        #print(game.getCondition())
        higher_winner(game.getBcount(), game.getWcount())
    else:
        #print(game.getCondition())
        lower_winner(game.getBcount(), game.getWcount())
        

if __name__ == '__main__':
    user_interface()
