print("""
+==================================+
|       Palindromo ou Não ?        |
+==================================+
""")

escreve = input("Digite uma Palavra: ").upper()

print(escreve,f"\n{''.join(reversed(escreve))}", )

if escreve == ''.join(reversed(escreve)):
    print("É um Palindromo")

else:
    print("Não é um Palindromo")