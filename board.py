from tkinter import *
from constantes import *


class Board:
    def __init__(self, canvas):
        self.canvas = canvas
        self.var = Constantes()

        self.floor = self.var.floor
        self.wall = self.var.wall
        self.gard = self.var.gard

    def init_board(self, level):
        # Display floor, wall and guardian
        e = 3
        for y in range(self.var.LIGNS):
            for x in range(self.var.COLUMNS):
                if level[y][x] == 1:
                    img = self.canvas.create_image(x*self.var.SIZE+e,
                                                   y*self.var.SIZE+e,
                                                   anchor=NW,
                                                   image=self.wall)

                if level[y][x] == 0:
                    img = self.canvas.create_image(x*self.var.SIZE+e,
                                                   y*self.var.SIZE+e,
                                                   anchor=NW,
                                                   image=self.floor)
                    self.canvas.tag_lower(img)

                if level[y][x] == 6:
                    self.guardian = self.canvas.create_image(x*self.var.SIZE+e,
                                                             y*self.var.SIZE+e,
                                                             anchor=NW,
                                                             image=self.gard)
                    self.canvas.tag_lower(self.guardian)
