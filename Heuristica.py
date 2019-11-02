from Scramble_Squares import Scramble_Squares

class Heuristica:
    def __init__(self):
        self.squares = Scramble_Squares()
        self.elementosFora = list()
        
    def h1(self,no): #h1 será a busca por quantidade de elementos fora da posição
        qtde_fora = 0
        for linha in range(3):
            for coluna in range(3):
                if no.estado[linha][coluna] != self.squares.matrizObjetivo[linha][coluna]:
                    qtde_fora += 1
                    self.elementosFora.append(no.estado[linha][coluna])
        return qtde_fora


    def h2(self,no): #h2 será a distancia dos elementos até sua posição objetivo
        pass