# Solicita a frase do usuário
frase = input("Digite uma frase: ").lower()

# Definição das vogais
vogais = 'aeiou'

# Lista de vogais na frase, ordenada
lista_vogais = sorted([letra for letra in frase if letra in vogais])

# Lista de consoantes na frase, sem espaços
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

# Resultados
print("Vogais ordenadas:", lista_vogais)
print("Consoantes:", lista_consoantes)
