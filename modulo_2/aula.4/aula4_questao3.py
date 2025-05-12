#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:

#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)

#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).

# Solicitando os dados dos três produtos
nome1 = input("Informe o nome do primeiro produto: ")
preco1 = float(input("Informe o preço unitário do primeiro produto: "))
quantidade1 = int(input("Informe a quantidade do primeiro produto: "))

nome2 = input("Informe o nome do segundo produto: ")
preco2 = float(input("Informe o preço unitário do segundo produto: "))
quantidade2 = int(input("Informe a quantidade do segundo produto: "))

nome3 = input("Informe o nome do terceiro produto: ")
preco3 = float(input("Informe o preço unitário do terceiro produto: "))
quantidade3 = int(input("Informe a quantidade do terceiro produto: "))

# Calculando o preço total
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)

# Exibindo o valor total com formatação
print(f"Total: R$ {total:,.2f}")



