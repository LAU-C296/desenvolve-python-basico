# Lista para armazenar os números
numeros = []

print("Digite números inteiros (digite 'sair' para encerrar):")

# Loop para entrada dos números
while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == 'sair': 
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números antes de sair.")
            continue
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'sair'.")

# Saídas com fatiamento
print("\n Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
