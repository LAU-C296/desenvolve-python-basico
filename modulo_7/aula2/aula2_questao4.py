def validador_senha(senha):
    # Verifica se tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Verifica presença de pelo menos:
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    especiais = "@#$%&*!_?"

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_caractere_especial = True

    # Verifica se todos os critérios foram atendidos
    if tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial:
        return True
    else:
        return False

# exemplo de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1)) 
print(validador_senha(senha2)) 
print(validador_senha(senha3))  
