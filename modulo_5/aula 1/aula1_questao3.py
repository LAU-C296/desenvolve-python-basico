import random
# Gera um número aleatório entre 1 e 10 
numero_aleatorio = random.randint(1, 10)
# Inicializa o palpite do usuário como None
palpite_usuario = None
# Loop até que o usuário acerte o número
while palpite_usuario != numero_aleatorio:
    # Solicita ao usuário que insira um palpite
    palpite_usuario = int(input("Adivinhe o número entre 1 e 10: "))
    
    # Fornece feedback sobre o palpite
    if palpite_usuario < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif palpite_usuario > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número!")