import numpy as np
from Node import *
#from Tree import Tree
from Priority_List import PriorityList
from Busca_BME import BME
from ScrambleSquares import Scramble_Squares

if __name__ == "__main__":
    matriz = np.array([[3,4,2],
                       [1,7,6],
                       [-1,5,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    #arv = Tree(no)
    scramble_squares = Scramble_Squares()
    busca_informacao = BME(scramble_squares)
    #Para executar, tirar o comentário do método
    #noFim = arv.buscaEmLargura()
    #noFim = arv.buscaEmProfundidade()
    #noFim = arv.buscaEmProfundidadeComLimite(100)
    #noFim = arv.buscaEmProfundidadeIterativa()
    #noFim = prioridade.buscaPorCustoUniforme(no)
    noFim = busca_informacao.busca_GME(no,"h1")

    if(noFim != None and no != None):
        print(noFim.estado)
        print('Profundidade {0}'.format(noFim.profundidade))
        print('Custo {0}'.format(noFim.custo))