class PriorityList():
    def __init__(self):
        self.listaPrioridade = list()
        self.qtdeElementos = 0
        
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

    def addListListaPrioridade(self, lista):
        for elemento in lista:
            self.addElementListaPrioridade(elemento)
            self.qtdeElementos += 1


    def buscaPorCusto(self):
        self.addElementListaPrioridade(self.raiz)
        self.qtdeElementos += 1

        while(self.qtdeElementos > 0):
                no = self.getElementListaPrioridade()
                
                if (self.objetivo(no.estado)):
                    self.listaPrioridade = self.listaPrioridade.clear()
                    return no
                else:
                    self.addListListaPrioridade(self.sucessores(no))        