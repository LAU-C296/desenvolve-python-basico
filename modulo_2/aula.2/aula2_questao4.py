#4 - Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis.

saldo = 500.0
juros = 1.01

# Aplicando os juros mês a mês
saldo = saldo * juros  # após 1º mês
saldo = saldo * juros  # após 2º mês
saldo = saldo * juros  # após 3º mês

print("Após 3 meses meu novo saldo é")
print(saldo)


 