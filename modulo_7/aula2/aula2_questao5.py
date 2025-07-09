import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) > 3:
            # Separar os caracteres fixos e os que serão embaralhados
            primeira, meio, ultima = palavra[0], list(palavra[1:-1]), palavra[-1]
            random.shuffle(meio)
            palavra_embaralhada = primeira + ''.join(meio) + ultima
        else:
            # Palavras pequenas não são alteradas
            palavra_embaralhada = palavra
        resultado.append(palavra_embaralhada)

    return ' '.join(resultado)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
