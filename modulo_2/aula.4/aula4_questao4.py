#4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

valor = int(input('Digite o valor em reais: ')) # Lê o valor em reais

# Notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calculando a quantidade de cada nota
for nota in notas:
    quantidade = valor // nota
    valor %= nota
    print(f"{quantidade} nota(s) de R${nota},00")

