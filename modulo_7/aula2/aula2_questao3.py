import string

while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")

    # Verifica se o usuário quer encerrar
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break

    # Remove espaços, pontuação e coloca tudo em minúsculo
    frase_limpa = ''
    for letra in frase:
        if letra.isalnum():  # Mantém apenas letras e números
            frase_limpa += letra.lower()

    # Verifica se é palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
