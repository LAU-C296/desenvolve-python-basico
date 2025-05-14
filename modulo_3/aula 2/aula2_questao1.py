#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão. 

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#se somando os dois numeros do resto (%) da divisao por 2 for 0, ent o numero é par, se não é ímpar

if( numero + numero2) % 2 == 0:  

    print("A soma é par")
else:
    print("A soma é ímpar")