import numpy as np
from Node import Node
class Tree:
    def __init__(self,raiz):
        self.raiz = raiz
        self.profundidade = 0

    def buscaEmLargura(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0
        
        while(len(listaNos) > 0):
            self.profundidade = listaNos[len(listaNos)-1].profundidade
            no = listaNos.pop(0)
            if(self.objetivo(no.estado)):
                return no
            else:
                listaAuxiliar = self.sucessores(no)
            
                for node in listaAuxiliar:
                    listaNos.append(node)
    
    def buscaEmProfundidade(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0

        while(len(listaNos) > 0):
            no = listaNos.pop(len(listaNos)-1)
            self.profundidade = no.profundidade
            if(self.objetivo(no.estado)):
                return no
            else:
                listaAuxiliar = self.sucessores(no)
                for node in listaAuxiliar:
                    listaNos.append(node)

    def buscaEmProfundidadeComLimite(self, limite):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)

        while(len(listaNos) > 0):
            no = listaNos.pop(len(listaNos)-1)
            self.profundidade = no.profundidade
            if(self.objetivo(no.estado)):
                return no
            elif (no.profundidade < limite):
                listaAuxiliar = self.sucessores(no)
                for node in listaAuxiliar:
                    listaNos.append(node)
        return None

    def buscaEmProfundidadeIterativa(self):
        limite = 0
        while(True):
            no = self.buscaEmProfundidadeComLimite(limite)         
            if no != None:
                return no            
            limite += 1



    def getElementListaPrioridade(self):
        for custo in range(len(self.listaPrioridade)):
            if(len(self.listaPrioridade[custo]) > 1):
                self.qtdeElementos -= 1
                return self.listaPrioridade[custo].pop(1)
    

if __name__ == "__main__":
    matriz = np.array([[1,2,3],
                       [4,5,6],
                       [7,-1,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    arv = Tree(no)
    noFim = arv.buscaMenorCusto()
    if(noFim != None):
        print(noFim.estado)
        print(noFim.profundidade)
        print(noFim.custo)