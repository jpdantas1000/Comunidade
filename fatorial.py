def fatorial(n: int) -> int:
    '''
    Retorna o fatorial de um número n.

    Parâmetros:
    n (int): Um número inteiro não negativo.

    Retorna:
    int: O fatorial de n.
    '''
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)



numero: int = int(input("Informe um numero inteiro: \n"))
resultado: int = fatorial(numero)
print(resultado)
