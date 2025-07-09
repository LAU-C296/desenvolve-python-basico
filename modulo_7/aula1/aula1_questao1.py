while True:
    nome = input("digite seu nome aqui: ")
    for i in range(1, len(nome) + 1): #a primeira letra, depois soma com +1 ate acabar
        print(nome[:i])
    break