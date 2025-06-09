# Recebe duas listas de números do usuário
lista1 = input("Digite os números da primeira lista, separados por espaço: ").split()
lista2 = input("Digite os números da segunda lista, separados por espaço: ").split()

# Converte os elementos para inteiros
lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

# Intercala as listas
lista_intercalada = []
len1 = len(lista1)
len2 = len(lista2)
maior = max(len1, len2)

for i in range(maior):
    if i < len1:
        lista_intercalada.append(lista1[i])
    if i < len2:
        lista_intercalada.append(lista2[i])

print("Lista intercalada:", lista_intercalada)