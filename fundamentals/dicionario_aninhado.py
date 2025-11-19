# Dicionário aninhado:

import pprint

filmes = {

    "Interestelar": {
    "Ano de lançamento" : 2014,
    "Nota" : 9.8,
    "Gênero" : ["Ação", "Romance", "Ficção"]
    },

    "Mine": {

    "Ano de lançamento" : 2017,
    "Nota" : 9.2,
    "Gênero" : ["Ação", "Reflexão", "Ficção"]
    }
}

# Imprimindo na tela o dicionário completo:

print(filmes)

# Buscando um dos filmes do dicionário:

ab = pprint.PrettyPrinter(depth=4)
ab.pprint(filmes)

# Buscar uma informação de um dicionário aninhado:

line = "="
print(line*30)
print(filmes["Interestelar"]["Gênero"])

# Adicionar novo item em um subdicionário:

print(line*30)
filmes["Interestelar"]["Diretor"] = "Crhistopher Nolan"
print(filmes["Interestelar"])

# Excluir um subdicionário:

print(line*30)
del filmes["Mine"]
ab.pprint(filmes)