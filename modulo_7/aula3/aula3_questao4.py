import random

# Lê os estágios do enforcado a partir do arquivo
def carrega_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    fases = conteudo.strip().split("\n\n")
    return fases

# Lê a lista de palavras e escolhe uma aleatoriamente
def escolhe_palavra():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
        palavras = [linha.strip().lower() for linha in f.readlines()]
    return random.choice(palavras)

# Imprime o enforcado conforme o número de erros
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Função principal do jogo
def jogar_forca():
    palavra = escolhe_palavra()
    estagios = carrega_enforcado()
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = []
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while erros < 6 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Letras erradas:", " ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Boa! Você acertou uma letra.")
        else:
            erros += 1
            letras_erradas.append(letra)
            print("Letra errada!")
            imprime_enforcado(erros, estagios)

    if "_" not in letras_descobertas:
        print("\nParabéns! Você acertou a palavra:", palavra)
    else:
        print("\nQue pena! Você foi enforcado.")
        imprime_enforcado(erros, estagios)
        print("A palavra era:", palavra)

# Executar o jogo
if __name__ == "__main__":
    jogar_forca()
