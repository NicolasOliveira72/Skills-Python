# Trabalhando com set:

filmes = {"A Origem", "A Volta ao Mundo em 80 dias", "O Conde de Monte Cristo", "Os pecadores", True}
line = "="

print(line*30)
print(filmes)

# Verificando tipo do set:
print(line*30)
print(type(filmes))

# Removendo item do set:
print(line*30)
filmes.remove("A Origem")
print(filmes)

# Adicionando item do outro set: 
print(line*30)
filmes2 = {"Mine", "Os três mMosqueteiros", "A Origem", 1}
filmes.update(filmes2)
print(filmes)

