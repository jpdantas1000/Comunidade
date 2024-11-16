def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)



numero: int = int(input("Informe um numero inteiro: \n"))
resultado: int = fatorial(numero)
print(resultado)
