from Heuristica import Heuristica
from Priority_List import PriorityList

class BME():
    def __init__(self, squares):
        self.squares = squares
        self.heuristica = Heuristica(squares)
        self.priority_list = PriorityList(self.squares)
        
    def busca_GME(self, raiz, funcao_h, limite=22):
        self.priority_list.addElementListaPrioridade(raiz)
        
        while(self.priority_list.qtdeElementos > 0):
            no = self.priority_list.getElementListaPrioridade()
            if(self.squares.objetivo(no.estado)):
                self.priority_list.listaPrioridade.clear()
                return no
            elif(no.profundidade<limite):
                self.priority_list.addListListaPrioridade(self.squares.sucessores(no, "GME", funcao_h))
        return None

    def busca_A(self, raiz, funcao_h):
        self.priority_list.addElementListaPrioridade(raiz)

        while(self.priority_list.qtdeElementos > 0):
            no = self.priority_list.getElementListaPrioridade()
            if(self.squares.objetivo(no.estado)):
                self.priority_list.listaPrioridade.clear()
                return no
            else:
                self.priority_list.addListListaPrioridade(self.squares.sucessores(no, "A*", funcao_h))
        return None