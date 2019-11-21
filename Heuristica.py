import numpy as np

class Heuristica:
    def __init__(self, squares):
        self.squares = squares
        self.elementosFora = []
        
    def h1(self,no): #h1 será a busca por quantidade de elementos fora da posição
        qtde_fora = 0
        self.elementosFora.clear()
        for linha in range(3):
            for coluna in range(3):
                if no.estado[linha][coluna] != self.squares.matrizObjetivo[linha][coluna]:
                    qtde_fora += 1
                    self.elementosFora.append(no.estado[linha][coluna])
        return qtde_fora


    def h2(self,no): #h2 será a distancia dos elementos até sua posição objetivo
        self.h1(no)
        distancia_obj = 0

        for elemento in self.elementosFora:
            indice_obj = np.where(self.squares.matrizObjetivo == elemento)
            indice_fora = np.where(no.estado == elemento)

            distancia_obj += abs(indice_obj[0]-indice_fora[0]) + abs(indice_obj[1] - indice_fora[1]) 

        return distancia_obj