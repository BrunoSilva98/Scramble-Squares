

class PriorityList:
    def __init__(self, squares):
        self.listaPrioridade = list()
        self.qtdeElementos = 0
        self.squares = squares
        self.total_elementos = 0
        
    def ordListaPrioridade(self):
        self.listaPrioridade = sorted(self.listaPrioridade)

    def addElementListaPrioridade(self, no):
        for custo in range(len(self.listaPrioridade)):
            if(no.custo == self.listaPrioridade[custo][0]):
                self.listaPrioridade[custo].append(no)
                self.qtdeElementos += 1
                self.total_elementos += 1
                return None

        self.listaPrioridade.append([no.custo])
        self.listaPrioridade[len(self.listaPrioridade)-1].append(no)
        self.qtdeElementos += 1
        self.total_elementos += 1
        return None

    def addListListaPrioridade(self, lista):
        for elemento in lista:
            self.addElementListaPrioridade(elemento)
        self.ordListaPrioridade()

    def getElementListaPrioridade(self):
        for custo in range(len(self.listaPrioridade)):
            if(len(self.listaPrioridade[custo]) > 1):
                self.qtdeElementos -= 1
                return self.listaPrioridade[custo].pop(1)

    def buscaPorCustoUniforme(self, raiz):
        self.addElementListaPrioridade(raiz)

        while(self.qtdeElementos > 0):
                no = self.getElementListaPrioridade()
                
                if (self.squares.objetivo(no.estado)):
                    self.listaPrioridade.clear()
                    return no
                else:
                    self.addListListaPrioridade(self.squares.sucessores(no))        