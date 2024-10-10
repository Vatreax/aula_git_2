print("""
+==================================+
|  Tabuada do Número Selecionado   |
+==================================+
""")
n1 = int(input("Digite um Número: "))
multi = int(input("Quantas vezes devo multiplicar: "))
contador = 0

while contador < multi:
    contador += 1
    r = n1 * contador
    
    print(f"{n1}x{contador}: {r}")