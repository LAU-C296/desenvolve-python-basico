import random #random para geracao aleatoria de numeros

# Gera um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera uma lista com num_elementos valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprime a lista
print("Lista de elementos:", elementos)

# Soma dos valores da lista
soma = sum(elementos)
print("Soma dos valores:", soma)

# Média dos valores da lista
media = soma / num_elementos
print("Média dos valores:", media)