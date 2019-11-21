from Scramble_Squares import Scramble_Squares
from Heuristica import Heuristica
from Priority_List import PriorityList

class BME():
    def __init__(self):
        self.squares = Scramble_Squares()
        self.heuristica = Heuristica()
        self.priority_list = PriorityList()
        
    def busca_GME(self, raiz):
        
