import numpy as np
import matplotlib.pyplot as plt
from leitorarquivo import LeitorArquivo


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    i = 1
    for serie in valores:
       plt.plot(serie)
       i += 1
    plt.legend(loc='upper left')
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.title('Gráfico de linhas')
    plt.show()

main()  