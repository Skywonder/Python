#othello GUI
#to do - list
#make direct copy of game board after the values are set
#draw oval for the starting point take the setting directly from the othello game board setting


import tkinter as tk
from tkinter import *
from othello_gui_logic import *

DEFAULT_FONT = ('Helvetica', 14)
MINICANVASHEIGHT = 100
MINICANVASWIDTH = 100
stickyAll = 'WENS'
game = OthelloGame(0, 0, None , False, 0, 0, None)

def myName() -> ((int, str)):
    return ((71018021, "Kuan-Ping Chang"))

    
class Gui():
    def __init__(self, root):
        self.gamelive = True
        self.root = root
        self.root.resizable(True, True)
        self.entry = tk.Entry(root)
        self.toplevel = tk.Toplevel()
        self.end = False
        self.clicked = False
        self.win = False
        self.b_count = 0
        self.w_count = 0
        self._ok_clicked = False
        self.dialog_window = None
        self.frame = None
        self.valid = False
        self._canvas = None
        self.height = 0
        self.width = 0
        self.mini_height_frac = 0
        self.mini_width_frac = 0
        self.root.rowconfigure(0,weight = 1)
        self.root.columnconfigure(0, weight = 1)
        
        self.row_dialogue()
    
    def buttonSetting(self, window):
        button_frame = tk.Frame(master = self.dialog_window)
        button_frame.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 10, sticky = stickyAll)
        button_frame.columnconfigure(0, weight=1)
        button_frame.rowconfigure(3, weight =1)
        return button_frame


    def dialog_window_setting(self): 
        self.root.withdraw()
        self.dialog_window = self.toplevel
        self.dialog_window.rowconfigure(0, weight=1)
        self.dialog_window.columnconfigure(0, weight =1)
        return self.dialog_window

    def label0_configure(self, label0):
        label0.grid(row=0, column=0, sticky = stickyAll)
        label0.rowconfigure(0, weight =1)
        label0.columnconfigure(0, weight =1)

    def label1_configure(self, label1):
        label1.grid(row=1,column=0, sticky= stickyAll)
        label1.rowconfigure(1, weight =1)
        label1.columnconfigure(0, weight =1)

    def label_entry_configure(self, row_entry):
        row_entry.grid(row = 2, column = 0, sticky= stickyAll)
        row_entry.rowconfigure(2, weight =1)
        row_entry.columnconfigure(0, weight =1)

    def next_button_configure(self, next_button):
        next_button.grid(row=0, column=0, padx = 10, pady = 10, sticky = stickyAll)
        next_button.rowconfigure(0, weight =1)
        next_button.columnconfigure(0, weight=1)

    
    def row_dialogue(self):
        self.dialog_window = self.dialog_window_setting()
        
        label0 = Label(self.dialog_window, text="Please enter even number between 4 and 16", font = ('Helvetica', 12))
        self.label0_configure(label0)
        
        label1=Label(self.dialog_window, text="Set Row:", font = ('Helvetica', 12))
        self.label1_configure(label1)
        
        self._row_entry = Entry(self.dialog_window, font=("Calibri",12),justify="center")
        self.label_entry_configure(self._row_entry)

        button_frame = self.buttonSetting(self.dialog_window)

        next_button = tk.Button(master = button_frame, text = 'Next', font = DEFAULT_FONT, command = lambda:self._on_next_column())
        self.next_button_configure(next_button)
        

    def _on_next_column(self):
        
        #process the entry to checker
        confirm = game.define_row(self._row_entry.get())
        if confirm == True:
            game.setRow(int(self._row_entry.get()))
            self.column_dialogue()
        else:
            self.row_dialogue()
        
        #confirm if the column entry is valid if not request re-entry

    def column_dialogue(self):
        
        self.dialog_window = self.dialog_window_setting()
        
        label0 = Label(self.dialog_window, text="Please enter even number between 4 and 16", font = ('Helvetica', 12))
        self.label0_configure(label0)
        
        label1=Label(self.dialog_window, text="Set Column:", font = ('Helvetica', 12))
        self.label1_configure(label1)
        
        self._column_entry = Entry(self.dialog_window, font=("Calibri",12),justify="center")
        self.label_entry_configure(self._column_entry)

        button_frame = self.buttonSetting(self.dialog_window)

        next_button = tk.Button(master = button_frame, text = 'Next', font = DEFAULT_FONT, command = lambda:self._on_next_turn())
        self.next_button_configure(next_button)
        

    def _on_next_turn(self):
        confirm = game.define_column(self._column_entry.get())
        if confirm == True:
            game.setColumn(int(self._column_entry.get()))
            self.setTurn_dialogue()
        else:
            self.column_dialogue()
        
        #confirm if the column entry is valid if not request re-entry

    def setTurn_dialogue(self):
        
        self.dialog_window = self.dialog_window_setting()
        
        label0 = Label(self.dialog_window, text="Please enter who goes first('B' or 'W')", font = ('Helvetica', 12))
        self.label0_configure(label0)
        
        label1=Label(self.dialog_window, text="Set Turn:", font = ('Helvetica', 12))
        self.label1_configure(label1)

        self._turn_entry = Entry(self.dialog_window, font=("Calibri",12),justify="center")
        self.label_entry_configure(self._turn_entry)
    
        button_frame = self.buttonSetting(self.dialog_window)
        
        next_button = tk.Button(master = button_frame, text = 'Next', font = DEFAULT_FONT, command = lambda:self._on_next_start())
        self.next_button_configure(next_button)

    def _on_next_start(self):
        #use player_start to confirm the input
        confirm = game.player_start(self._turn_entry.get())
        if confirm == black or confirm == white:
            game.setTurn(game.player_start(self._turn_entry.get()))
            self.set_piece_start_dialogue()
        else:
            self.setTurn_dialogue()
        #confirm if the column entry is valid if not request re-entry


    def set_piece_start_dialogue(self):
        
        self.dialog_window = self.dialog_window_setting()
        
        label0 = Label(self.dialog_window, text="Please which piece to start with ('B' or 'W'):", font = ('Helvetica', 12))
        self.label0_configure(label0)
        
        label1=Label(self.dialog_window, text="Set Piece Start:", font = ('Helvetica', 12))
        self.label1_configure(label1)

        self._wOrb_entry = Entry(self.dialog_window, font=("Calibri",12),justify="center")
        self.label_entry_configure(self._wOrb_entry) 

        button_frame = self.buttonSetting(self.dialog_window)

        next_button = tk.Button(master = button_frame, text = 'Next', font = DEFAULT_FONT, command = lambda:self._on_next_condition())
        self.next_button_configure(next_button) 

    def _on_next_condition(self):
        #use player_start to confirm for same thing(black or white)
        confirm = game.player_start(self._wOrb_entry.get())
        if confirm == black or confirm == white:
            #set the board at this point otherwise cannot set piece
            game.setBoard(self._gui_board())
            game.setPieceStart(self._wOrb_entry.get())
            self.setCondition_dialogue()
        else:
            self.set_piece_start_dialogue()
        #confirm if the column entry is valid if not request re-entry

    def setCondition_dialogue(self):
        
        self.dialog_window = self.dialog_window_setting()
        
        label0 = Label(self.dialog_window, text="Please enter the winning condition ('>' or '<'):", font = ('Helvetica', 12))
        self.label0_configure(label0)
        
        label1=Label(self.dialog_window, text="Set Condition:", font = ('Helvetica', 12))
        self.label1_configure(label1)

        self._condition_entry = Entry(self.dialog_window, font=("Calibri",12),justify="center")
        self.label_entry_configure(self._condition_entry)

        button_frame = self.buttonSetting(self.dialog_window)
        
        #since this is last condition - use start button to start the game
        start_button = tk.Button(master = button_frame, text = 'Start', font = DEFAULT_FONT, command = lambda:self._on_final_button())
        start_button.grid(row=0, column = 0, padx = 10, pady = 10, sticky = stickyAll)
        start_button.columnconfigure(0, weight=1)
        start_button.rowconfigure(0, weight =1)

    def _on_final_button(self):
        #use player_start to confirm for same thing(black or white)
        confirm = game.win_condition(self._condition_entry.get())
        
        if confirm == ">" or confirm == "<":
            game.setCondition(self._condition_entry.get())
            self._on_start_game()
        else:
            self.setCondition_dialogue()

    
    def _on_start_game(self):
        root.deiconify()
        self.toplevel.destroy()
        self.game_Start(game)
        game.print_board()

    def _on_quit_button(self) -> None:
        self.end = True
        self.root.destroy()

   
        
        
    def game_Start(self, game):
        #create the starting canvas of the game - the width of the entire canvas is canvas.width, and the height of the entire canvas is canvas.height 
        self._canvas = tk.Canvas(master = self.root, width= MINICANVASWIDTH * game.getColumn() , height= MINICANVASHEIGHT * game.getRow(), background='green')
        self._canvas.grid(row=0, column=0, padx = 10, pady = 10, sticky = stickyAll)
        self._canvas.rowconfigure(0, weight =1)
        self._canvas.columnconfigure(0, weight =1)
        game_board = game.copy_board()
        
        self._canvas.bind("<Configure>", self.on_canvas_drawline())

        self._canvas.bind("<Configure>", self.on_piece_resized(game_board))

        self._canvas.bind("<Configure>", self.on_score_resized())

    def on_score_resized(self):
        self._show_game_score()

    def on_piece_resized(self, gameboard):
        self.draw_board(gameboard)
        
    def on_canvas_drawline(self):
        self._canvas.delete("all")
        
        #whatever the new canvas width and height
        for i in range(1, game.getColumn()):
            self.draw_line(i)

    def draw_line(self, i):
        self.width = self._canvas.winfo_reqwidth()
        self.height = self._canvas.winfo_reqheight()
        self._canvas.config(width=self.width, height=self.height)

        #need to update the mini canvas to get the new accurate height 
        self.mini_height_frac = (self.width/MINICANVASHEIGHT)/game.getRow()
        self.mini_width_frac = (self.height/MINICANVASWIDTH)/game.getColumn()
            #draw horizontal line
        self._canvas.create_line(0, i * MINICANVASHEIGHT * self.mini_height_frac, MINICANVASWIDTH * self.mini_width_frac * game.getColumn(), i * MINICANVASHEIGHT * self.mini_height_frac)
            
            #draw vertical line
        self._canvas.create_line(i*MINICANVASWIDTH * self.mini_width_frac, 0, i* MINICANVASWIDTH * self.mini_width_frac, MINICANVASHEIGHT * self.mini_height_frac *game.getRow())

        self._canvas.rowconfigure(0, weight =1)
        self._canvas.columnconfigure(0, weight =1) 

            
    def draw_board(self, board):
        game.print_board()
        for x in range(game.getRow()):
            for y in range(game.getColumn()):
                if board[x][y] == black:
                    board[x][y] = self._canvas.create_oval(y* (MINICANVASWIDTH * self.mini_width_frac) + 2, x * (MINICANVASHEIGHT * self.mini_height_frac) + 2, (y+1)*(MINICANVASWIDTH * self.mini_width_frac)-2,
                        (x+1)*(MINICANVASHEIGHT * self.mini_height_frac)-2, fill="black", outline ="#DDD", width = 4)
                    self._canvas.rowconfigure(0, weight =1)
                    self._canvas.columnconfigure(0, weight =1)
                elif board[x][y] == white:
                    board[x][y] = self._canvas.create_oval(y*(MINICANVASWIDTH * self.mini_width_frac)+ 2, x *(MINICANVASHEIGHT * self.mini_height_frac) + 2, (y+1)*(MINICANVASWIDTH * self.mini_width_frac)-2,
                        (x+1)*(MINICANVASHEIGHT * self.mini_height_frac)-2, fill="white", outline ="#DDD", width = 4)
                    self._canvas.rowconfigure(0, weight =1)
                    self._canvas.columnconfigure(0, weight =1)

        
    def _show_game_score(self):
        score_frame = Frame(self.root)
        score_frame.grid(row=1,column=0, sticky= stickyAll)
        score_frame.rowconfigure(1, weight =1)
        
        score_frame.columnconfigure(0, weight =1)
        score_frame.columnconfigure(1, weight =1)
        
        label4 = Label(score_frame, text="Black Score:", font = ('Helvetica', 20))
        label4.grid(row=2,column=0, sticky=stickyAll)
        label4.rowconfigure(2, weight =1)
        label4.columnconfigure(0, weight =1)
        
        label5 = Label(score_frame, text="White Score:", font = ('Helvetica', 20))
        label5.grid(row=2,column=1, sticky=stickyAll)
        label5.rowconfigure(2, weight=1)
        label5.columnconfigure(1, weight =1)
        
        self.b_count, self.w_count = game.count()
        game.setBcount(self.b_count)
        game.setWcount(self.w_count)
        
        self.score_canvas1 = tk.Canvas(score_frame, width= MINICANVASWIDTH * game.getColumn()//2 , height= MINICANVASHEIGHT * game.getRow()//4, background='white')
        self.score_canvas1.grid(row=3,column=0, sticky = stickyAll)
        self.score_canvas1.create_text(100, 50, anchor = CENTER, fill = "darkblue", font = ('Helvetica', 20), text = "{}".format(game.getBcount()))

        self.score_canvas1.rowconfigure(3, weight =1)
        self.score_canvas1.columnconfigure(0, weight =1)
        
        self.score_canvas2 = tk.Canvas(score_frame, width= MINICANVASWIDTH * game.getColumn()//2 , height= MINICANVASHEIGHT * game.getRow()//4, background='white')
        self.score_canvas2.grid(row=3,column=1, sticky = stickyAll)
        self.score_canvas2.create_text(100, 50, anchor = CENTER, fill = "darkblue", font = ('Helvetica', 20), text = "{}".format(game.getWcount()))

        self.score_canvas2.rowconfigure(3, weight =1)
        self.score_canvas2.columnconfigure(1, weight =1)
        
        self._canvas.bind("<Button-1>", self.on_click)
        self.root.update()


    def _gui_board(self):
        self.gui_board = []
        for x in range(game.getRow()):
            self.gui_board.append([])
            for y in range(game.getColumn()):
                self.gui_board[-1].append('.')
        
        return self.gui_board


    def on_click(self, event:tk.Event):
        
        #get the click point and convert to simple x, y coordinate for board. Change board directly if the point is valid.
        self.point = (event.y//(MINICANVASHEIGHT * self.mini_height_frac), event.x//(MINICANVASWIDTH * self.mini_width_frac))
        self.clicked = True
        
        p_row, p_column = self.point
        p_row, p_column = [int(p_row), int(p_column)]
        print(p_row, p_column)
        int_point = (p_row, p_column)
        #check if any avaliable move is valid
        check = game.new_avaliable_move(int_point, game.getTurn(), game.getBoard())
        #check if any possible move is valid
        check0 = game.possible_moves()
        #check if the board is filled
        check1 = game.end_game_checker()
        
        self._show_game_score()
        
        if check == True:
            game_board = game.copy_board()
            self.draw_board(game_board)
## added line below
##            self._canvas.bind("<Configure>", self.on_canvas_drawline())
##            self._canvas.bind("<Configure>", self.on_piece_resized(game_board))
            
            game.setTurn(game.next_player_turn())

        if check == False:
        #this make sure if the is empty it will change to the possible player with moves
            if check0 != False:
                game.setTurn(check0)
            if check0 == False:
                #this ends the game and goes to calculate winner
                self.gamelive = False
                self.game_condition()
        
        if check1 == True:
            self.gamelive = False
            self.game_condition()

    
    def _on_end_button(self) -> None:
        self._ok_clicked = True
        self.dialog_window.destroy()
        self.root.destroy()

    def _on_cancel_button(self) -> None:
        self.dialog_window.destroy()
        
        
    def end_dialogue(self, message):
        self.dialog_window = tk.Toplevel()
        self.dialog_window.rowconfigure(0, weight=1)
        self.dialog_window.columnconfigure(0, weight =1)
        
        game_over_label = tk.Label(master = self.dialog_window, text = message, font = DEFAULT_FONT)

        game_over_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = stickyAll)
        game_over_label.rowconfigure(0, weight=1)
        game_over_label.columnconfigure(0, weight =1)
        
        button_frame = tk.Frame(master = self.dialog_window)
        
        button_frame.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = stickyAll)
        button_frame.columnconfigure(0, weight=1)
        button_frame.rowconfigure(1, weight=1)
            
        end_button = tk.Button(master = button_frame, text = 'END', font = DEFAULT_FONT, command = lambda:self._on_end_button())
        end_button.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = stickyAll)
        end_button.columnconfigure(0, weight = 1)
        end_button.rowconfigure(0, weight =1)



    def game_condition(self):
        if self.gamelive == False:
            if game.getCondition() == ">":
                message = higher_winner(game.getBcount(), game.getWcount())
                self.end_dialogue(message)
                


            if game.getCondition() == "<":
                message = lower_winner(game.getBcount(), game.getWcount())
                self.end_dialogue(message)
            
        
if __name__== '__main__':
    
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()
    
