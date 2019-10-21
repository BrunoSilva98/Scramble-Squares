import numpy as np
from Node import *
from Tree import Tree
from Priority_List import PriorityList

if __name__ == "__main__":
    matriz = np.array([[1,2,3],
                       [4,5,6],
                       [7,-1,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    arv = Tree(no)
    Prioridade = PriorityList()

    noFim = arv.buscaEmLargura()
    no = Prioridade.buscaPorCustoUniforme(no)

    if(noFim != None and no != None):
        print(noFim.estado)
        print(noFim.profundidade)
        print(noFim.custo)
        print(no.estado)
        print(no.profundidade)
        print(no.custo)