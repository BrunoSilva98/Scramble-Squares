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

    #Para executar, tirar o comentário do método
    noFim = arv.buscaEmLargura()
    noFim = arv.buscaEmProfundidade()
    noFim = arv.buscaEmProfundidadeComLimite(100)
    noFim = arv.buscaEmProfundidadeIterativa()
    noFim = Prioridade.buscaPorCustoUniforme(no)

    if(noFim != None and no != None):
        print(noFim.estado)
        print('Profundidade {0}'.format(noFim.profundidade))
        print('Custo {0}'.format(noFim.custo))