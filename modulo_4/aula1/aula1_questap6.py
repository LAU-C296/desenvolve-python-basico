n = int(input("me diga quantos experimentos: "))
cont = 0
somasapo, somarato, somacoelho = 0, 0, 0

while cont < n:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo = input()
    if tipo == "S":
        somasapo = quantia
    elif tipo == "R":
        somarato = quantia
    elif tipo == "C":
        somacoelho = quantia
    cont += 1


print("total de cobaias:", somasapo+somarato+somacoelho)
print("total de sapos:", somasapo)
print("total de ratos:", somarato)
print("total de coelhos:", somacoelho)
