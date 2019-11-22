#b - Fator de ramificacao
#d - Profundidade na qual a solução foi encontrada

def calc_n(b, d):
    contador = 1
    n = 0
    while(contador <= d):
        n += b**contador
        contador += 1
    n += 1
    return n

def fator_ramificacao_efetivo(total_nos, d):
    minimo = 1.25
    maximo = 2.5
    erro = 0.0001
    n = 0
    
    while(abs(n-total_nos) > erro):
        b = (minimo + maximo)/2
        n = calc_n(b,d)
        if(n>total_nos):
            maximo = b
        else:
            minimo = b

    return b