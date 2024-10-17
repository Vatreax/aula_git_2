import math

n1 = int(input("Digite um Número Inteiro: "))

def primo(n1):
    if n1 <= 1:
        return "Não é primo"
    
    n2 = 2
    while n2 <= math.sqrt(n1):
        if n1 % n2 == 0:
            return "Não é primo"
        n2 += 1
    
    return "É primo"

print(primo(n1))
