n = int(input("Digite um número inteiro: "))
maior = 0

while n > 0:
    x = int(input("Digite um número inteiro: "))
    if x > maior:
        maior = x
        n -= 1
        break
print("O maior número digitado foi:", maior)

#nao ta dando certo


