import numpy as np
from Node import *
from Heuristica import Heuristica

class Scramble_Squares:
    def __init__(self):
        self.heuristica = Heuristica(self)
        self.matrizObjetivo = np.array([[1,2,3],
                                        [4,5,6],
                                        [7,8,-1]
                                       ])

    def direita(self, noPai):
        no = Node(noPai)
        no.acao = 'Direita'
        no.estado = np.copy(noPai.estado)
        indice = np.where(no.estado == -1)

        if (indice[1] != 0):
            indiceMudar = (indice[0], indice[1]-1)
            numeroMudar = no.estado[indiceMudar]
            no.estado[indiceMudar] = no.estado[indice]
            no.estado[indice] = numeroMudar
        else:
            return None
        return no
    
    def esquerda(self, noPai):
        no = Node(noPai)
        no.acao = 'Esquerda'
        no.estado = np.copy(noPai.estado)
        indice = np.where(no.estado == -1)
    
        if (indice[1] != 2):
            indiceMudar = (indice[0], indice[1]+1)
            numeroMudar = no.estado[indiceMudar]
            no.estado[indiceMudar] = no.estado[indice]
            no.estado[indice] = numeroMudar
        else:
            return None
        return no
    
    def abaixo(self, noPai):
        no = Node(noPai)
        no.acao = 'Abaixo'
        no.estado = np.copy(noPai.estado)
        indice = np.where(no.estado == -1)

        if (indice[0] != 0):
            indiceMudar = (indice[0]-1, indice[1])
            numeroMudar = no.estado[indiceMudar]
            no.estado[indiceMudar] = no.estado[indice]
            no.estado[indice] = numeroMudar
        else:
            return None
        return no

    def acima(self, noPai):
        no = Node(noPai)
        no.acao = 'Acima'
        no.estado = np.copy(noPai.estado)
        indice = np.where(no.estado == -1)

        if (indice[0] != 2):
            indiceMudar = (indice[0]+1, indice[1])
            numeroMudar = no.estado[indiceMudar]
            no.estado[indiceMudar] = no.estado[indice]
            no.estado[indice] = numeroMudar
        else:
            return None
        return no

    def sucessores(self, pai, origem="no_info", func_h=None):
        listaSucessores = list()
        listaNos = list()

        listaNos.append(self.esquerda(pai))
        listaNos.append(self.acima(pai))
        listaNos.append(self.direita(pai))
        listaNos.append(self.abaixo(pai))

        for no in listaNos:
            if no != None:
                no.profundidade = pai.profundidade + 1
                if origem == "GME":
                    if func_h == "h1":
                        no.custo = self.heuristica.h1(no)
                    elif func_h == "h2":
                        no.custo = self.heuristica.h2(no)
                elif origem == "A*":
                    if func_h == "h1":
                        no.custo = no.profundidade + self.heuristica.h1(no)
                    elif func_h == "h2":
                        no.custo = no.profundidade + self.heuristica.h2(no)
                else:
                    no.custo = pai.custo + 1
                listaSucessores.append(no)
        
        return listaSucessores

    def objetivo(self, matriz):   
         return np.array_equal(matriz, self.matrizObjetivo)