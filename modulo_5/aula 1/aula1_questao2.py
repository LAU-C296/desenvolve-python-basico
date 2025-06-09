import random
import math

    # Solicita ao usuário o valor de n
n = int(input("Digite o número de valores inteiros aleatórios a serem gerados (n): "))

    # Gera n valores inteiros aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]

    # Calcula a soma dos valores
soma = sum(valores)

    # Calcula a raiz quadrada da soma
raiz_quadrada = math.sqrt(soma)

    # Exibe os resultados
print(f"Valores gerados: {valores}")
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")