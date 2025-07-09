from itertools import permutations

# Entrada da frase
frase = input("Digite uma frase: ")

# Entrada da palavra da frase
palavra = input("Digite uma palavra obbjetivo que esteja na frase: ")

# Verifica se a palavra está na frase
if palavra not in frase.split():
    print("A palavra não está na frase.")
else:
    # Gera anagramas
    anagramas = set([''.join(p) for p in permutations(palavra)])

    # Exibe o resultado
    print(f"Anagramas da palavra '{palavra}': {sorted(anagramas)}")
