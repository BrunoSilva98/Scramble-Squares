from Scramble_Squares import Scramble_Squares
from Heuristica import Heuristica
from Priority_List import PriorityList

class BME():
    def __init__(self):
        self.squares = Scramble_Squares()
        self.heuristica = Heuristica()
        self.priority_list = PriorityList()
        
    def busca_GME(self, raiz, funcao_h, limite=22):
        self.priority_list.addElementListaPrioridade(raiz)
        
        while(self.priority_list.qtdeElementos>0):
            no = self.priority_list.getElementListaPrioridade()
            if(self.squares.objetivo(no.estado)):
                return no
            elif(no.profundidade<limite):
                self.squares.sucessores(no, "info", funcao_h)


