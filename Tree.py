from ScrambleSquares import Scramble_Squares

class Tree:
    def __init__(self,raiz):
        self.raiz = raiz
        self.profundidade = 0
        self.squares = Scramble_Squares()

    def buscaEmLargura(self):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)
        self.profundidade = 0
        
        while(len(listaNos) > 0):
            self.profundidade = listaNos[len(listaNos)-1].profundidade
            no = listaNos.pop(0)
            if(self.squares.objetivo(no.estado)):
                return no
            else:
                listaAuxiliar = self.squares.sucessores(no)
            
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
            if(self.squares.objetivo(no.estado)):
                return no
            else:
                listaAuxiliar = self.squares.sucessores(no)
                for node in listaAuxiliar:
                    listaNos.append(node)

    def buscaEmProfundidadeComLimite(self, limite):
        listaNos = list()
        listaAuxiliar = list()
        listaNos.append(self.raiz)

        while(len(listaNos) > 0):
            no = listaNos.pop(len(listaNos)-1)
            self.profundidade = no.profundidade
            if(self.squares.objetivo(no.estado)):
                return no
            elif (no.profundidade < limite):
                listaAuxiliar = self.squares.sucessores(no)
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