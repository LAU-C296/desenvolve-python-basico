from datetime import datetime

# Pega a data e hora atual
agora = datetime.now()

# Formata e exibe a data e hora
print(f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}")
print(f"Hora: {agora.hour:02d}:{agora.minute:02d}")