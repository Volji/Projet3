from tkinter import *
from random import randrange
from constantes import *


class Items:
    def __init__(self, canvas):
        self.canvas = canvas
        self.var = Constantes()

        self.obj = []
        self.obj.append(self.var.obj1)
        self.obj.append(self.var.obj2)
        self.obj.append(self.var.obj3)
        self.floor = self.var.floor

    def display_items(self, level):
        # Choice and display objects
        tow = 0
        e = 3
        while tow < 3:
            x, y = self.recursiv(level)
            level[y][x] = tow + 7
            img = self.canvas.create_image(x*self.var.SIZE+e,
                                           y*self.var.SIZE+e,
                                           anchor=NW,
                                           image=self.obj[tow])
            self.canvas.tag_lower(img)
            img = self.canvas.create_image(x*self.var.SIZE+e,
                                           y*self.var.SIZE+e,
                                           anchor=NW,
                                           image=self.floor)
            self.canvas.tag_lower(img)
            tow += 1

    def delete_objet(self, x, y, num):
        self.canvas.itemconfigure(self.obj[num], image=self.obj[3])
        self.canvas.tag_lower(self.obj[num])

    def recursiv(self, level):
        x = randrange(self.var.COLUMNS)
        y = randrange(self.var.LIGNS)
        if (level[y][x] == 0):
            return x, y
        else:
            return self.recursiv(level)

