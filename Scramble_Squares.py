import numpy as np

class Node:
    def __init__(self, pai = None, tabela = None):
        self.pai = pai
        self.tabela = tabela
    
class Tree:
    def __init__(self,raiz):
        self.raiz = raiz
        self.contadorIteracao = 0
        self.noEqual = None
        self.matrizObjetivo = np.array([[1,2,3],
                                        [4,5,6],
                                        [7,8,-1]
                                        ])

    def direita(self, noPai):
        no = Node(noPai)
        no.tabela = np.copy(noPai.tabela)
        indice = np.where(no.tabela == -1)

        if (indice[1] != 0):
            indiceMudar = (indice[0], indice[1]-1)
            numeroMudar = no.tabela[indiceMudar]
            no.tabela[indiceMudar] = no.tabela[indice]
            no.tabela[indice] = numeroMudar
        else:
            return None
        return no
    
    def esquerda(self, noPai):
        no = Node(noPai)
        no.tabela = np.copy(noPai.tabela)
        indice = np.where(no.tabela == -1)
    
        if (indice[1] != 2):
            indiceMudar = (indice[0], indice[1]+1)
            numeroMudar = no.tabela[indiceMudar]
            no.tabela[indiceMudar] = no.tabela[indice]
            no.tabela[indice] = numeroMudar
        else:
            return None
        return no
    
    def abaixo(self, noPai):
        no = Node(noPai)
        no.tabela = np.copy(noPai.tabela)
        indice = np.where(no.tabela == -1)

        if (indice[0] != 0):
            indiceMudar = (indice[0]-1, indice[1])
            numeroMudar = no.tabela[indiceMudar]
            no.tabela[indiceMudar] = no.tabela[indice]
            no.tabela[indice] = numeroMudar
        else:
            return None
        return no

    def acima(self, noPai):
        no = Node(noPai)
        no.tabela = np.copy(noPai.tabela)
        indice = np.where(no.tabela == -1)

        if (indice[0] != 2):
            indiceMudar = (indice[0]+1, indice[1])
            numeroMudar = no.tabela[indiceMudar]
            no.tabela[indiceMudar] = no.tabela[indice]
            no.tabela[indice] = numeroMudar
        else:
            return None
        return no
        
    def sucessores(self,pai):
        listaSucessores = list()
        
        noEsq = self.esquerda(pai)
        noAcima = self.acima(pai)
        noDir = self.direita(pai)
        noAbaixo = self.abaixo(pai)
        
        if noEsq != None:
            listaSucessores.append(noEsq)

        if noAcima != None:        
            listaSucessores.append(noAcima)
        
        if noDir != None:
            listaSucessores.append(noDir)

        if noAbaixo != None:
            listaSucessores.append(noAbaixo)

        return listaSucessores

    def objetivo(self, matriz):   
         return np.array_equal(matriz, self.matrizObjetivo)

    def baseEmLargura(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)

        while(len(listaNos) > 0):
            self.contadorIteracao += 1
            no = listaNos.pop(0)

            if(self.objetivo(no.tabela)):
                self.noEqual = no
                break
            else:
                listaAuxiliar = self.sucessores(no)
                no = None
                for node in listaAuxiliar:
                        listaNos.append(node)
    
    
if __name__ == "__main__":
    matriz = np.array([[1,2,3],
                       [4,5,6],
                       [7,-1,8]
                      ])

    no = Node(tabela=matriz)
    arv = Tree(no)
    arv.baseEmLargura()
    print(arv.contadorIteracao)
    print(arv.noEqual.tabela)

    