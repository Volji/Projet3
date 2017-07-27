from tkinter import *


class Constantes:
    def __init__(self):
        # Images des objets
        self.obj1 = PhotoImage(file="data/obj1.gif")
        self.obj2 = PhotoImage(file="data/obj2.gif")
        self.obj3 = PhotoImage(file="data/obj3.gif")
        # Image du sol
        self.floor = PhotoImage(file="data/sol.gif")
        # Image du mur
        self.wall = PhotoImage(file="data/mur.gif")
        # Image du gardien
        self.gard = PhotoImage(file="data/gardien.gif")
        # Images du player
        self.mcgyver1 = PhotoImage(file="data/mcgyver.gif")
        self.mcgyver2 = PhotoImage(file="data/death.gif")
        # Image du début du jeu
        self.photo1 = PhotoImage(file='data/init.gif')
        # variables
        self.play = False
        self.end_game = True
        # Dimension image
        self.SIZE = 25
        # Nombre de ligne
        self.LIGNS = 15
        # Nombre de colone
        self.COLUMNS = 15
        # Création du tableau
        self.board = [[0]*self.COLUMNS for i in range(self.LIGNS)]
