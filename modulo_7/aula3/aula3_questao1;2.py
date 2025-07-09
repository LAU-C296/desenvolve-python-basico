import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define o caminho do arquivo (na mesma pasta do script)
caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")

# Salva a frase no arquivo
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write(frase)

# Imprime o caminho completo do arquivo
print(f"Frase salva em {caminho_arquivo}")

import re
import os

# Caminho dos arquivos
caminho_frase = os.path.join(os.getcwd(), "frase.txt")
caminho_palavras = os.path.join(os.getcwd(), "palavras.txt")

# Lê o conteúdo de "frase.txt"
with open(caminho_frase, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Usa regex para encontrar somente palavras compostas por letras
palavras = re.findall(r'\b[a-zA-ZáéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ]+\b', conteudo)

# Salva cada palavra em uma nova linha em "palavras.txt"
with open(caminho_palavras, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# Lê e imprime o conteúdo de "palavras.txt"
with open(caminho_palavras, "r", encoding="utf-8") as f:
    print(f.read())
