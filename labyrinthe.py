from tkinter import *
from random import randrange
from items import *
from board import *
from player import *
from constantes import *
import os
from tkinter.font import Font


#----------------------------------------------------------------------

def onKeyPress(event):
	global play
	global level
	
	key = event.keysym
	
	if play:
		# Up
		if key == "Up":
			p.movePlayer(0, -1, level)
		# Down                  
		if key == "Down":
			p.movePlayer(0, 1, level)
	
		# Right               
		if key == "Right":
			p.movePlayer(1, 0, level)
	
		# Left
		if key == "Left":
			p.movePlayer(-1, 0, level)

		#change label number of items
		number = p.statusItems()
		new_text = "Number of item: " + str(number)
		labelItems.config(text=new_text)


		# End of game?
		end_game, game_state = p.statusGame()
		if end_game:
			play = False
			if game_state == 0:
				font = Font(family='Helvetica', size=56, weight='bold')
				canvas_text = canvas.create_text(200,200,text="PERDU!",fill="red", font=font, justify="left")

			else:
				font = Font(family='Helvetica', size=56, weight='bold')
				canvas_text = canvas.create_text(200,200,text="GAGNE!",fill="green", font=font, justify="left")

		

def newGame():
	global level
	global play, end_game
	
	# Initialize level
	level = var.board
		
	# Load file level
	file_name = "data/level0.txt"
	if (os.path.exists(file_name)):
		files = open(file_name, "r")

		# Create level
		lignes = files.readlines()
		files.close()	
		
		for l in range(var.LIGNS):
			ligne = lignes[l].rstrip()
			for c in range(var.COLUMNS):
				level[l][c] = int(ligne[c])
		
		p.setToZero()
		
		# Delete Canvas
		canvas.delete(ALL)
		
		# Choice and display objects
		level[0][1] = 5
		o.displayItems(level)
		level[0][1] = 0
		
		# Display Board
		b.initBoard(level)
		
		# Display player
		p.affichePlayer()
		
		# Active keys
		play = True
		end_game = False
			
	else:
		play = False
		canvas.delete(ALL)
		font = Font(family='Helvetica', size=56, weight='bold')
		canvas_text = self.canvas.create_text(200,100,text="ERREUR!",fill="red", font=font, justify="left")

#----------------------------------------------------------------------
	
# Create Tk modules
root = Tk()
root.title("Mac Gyver")

var = Constantes()

button = Button(root, text="Play", command=newGame)
#button.pack(side=TOP, padx=5, pady=5)
button.grid(row=0, column=0)

labelItems = Label(root, text="Number of item: 0", anchor=W, justify=LEFT)
#labelItems.pack(side=TOP, padx=5, pady=5)
labelItems.grid(row=0, column=1)

canvas = Canvas(root, width=var.COLUMNS*var.SIZE, height=var.LIGNS*var.SIZE, bg='black')
#canvas.pack(side=BOTTOM, padx=0, pady=0)
canvas.grid(row=1, columnspan=2)
canvas.focus_set()
canvas.bind("<Key>", onKeyPress)

o = Items(canvas)
b = Board(canvas)
p = Player(canvas)

play = var.play
end_game = var.end_game
level = var.board


canvas.create_image(0, 50, anchor=NW, image=var.photo1)

root.mainloop()
