#Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto". 

#Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 

ano = int(input("Digite um ano: "))

# se ao dividir o ano por 4, o restp for 0 e se o ano for dividido por 100 o resto for diferente de 0. imprimir "Bissexto" ou se o ano for dividido por 400 o resto for 0, imprimir "Bissexto"
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
    print("Bissexto")
#se nenhuma das duas for verdadeiras, imprimir "Não Bissexto"
else:
    print("Não Bissexto")