urls = ["www.google.com", "www.facebook.com", "www.youtube.com", "www.GitHub.com"]

# Cria a lista apenas com os nomes dos domínios
dominios = [url[4:-4] for url in urls]

print("Lista de domínios:", dominios)
