import csv

# Caminho para o arquivo CSV baixado do Kaggle
csv_file = 'spotify-2023.csv'

# Abrir o arquivo e imprimir as 5 primeiras linhas para inspeção
with open(csv_file, encoding='latin-1') as f:
    for i in range(5):
        print(f.readline().strip())

# Função para verificar se a linha deve ser ignorada
def linha_valida(row):
    # Ignora linhas com aspas em track_name ou artist(s)_name
    # (exceto se for apenas para delimitar o campo)
    # Se o campo track_name ou artist(s)_name começa e termina com aspas, mas contém vírgula dentro, ignorar
    # Se o campo artist_count > 1, ignorar
    try:
        track_name = row['track_name']
        artist_name = row["artist(s)_name"]
        artist_count = int(row['artist_count'])
        # Ignorar se há aspas e vírgula dentro do campo
        if (track_name.startswith('"') and track_name.endswith('"') and ',' in track_name) or \
           (artist_name.startswith('"') and artist_name.endswith('"') and ',' in artist_name):
            return False
        if artist_count > 1:
            return False
        return True
    except Exception:
        return False

# Dicionário para armazenar a música mais tocada de cada ano
mais_tocadas = {}

with open(csv_file, encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            year = int(row['released_year'])
            if 2012 <= year <= 2022 and linha_valida(row):
                streams = int(row['streams'])
                if (year not in mais_tocadas) or (streams > mais_tocadas[year][3]):
                    mais_tocadas[year] = [
                        row['track_name'],
                        row["artist(s)_name"],
                        year,
                        streams
                    ]
        except Exception:
            continue

# Gerar lista ordenada por ano
resultado = [mais_tocadas[year] for year in sorted(mais_tocadas)]

print(resultado)