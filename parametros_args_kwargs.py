"""
args: não se sabe quantos argumentos.
Argumentos como tupla

"""

'''def soma(*num):
    total = 0
    for x in num:
        total += x
    print(f"A soma é: {total}")
soma(1,2,3)'''

'''
kwargs: valores com chaves
kwars em forma de dicionário
'''

def soma(**num):
    for x, y in num.items():
        print(f"Os valores são: {x}, {y}")

soma(name = "nicolas", apelido = "Hardtan")
