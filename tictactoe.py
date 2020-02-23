from tkinter import *
from tkinter import messagebox
import copy

squares = {
          'r1c1':{'location':[0,0,150,150],'status':None},
          'r1c2':{'location':[150,0,300,150],'status':None},
          'r1c3':{'location':[300,0,450,150],'status':None},
          'r2c1':{'location':[0,150,150,300],'status':None},
          'r2c2':{'location':[150,150,300,300],'status':None},
          'r2c3':{'location':[300,150,450,300],'status':None},
          'r3c1':{'location':[0,300,150,450],'status':None},
          'r3c2':{'location':[150,300,300,450],'status':None},
          'r3c3':{'location':[300,300,450,450],'status':None}
          }

class App():

    def __init__(self, squares):
        self.currentturn = 'x'
        self.squares = squares
        self.copy = copy.deepcopy(squares)
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.filemenu.add_command(label="New Game", command=self.newgame)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.window.config(menu=self.menubar)
        self.bottom_canvas = Canvas(self.window, bg="white", height=450, width=450)
        self.createBoard()
        self.bottom_canvas.pack()
        self.window.mainloop()

    def about(self):
        messagebox.showinfo("About", "Made by Jason Alencewicz!")
        return

    def newgame(self):
        self.currentturn = 'x'
        self.squares.clear()
        self.squares = copy.deepcopy(self.copy)
        self.createBoard()
        self.bottom_canvas.pack()
        
        
    def createBoard(self):
        for x in self.squares.keys():
            for y, z in self.squares[x].items():
                if y == 'location':
                    self.bottom_canvas.create_rectangle(z[0], z[1], z[2], z[3], fill='lightgray', tag=x)
                    self.bottom_canvas.tag_bind(self.bottom_canvas.itemcget(x, "tag"), '<1>', self.objectClick)
                
                
    def objectClick(self, event):
        item = self.bottom_canvas.find_closest(event.x, event.y)
        square = self.bottom_canvas.itemcget(item, "tag").replace(' current', '')
        if self.squares[square]['status'] == None:
            self.squares[square]['status'] = self.currentturn
            if self.currentturn == 'o':
                self.bottom_canvas.create_oval(self.squares[square]['location'][0]+20, self.squares[square]['location'][1]+20,  self.squares[square]['location'][2]-20,  self.squares[square]['location'][3]-20, fill='lightgray', outline = 'black', width=2, tag=square)
            elif self.currentturn == 'x':
                self.bottom_canvas.create_line(self.squares[square]['location'][0]+20, self.squares[square]['location'][1]+20, self.squares[square]['location'][2]-20, self.squares[square]['location'][3]-20, width=2)
                self.bottom_canvas.create_line(self.squares[square]['location'][0]+130, self.squares[square]['location'][1]+20, self.squares[square]['location'][2]-130, self.squares[square]['location'][3]-20, width=2)
            over = self.tic_tac_toe()
            draw = self.stalemate()
            if draw == False and over == False:
                self.switchTurn()
        else:
            return

    def switchTurn(self):
        if self.currentturn == 'x':
            self.currentturn = 'o'
        elif self.currentturn == 'o':
            self.currentturn = 'x'
        return
                                
    def stalemate(self):
        for x in self.squares.keys():
            for y, z in self.squares[x].items():
                if y == 'status':
                    if z == None:
                        return False       
        message = messagebox.askyesno("Game over!","Stalemate! Would you like to play again?")
        if message:
            self.newgame()
            return True
        else:
            self.window.destroy()
            return True
        return

    def tic_tac_toe(self):
        #rows
        if self.squares['r1c1']['status'] == 'x' and self.squares['r1c2']['status'] == 'x' and self.squares['r1c3']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r2c1']['status'] == 'x' and self.squares['r2c2']['status'] == 'x' and self.squares['r2c3']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r3c1']['status'] == 'x' and self.squares['r3c2']['status'] == 'x' and self.squares['r3c3']['status'] == 'x':
            self.gameOver('x')
            
        elif self.squares['r1c1']['status'] == 'o' and self.squares['r1c2']['status'] == 'o' and self.squares['r1c3']['status'] == 'o':
            self.gameOver('o')
        elif self.squares['r2c1']['status'] == 'o' and self.squares['r2c2']['status'] == 'o' and self.squares['r2c3']['status'] == 'o':
            self.gameOver('o')
        elif self.squares['r3c1']['status'] == 'o' and self.squares['r3c2']['status'] == 'o' and self.squares['r3c3']['status'] == 'o':
            self.gameOver('o')
        #columns
        elif self.squares['r1c1']['status'] == 'x' and self.squares['r2c1']['status'] == 'x' and self.squares['r3c1']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r1c2']['status'] == 'x' and self.squares['r2c2']['status'] == 'x' and self.squares['r3c2']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r1c3']['status'] == 'x' and self.squares['r2c3']['status'] == 'x' and self.squares['r3c3']['status'] == 'x':
            self.gameOver('x')
            
        elif self.squares['r1c1']['status'] == 'o' and self.squares['r2c1']['status'] == 'o' and self.squares['r3c1']['status'] == 'o':
            self.gameOver('o')
        elif self.squares['r1c2']['status'] == 'o' and self.squares['r2c2']['status'] == 'o' and self.squares['r3c2']['status'] == 'o':
            self.gameOver('o')
        elif self.squares['r1c3']['status'] == 'o' and self.squares['r2c3']['status'] == 'o' and self.squares['r3c3']['status'] == 'o':
            self.gameOver('o')
        #diagonal
        elif self.squares['r1c1']['status'] == 'x' and self.squares['r2c2']['status'] == 'x' and self.squares['r3c3']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r1c3']['status'] == 'x' and self.squares['r2c2']['status'] == 'x' and self.squares['r3c1']['status'] == 'x':
            self.gameOver('x')
        elif self.squares['r1c1']['status'] == 'o' and self.squares['r2c2']['status'] == 'o' and self.squares['r3c3']['status'] == 'o':
            self.gameOver('o')
        elif self.squares['r1c3']['status'] == 'o' and self.squares['r2c2']['status'] == 'o' and self.squares['r3c1']['status'] == 'o':
            self.gameOver('o')
        else:
            return False                                            
                                                                                                                                                                                              
    def gameOver(self, winner):
        newmessage = winner.capitalize()+ " wins! Would you like to play again?"
        message = messagebox.askyesno("Game over!",newmessage)
        if message:
            self.newgame()
            return
        else:
            self.window.destroy()
            return
                  
App(squares)
