from tkinter import *
from random import randrange
from items import *
from constantes import *

class Player:
	def __init__(self, canvas):
		self.canvas = canvas
		
		self.var = Constantes()
		
		self.mcgyver = []
		self.mcgyver.append(self.var.mcgyver1)
		self.mcgyver.append(self.var.mcgyver2)
		self.mcgyver.append(self.var.floor)
		
		self.px = 1
		self.py = 0
		self.nbObj = 0
		
		self.end_game = False
		self.game_state = 0
		
		self.o = Items(self.canvas)
		
	def setToZero(self):
		self.px = 1
		self.py = 0
		self.nbObj = 0
		self.end_game = False
		self.game_state = 0
		
	def statusGame(self):
		return self.end_game,self.game_state

	def statusItems(self):
		return self.nbObj

	def affichePlayer(self):
		e = 3
		self.player = self.canvas.create_image(self.px*self.var.SIZE+e,self.py*self.var.SIZE+e,anchor=NW,image = self.mcgyver[0])
		self.canvas.tag_raise(self.player)
		
		
	def movePlayer(self, xi, yi, level):
		x = self.px + xi
		y = self.py + yi
		
		# Floor
		if level[y][x] == 0:
			self.px = x
			self.py = y
			
		# Items
		if level[y][x] >= 7 and level[y][x] <= 9:
			self.px = x
			self.py = y
			level[y][x] = 0
			self.nbObj += 1	
		# Guardian
		if level[y][x] == 6:
			self.end_game = True
			if self.nbObj == 3:
				self.px = x
				self.py = y
				self.game_state = 1
			else:
				self.canvas.itemconfigure(self.player,image=self.mcgyver[1])
				self.game_state = 0	

		e = 3	
		img = self.canvas.create_image(self.px*self.var.SIZE+e,self.py*self.var.SIZE+e,anchor=NW,image = self.mcgyver[2])
		self.canvas.coords(self.player, self.px*self.var.SIZE+e, self.py*self.var.SIZE+e)
		self.canvas.tag_raise(self.player)
		
		
		
		


		
