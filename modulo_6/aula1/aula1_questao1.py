# Cria uma lista vazia e adiciona 20 números aleatórios de -100 a 100
import random

n = []
for i in range (20):
    valor = random.randint(-100,100)
    n.append(valor)

# imprimir a lista ordenada, sem modificar a lista original
print(sorted(n))

#A lista original
print(n)

#O índice do maior valor da lista
print(("o maior numero está no índice:",max(n)))

#O índice do menor valor da lista
print("o menor numero está no índice:",min(n))