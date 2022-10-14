import random
from tkinter import *
from classes.Camera import Camera
from classes.Printer import Printer
from classes.SetCamera import SetCamera

TAM_POPULACAO = 3
TAM_INDIVIDUO = 3
X_MAX = 500
Y_MAX = 500

# gerar população inicia com idividuos que contém 10 cameras
populacao = []

for i in range(0, TAM_POPULACAO):
    populacao.insert(i, [])
    cameras = []

    for j in range(0, TAM_INDIVIDUO):
        x = random.randrange(X_MAX)
        y = random.randrange(Y_MAX)
        angulo = random.randint(0, 360)
        c = Camera(x, y, angulo)
        cameras.insert(j, c)

        if (j == TAM_INDIVIDUO - 1):
            populacao[i] = SetCamera(cameras)

# seleciona individuos com mais pontos em amerelo
def selecionaIndividuos(populacao):
    selecionados = []

    for s in populacao:
        if (s.fitness > 5000):
            selecionados.insert(0, s)

    return selecionados

# Faz cruzamento de populacao
def cruzamento(populacao):
    cruzados = []

    return cruzados

# Gera mutacao em populacao
def mutacao(populacao):
    mutados = []
    
    return mutados

if __name__ == "__main__":
    master = Tk()
    printer = Printer(master)

    printer.print(populacao, 0)

    master.title("Cameras Simulador")
    master.geometry('500x500+400+300')
    master.mainloop()

    selecionados = selecionaIndividuos(populacao)
    cruzados = cruzamento(selecionados)
    mutados = mutacao(cruzados)