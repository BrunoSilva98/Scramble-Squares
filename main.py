import numpy as np
from Node import *
from Tree import Tree
from Priority_List import PriorityList
from Busca_BME import BME

if __name__ == "__main__":
    matriz = np.array([[1,2,3],
                       [4,5,6],
                       [7,-1,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    arv = Tree(no)
    prioridade = PriorityList()
    busca_informacao = BME()
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