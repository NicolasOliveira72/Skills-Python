# Dicionário:

filmes = {
    "nome": "Interestelar",
    "Ano de lançamento" : 2014,
    "Nota" : 9.8,
    "Gênero" : ["Ação", "Romance", "Ficção"]
}

print(filmes)
print(len(filmes))
print(type(filmes))

# Buscar um alemento do dicionário:

print(filmes["Gênero"])
print(filmes.get("Nota"))

# Buscar apenas as chaves do docionário:

print(filmes.keys())

# Buscar apenas os valores do dicionário:

print(filmes.values())

# Buscar chaves e valores:

print(filmes.items())

# Adicionar itens no dicionário:

filmes["Diretor"] = "Crhistopher Nolan"
print(filmes)

# Atualizar itens do dicionário;
filmes.update({"Nota": 9.9})
print(filmes)

# Remover itens do docionário:

filmes.pop("Nota")
print(filmes)