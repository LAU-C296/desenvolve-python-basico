# Este programa calcula a diferença absoluta entre dois números decimais fornecidos pelo usuário.

# Solicita ao usuário que insira dois números decimais
num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))

# Calcula a diferença absoluta entre os dois números
diferenca_absoluta = abs(num1 - num2)

# Arredonda o resultado para duas casas decimais
diferenca_arredondada = round(diferenca_absoluta, 2)

# Exibe o resultado
print(f"A diferença absoluta entre {num1} e {num2} é: {diferenca_arredondada}")
