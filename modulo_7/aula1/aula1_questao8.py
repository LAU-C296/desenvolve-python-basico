def validar_cpf(cpf):
    # Remove pontos e traços
    cpf_numeros = cpf.replace(".", "").replace("-", "")
    
    # Verifica se tem 11 dígitos
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return "Inválido"

    # Verifica se todos os dígitos são iguais (ex.: 111.111.111-11 -> inválido)
    if cpf_numeros == cpf_numeros[0] * 11:
        return "Inválido"

    # Cálculo do primeiro dígito verificador
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf_numeros[i]) * (10 - i)
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1

    # Cálculo do segundo dígito verificador
    soma2 = 0
    for i in range(9):
        soma2 += int(cpf_numeros[i]) * (11 - i)
    soma2 += digito1 * 2
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    # Verifica se os dígitos conferem com os informados
    if int(cpf_numeros[9]) == digito1 and int(cpf_numeros[10]) == digito2:
        return "Válido"
    else:
        return "Inválido"


# Execução
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf)
print(resultado)
