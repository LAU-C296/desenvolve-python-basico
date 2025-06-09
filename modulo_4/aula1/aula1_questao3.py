#se a nota for >= a 60 imprima aprovado 
#se a nota for >= a 40 imprima recuperação
#se a nota for < a 40 imprima reprovado

while True:
        n1 = float(input("Digite sua nota 1: "))
        n2 = float(input("Digite sua nota 2: "))
        n3 = float(input("Digite sua nota 3: "))

        m = (n1 + n2 + n3) / 3
        if m >= 60:
            print("Aprovado")
            break
        elif m >= 40:
            print("Recuperação")
            break
        else:
            print("Reprovado")
            break
print("Fim")

