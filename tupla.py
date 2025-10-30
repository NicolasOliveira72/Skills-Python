# Tuplas são imutáveis, ao contrário das listas

filmes = ("A Origem", "A Volta ao Mundo em 80 dias", "O Conde de Monte Cristo", "Os pecadores")

line = "="
print(line*30)
print(type(filmes))

# Buscando os dois primeiros itens da tupla:
print(line*30)
print(filmes[:2])

# Buscar o último item da tupla:
print(line*30)
print(filmes[-1])

# Buscar filmes até uma determinada posição:
print(line*30)
print(filmes[0:3])

# Recuperar o índice pelo nome:
print(line*30)
print(filmes.index("O Conde de Monte Cristo"))

print(line*30)
cid1 = input("Digite a primeira cidade:")
cid2 = input("Digite a segunda cidade: ")
cid3 = input("Digite a terceira cidade: ")

tuplaCidades = []
tuplaCidades.extend([cid1,cid2,cid3])
print(tuplaCidades)
print(tuplaCidades[-1])
print(len(tuplaCidades))

