from tkinter import *

class Constantes:
	def __init__(self):
		# Images of objects
		self.obj1 = PhotoImage(file = "data/obj1.gif")
		self.obj2 = PhotoImage(file = "data/obj2.gif")
		self.obj3 = PhotoImage(file = "data/obj3.gif")
		# Image of the floor
		self.floor = PhotoImage(file="data/sol.gif") 
		# Image of walls
		self.wall = PhotoImage(file="data/mur.gif")
		# Image of the keeper
		self.gard = PhotoImage(file="data/gardien.gif")
		# Image of McGyver (player)
		self.mcgyver1 = PhotoImage(file = "data/mcgyver.gif")
		self.mcgyver2 = PhotoImage(file = "data/death.gif")
		# Image of the beggining
		self.photo1 = PhotoImage(file ='data/init.gif')
		# variables
		self.play = False
		self.end_game = True
		# image size
		self.SIZE = 25
		# Number of lines
		self.LIGNS = 15
		# Number of columns
		self.COLUMNS = 15
		# table creation
		self.board = [[0]*self.COLUMNS for i in range(self.LIGNS)]
		
		