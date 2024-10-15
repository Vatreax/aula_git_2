print("""
+==================================+
|  Tabuada do Número Selecionado   |
+==================================+
""")
while True:
    try:
        n1 = int(input("Digite um Número Inteiro: "))
        multi = int(input("Quantas vezes devo multiplicar: "))

        if n1 > 0 and multi > 0:
            break

        else: 
            print("\nDigite um valor positivo!\n")
    except ValueError:
        print("\nValor Errado!\n")


contador = 0 
while contador < multi:
    contador += 1
    r = n1 * contador
    
    print(f"{n1}x{contador}: {r}")