frase = input("Digite uma frase aqui: ")

for letra in "aeiou":
    cont = 0
    indices = []
    for i, char in enumerate(frase):
        if char.lower() == letra:
            cont += 1
            indices.append(i)
    print(f"Existem {cont} '{letra}' na frase nos índices {indices}.")
	

