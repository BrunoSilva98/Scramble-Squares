import numpy as np
from Node import *
#from Tree import Tree
from Priority_List import PriorityList
from Busca_BME import BME
from ScrambleSquares import Scramble_Squares

if __name__ == "__main__":
    matriz = np.array([[-1,1,2],
                       [4,5,3],
                       [7,8,6]
                      ])

    no = Node(estado=matriz, profundidade=0)
    #arv = Tree(no)
    scramble_squares = Scramble_Squares()
    prioridade = PriorityList(scramble_squares)
    busca_informacao = BME(scramble_squares, prioridade)
    #Para executar, tirar o comentário do método
    #noFim = arv.buscaEmLargura()
    #noFim = arv.buscaEmProfundidade()
    #noFim = arv.buscaEmProfundidadeComLimite(100)
    #noFim = arv.buscaEmProfundidadeIterativa()
    #noFim = prioridade.buscaPorCustoUniforme(no)
    noFim = busca_informacao.busca_A(no,"h2")

    if(noFim != None and no != None):
        print(noFim.estado)
        print('Profundidade {0}'.format(noFim.profundidade))
        print('Custo {0}'.format(noFim.custo))
        print("Quantidade de nos {0}".format(busca_informacao.priority_list.total_elementos))