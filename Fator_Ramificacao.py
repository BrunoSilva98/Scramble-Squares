#b - Fator de ramificacao
#d - Profundidade na qual a solução foi encontrada

def calc_n(b, d):
    n = 0
    for profundidade in range(d+1):
        n += b**profundidade
    return n

def fator_ramificacao_efetivo(total_nos, d):
    minimo = 0
    maximo = 5
    erro = 0.0001
    n = 0
    b = 0
    
    while(abs(n-total_nos) > erro):
        b = (minimo + maximo)/2
        n = calc_n(b,d)
        if(n>total_nos):
            maximo = b
        else:
            minimo = b

    return b