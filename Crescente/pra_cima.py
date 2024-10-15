lista = []
n1 = int(input("Quantos números deseja inserir: "))

contador = 0
while contador < n1:
    try:
        n2 = int(input(f"Digite o {contador+1}°Número Inteiro: "))
        lista.append(n2)
        contador += 1
    except ValueError:
        print("\nDigite um Número Inteiro!\n")

print(sorted(lista))