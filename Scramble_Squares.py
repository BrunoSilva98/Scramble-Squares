import numpy as np

class Node:
    def __init__(self, pai=None, estado=None, profundidade=None):
        self.pai = pai
        self.estado = estado
        self.acao = None
        self.custo = None
        self.profundidade = profundidade
        
class Tree:
    def __init__(self,raiz):
        self.raiz = raiz
        self.profundidade = 0
        self.noEqual = None
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
        
    def sucessores(self, pai, custo):
        listaSucessores = list()
        
        noEsq = self.esquerda(pai)
        noAcima = self.acima(pai)
        noDir = self.direita(pai)
        noAbaixo = self.abaixo(pai)
        
        if noEsq != None:
            noEsq.profundidade = self.profundidade
            noEsq.custo = custo
            listaSucessores.append(noEsq)

        if noAcima != None:        
            noAcima.profundidade = self.profundidade
            noAcima.custo = custo
            listaSucessores.append(noAcima)
        
        if noDir != None:
            noDir.profundidade = self.profundidade
            noDir.custo = custo
            listaSucessores.append(noDir)

        if noAbaixo != None:
            noAbaixo.profundidade = self.profundidade
            noAbaixo.custo = custo
            listaSucessores.append(noAbaixo)
        
        return listaSucessores

    def objetivo(self, matriz):   
         return np.array_equal(matriz, self.matrizObjetivo)

    def baseEmLargura(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0
        custo = 0
        
        while(len(listaNos) > 0):
            no = listaNos.pop(0)

            if(self.objetivo(no.estado)):
                return no
            else:
                self.profundidade += 1
                custo += 1
                listaAuxiliar = self.sucessores(no, custo)
            
                for node in listaAuxiliar:
                    listaNos.append(node)
    
    def baseEmProfundidade(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0
        custo = 0

        while(len(listaNos) > 0):
            no = listaNos.pop(len(listaNos)-1)

            if(self.objetivo(no.estado)):
                return no
            else:
                self.profundidade += 1
                custo += 1
                listaAuxiliar = self.sucessores(no, custo)
            
                for node in listaAuxiliar:
                    listaNos.append(node)

    def baseEmProfundidadeComLimite(self, limite):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0
        custo = 0
        contadorIteracoes = 0

        while((len(listaNos) > 0) and (contadorIteracoes < limite)):
            no = listaNos.pop(len(listaNos)-1)

            if(self.objetivo(no.estado)):
                return no
            else:
                self.profundidade += 1
                contadorIteracoes += 1
                custo += 1
                listaAuxiliar = self.sucessores(no, custo)
            
                for node in listaAuxiliar:
                    listaNos.append(node)
        
        return None

if __name__ == "__main__":
    matriz = np.array([[1,2,3],
                       [4,5,6],
                       [7,-1,8]
                      ])

    no = Node(estado=matriz, profundidade=0)
    no.custo = 0
    arv = Tree(no)
    noFim = arv.baseEmProfundidadeComLimite(100)
    if(noFim != None):
        print(noFim.estado)
        print(noFim.profundidade)
        print(noFim.custo)
    
    

    