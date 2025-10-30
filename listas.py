filme = ["A Origem", "Os pecadores"]

line = "="
print(line*30)
print(type(filme))

print(line*30)
print(len(filme))

print(line*30)
print(filme.index("Os pecadores"))

print(line*30)
filme.append("O Conde de Monte Cristo")
filme.append("A Volta ao Mundo em 80 dias")
print(filme)

print(line*30)
filme.sort()
print(filme)

print(line*30)
copiadalista = filme.copy()
copiadalista.remove("O Conde de Monte Cristo")
print(copiadalista)

print(line*30)
filme.clear()
print(f"Lista esvaziada: {filme}")