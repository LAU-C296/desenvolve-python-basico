# Solicita a frase
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Substitui as vogais por "*"
frase_sem_vogais = ""

for letra in frase:
    if letra in vogais:
        frase_sem_vogais += "*"
    else:
        frase_sem_vogais += letra

# Exibe o resultado
print("Frase com vogais substituídas:", frase_sem_vogais)
