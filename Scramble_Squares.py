import numpy as np
from Node import Node
class Tree:
    def __init__(self,raiz):
        self.raiz = raiz
        self.profundidade = 0
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
        
    def sucessores(self, pai):
        listaSucessores = list()
        listaNos = list()

        listaNos.append(self.esquerda(pai))
        listaNos.append(self.acima(pai))
        listaNos.append(self.direita(pai))
        listaNos.append(self.abaixo(pai))

        for no in listaNos:
            if no != None:
                no.profundidade = pai.profundidade + 1
                no.custo = pai.custo + 1
                listaSucessores.append(no)
        
        return listaSucessores

    def objetivo(self, matriz):   
         return np.array_equal(matriz, self.matrizObjetivo)

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

    def ordListaPrioridade(self):
        self.listaPrioridade = sorted(self.listaPrioridade)

    def addElementListaPrioridade(self, no):
        for custo in range(len(self.listaPrioridade)):
            if(no.custo == self.listaPrioridade[custo][0]):
                self.listaPrioridade[custo].append(no)        
                return None

        self.listaPrioridade.append([no.custo])
        self.listaPrioridade[len(self.listaPrioridade)-1].append(no)
        self.ordListaPrioridade()
        return None

    def getElementListaPrioridade(self):
        for custo in range(len(self.listaPrioridade)):
            if(len(self.listaPrioridade[custo]) > 1):
                self.qtdeElementos -= 1
                return self.listaPrioridade[custo].pop(1)
    
    def addListListaPrioridade(self, lista):
        for elemento in lista:
            self.addElementListaPrioridade(elemento)
            self.qtdeElementos += 1

    def buscaMenorCusto(self):
        self.addElementListaPrioridade(self.raiz)
        self.qtdeElementos += 1

        while(self.qtdeElementos > 0):
                no = self.getElementListaPrioridade()
                
                if (self.objetivo(no.estado)):
                    self.listaPrioridade = self.listaPrioridade.clear()
                    return no
                else:
                    self.addListListaPrioridade(self.sucessores(no))

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