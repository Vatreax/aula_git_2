import math

try:
    n1 = int(input("Digite um Número Inteiro: "))
    def primo(n1):
        p1 = 2

        while p1 <= math.sqrt(n1):
            if n1 % p1 < 1:
                return False;
            p1 += 1;

        return n1 > 1;




except ValueError:
    print("Valor Invalido!")

print(primo(n1))