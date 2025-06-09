import random

# Criando as listas com 20 números aleatórios de 0 a 50
list1 = [random.randint(0, 50) for _ in range(20)]
list2 = [random.randint(0, 50) for _ in range(20)]

# Criando a lista de interseção (sem duplicatas e ordenada)
intersecao = sorted(set(list1) & set(list2))

# Exibindo as listas
print("Lista 1:", list1)
print("Lista 2:", list2)
print("\nLista de interseção (ordenada e sem duplicatas):", intersecao)

# Contando quantas vezes cada número da interseção aparece em cada lista
for num in intersecao:
    count1 = list1.count(num)
    count2 = list2.count(num)
    print(f"O número {num} aparece {count1} vez(es) na Lista 1 e {count2} vez(es) na Lista 2.")
