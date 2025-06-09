#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
pares = [n for n in range(20, 51) if n % 2 == 0]
print("Números pares entre 20 e 50:", pares)

#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

quadrados = [n ** 2 for n in numeros]

print("Quadrados:", quadrados)

#Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [n for n in range(1, 101) if n % 7 == 0]

print("Números divisíveis por 7 entre 1 e 100:", divisiveis_por_7)


#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar']) 
paridade = ['par' if n % 2 == 0 else 'impar' for n in range(0, 30, 3)]

print(paridade)


 