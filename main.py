import numpy as np
from Node import *
from Tree import Tree
from Priority_List import PriorityList
from Busca_BME import BME
from ScrambleSquares import Scramble_Squares

if __name__ == "__main__":
    matriz = np.array([[3,4,2],
                       [1,7,6],
                       [-1,5,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    arv = Tree(no)
    scramble_squares = Scramble_Squares()
    prioridade = PriorityList(scramble_squares)
    busca_informacao = BME(scramble_squares, prioridade)

    noFim = busca_informacao.busca_A(no,"h2")

    if(noFim != None and no != None):
        print(noFim.estado)
        print('Profundidade {0}'.format(noFim.profundidade))
        print('Custo {0}'.format(noFim.custo))
        print("Quantidade de nos {0}".format(busca_informacao.priority_list.total_elementos))