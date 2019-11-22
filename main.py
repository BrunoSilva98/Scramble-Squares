import numpy as np
from Node import *
from Tree import Tree
from Priority_List import PriorityList
from Busca_BME import BME
from ScrambleSquares import Scramble_Squares
from Fator_Ramificacao import fator_ramificacao_efetivo

if __name__ == "__main__":
    matriz = np.array([[4,1,2],
                       [5,3,6],
                       [7,8,-1]
                      ])

    no = Node(estado=matriz, profundidade=0)
    arv = Tree(no)
    scramble_squares = Scramble_Squares()
    prioridade = PriorityList(scramble_squares)
    busca_informacao = BME(scramble_squares, prioridade)
    noFim = busca_informacao.busca_GME(no,"h2")
    qtde_total_nos = busca_informacao.priority_list.total_elementos
    fator_ramificacao = fator_ramificacao_efetivo(qtde_total_nos, noFim.profundidade)

    if(noFim != None and no != None):
        print(noFim.estado)
        print('Profundidade {0}'.format(noFim.profundidade))
        print('Custo {0}'.format(noFim.custo))
        print("Quantidade de nos {0}".format(qtde_total_nos))
        print("Fator de Ramificacao Efetivo {0}".format(fator_ramificacao))