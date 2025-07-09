# Lista com os nomes dos meses
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

# Solicita a data
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa dia, mês e ano
try:
    dia, mes, ano = data.split('/')

    # Converte o mês para inteiro e pega da lista (índice começa em 0)
    nome_mes = meses[int(mes) - 1]

    # Imprime a data formatada
    print(f"Você nasceu em {dia} de {nome_mes.capitalize()} de {ano}.")
except:
    print("Data inválida. Use o formato dd/mm/aaaa corretamente.")

