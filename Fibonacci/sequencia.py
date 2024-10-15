def fibonados(n1):
    lista = [0,1]
    while len(lista) < n1:
        num = lista[-1] + lista[-2]
        lista.append(num)
    return lista
try:
    n1 = int(input("Digite o Número de Sequências: "))
    resultado = fibonados(n1)
    print(resultado)

except ValueError:
    print("\nDigite um Número Inteiro!\n")
