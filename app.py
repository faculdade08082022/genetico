import random
from re import M
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pyplot import plot
from classes.Camera import Camera
from classes.Printer import Printer
from classes.SetCamera import SetCamera

TAM_POPULACAO = 20
TAM_INDIVIDUO = 20
X_MAX = 500
Y_MAX = 500
TAXA_MUTACAO = 0.02 # 5%

maioresFits = []

# Gera populacao inicial
def gerarPopulacao():
    populacao = []

    for i in range(0, TAM_POPULACAO):
        individuo = geraIndividuo()
        populacao.insert(i, individuo)
    
    return populacao


# Gera individuo
def geraIndividuo():
    cameras = []

    for j in range(0, TAM_INDIVIDUO):
        x = random.randrange(X_MAX)
        y = random.randrange(Y_MAX)
        angulo = random.randint(0, 360)
        c = Camera(x, y, angulo)
        cameras.insert(j, c)

    if (j == TAM_INDIVIDUO - 1):
        return SetCamera(cameras)


# Gerar nova populacao
def gerarNovaPopulacao(pai, mae):
    populacao = []

    for i in range(0, TAM_POPULACAO):
        filho = cruza(pai, mae) 
        filho = muta(filho)
        populacao.insert(i, filho)
    
    return populacao


# Seleciona pai
def selecionaPai(populacao):
    maiorFitness = 0
    selecionado = 0

    for s in populacao:
        if (s.fitness > maiorFitness):
            selecionado = s
            maiorFitness = s.fitness

    print(maiorFitness)

    maioresFits.insert(len(maioresFits), maiorFitness)

    return selecionado


# Seleciona mae
def selecionaMae(populacao):
    maiorFitness = 0
    segundoMaior = 0
    selecionado = 0

    for s in populacao:
        if (s.fitness > maiorFitness):
            selecionado = s
            maiorFitness = s.fitness
    
    for s in populacao:
        if (s.fitness > segundoMaior and s.fitness < maiorFitness):
            selecionado = s
            segundoMaior = s.fitness

    return selecionado


# Cruza pai, mae
def cruza(pai, mae):
    cameras = []

    for j in range(0, TAM_INDIVIDUO): 
        cameraPai = pai.cameras[j]
        cameraMae = mae.cameras[j]
        escolhido = random.choice([cameraPai, cameraMae])

        x = escolhido.x
        y = escolhido.y
        angulo = escolhido.a

        c = Camera(x, y, angulo)
        cameras.insert(j, c)

    if (j == TAM_INDIVIDUO - 1):
        return SetCamera(cameras)


# Muta individuo
def muta(individuo):
    cameras = []

    for j in range(0, TAM_INDIVIDUO):
        cameraIndividuo = individuo.cameras[j]

        x = random.choices([cameraIndividuo.x, random.randrange(X_MAX)], [1, TAXA_MUTACAO])[0]
        y = random.choices([cameraIndividuo.y, random.randrange(Y_MAX)], [1, TAXA_MUTACAO])[0]
        angulo = random.choices([cameraIndividuo.a, random.randint(0, 360)], [1, TAXA_MUTACAO])[0]
        c = Camera(x, y, angulo)
        cameras.insert(j, c)

    if (j == TAM_INDIVIDUO - 1):
        return SetCamera(cameras)


# Roda
def start(populacao):
    master = Tk()
    printer = Printer(master)
    printer.print(populacao, 0)

    master.title('Cameras Simulador')
    master.geometry('500x500+400+300')
    master.mainloop()

    pai = selecionaPai(populacao)
    mae = selecionaMae(populacao)
    novaPopulacao = gerarNovaPopulacao(pai, mae)

    if (len(maioresFits) < 50):
        start(novaPopulacao)
    else:
        plt.plot(maioresFits)
        plt.show()


if __name__ == '__main__':
    populacao = gerarPopulacao()

    start(populacao)