import random

#Gerar lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)

#Dividir a lista em 4 intervalos de 5 elementos
intervalos = [
    lista[0:5],
    lista[5:10],
    lista[10:15],
    lista[15:20]
]

#Contar negativos em cada intervalo
contagem_negativos = [sum(1 for n in intervalo if n < 0) for intervalo in intervalos]

#Encontrar o índice do intervalo com mais negativos
indice_para_deletar = contagem_negativos.index(max(contagem_negativos))

#Calcular índices para usar com del
inicio = indice_para_deletar * 5
fim = inicio + 5

# Deletar o intervalo
del lista[inicio:fim]

#Mostrar resultado
print("Lista após deletar o intervalo com mais negativos:", lista)
