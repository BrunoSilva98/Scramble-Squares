class Node:
    def __init__(self, pai=None, estado=None, profundidade=None):
        self.pai = pai
        self.estado = estado
        self.acao = None
        self.custo = 0
        self.profundidade = profundidade