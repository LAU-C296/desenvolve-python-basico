import random

def encrypt(lista_de_strings):
    chave = random.randint(1, 10)  # Gera a chave entre 1 e 10
    criptografados = []

    for texto in lista_de_strings:
        texto_criptografado = ''
        for caractere in texto:
            codigo = ord(caractere)
            # Verifica se está no intervalo visível (33 a 126)
            if 33 <= codigo <= 126:
                # Faz o deslocamento com retorno circular
                novo_codigo = ((codigo - 33 + chave) % 94) + 33
                texto_criptografado += chr(novo_codigo)
            else:
                # Se não estiver no intervalo, mantém o caractere
                texto_criptografado += caractere
        criptografados.append(texto_criptografado)

    return criptografados, chave

nomes = ["Maria", "João", "Carlos"]
criptografados, chave = encrypt(nomes)

print("Nomes criptografados:", criptografados)
print("Chave de criptografia:", chave)
