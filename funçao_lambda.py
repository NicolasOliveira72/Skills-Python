'''# Função Lambda:

# Exponencial:

power = lambda num: num ** 2
print(power(4))
print(power(5))

# Função queverifica se o número é par:

line = "="
print(line*30)

ver = lambda x: x % 2 == 0
print(ver(4))
print(ver(5))

# Fnução que divide um número por outro:

print(line*30)
divisao = lambda a,b: a + b
print(divisao(15,3))
print(line*30)

# Função que inverte ua string:

ineverte = lambda word: word[::-1]
print(ineverte("Python"))'''

# Funcionalidades para filmes:

filmes = ["Mine", "Titanic", "Mad Max"]
notes = {
    "Mine": [9, 8, 7.5],
    "Titanic": [8, 8, 7],
    "Mad Max": [9.6, 8, 7.5]
}

# Média dos filmes:

med = lambda medfilme: sum(notes[medfilme]) / len([notes])
print(f"A méda do mine é: {med("Mine")}")

# Buscar filme:

busca = lambda namefilme: namefilme in notes
print(f"Mine está na lista?: {busca("Mine")}")

# Recomendação de filme:

recomendar = lambda namefilme: f"Recomendado {namefilme} com media de {med(namefilme)}" 
print(f"{recomendar("Mad Max")}")