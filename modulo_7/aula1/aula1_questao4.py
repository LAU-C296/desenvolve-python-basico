numero = input("Digite o número de celular (apenas dígitos): ").strip()

if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9:
    if numero[0] != '9':
        print("Número inválido: o primeiro dígito deve ser 9.")
        exit()
else:
    print("Número inválido: deve conter 8 ou 9 dígitos.")
    exit()

# Formata como 9XXXX-XXXX
numero_formatado = f"{numero[:5]}-{numero[5:]}"
print("Número formatado:", numero_formatado)