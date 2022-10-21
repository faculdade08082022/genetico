import math
from tkinter import *


class Printer:
    def __init__(self, master=None):
        self.master = master
        self.canvas = Canvas(self.master)

    def print(self, populacao, p):
        #print(populacao)
        #print(p)

        self.canvas.delete("all")

        for c in populacao[p].cameras:
            # ponto fixo
            x = c.x  # random.randint(0, 400)
            y = c.y  # random.randint(0, 400)
            a = c.a * math.pi / 180  # random.randint(0, 360)
            #print(x, y)

            x2 = x - 50
            y2 = 100 + y
            # origem
            x2 -= x
            y2 -= y
            # rotacionar
            x2_ = x2 * math.cos(a) - y2 * math.sin(a)
            y2_ = x2 * math.sin(a) + y2 * math.cos(a)
            # volta a posicao
            x2 = x2_ + x
            y2 = y2_ + y

            x3 = 50 + x
            y3 = 100 + y

            # origem
            x3 -= x
            y3 -= y
            # rotacionar
            x3_ = x3 * math.cos(a) - y3 * math.sin(a)
            y3_ = x3 * math.sin(a) + y3 * math.cos(a)
            # volta a posicao
            x3 = x3_ + x
            y3 = y3_ + y

            points = [x, y, x2, y2, x3, y3]
            self.polygon = self.canvas.create_polygon(
                points, outline="orange", fill="yellow", width=2)
            self.canvas.create_rectangle(
                x, y, x+2, y+2, outline="black", fill="black")
            self.canvas.pack(fill=BOTH, expand=1)

        value = self.getQuantidadeCor(self.canvas)

        # atribuindo o fitness
        populacao[p].fitness = value

        if (p < len(populacao) - 1):
            self.canvas.after(1, lambda: self.print(populacao, p + 1))
        else:
            self.master.destroy()

    def getQuantidadeCor(self, canvas):
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])
        value = 0

        for x in range(width):
            for y in range(height):
                value = value + self.get_pixel_color(canvas, x, y)

        return value

    def get_pixel_color(self, canvas, x, y):
        ids = canvas.find_overlapping(x, y, x, y)

        if len(ids) > 0:
            index = ids[-1]
            color = canvas.itemcget(index, "fill")
            color = color.upper()

            if color == 'YELLOW':
                return 1

        return 0
