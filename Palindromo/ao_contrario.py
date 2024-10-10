print("""
+==================================+
|       Palindromo ou Não ?        |
+==================================+
""")

escreve = input("Digite uma Palavra: ").lower()

print(escreve,f"\n{escreve[::-1]}", )

if escreve == ''.join(reversed(escreve)):
    print("É um Palindromo")

else:
    print("Não é um Palindromo")