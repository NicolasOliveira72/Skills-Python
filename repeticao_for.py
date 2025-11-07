# Estrutura de repetição: FOR:

# Impriindo números acima de 5: 

"""
numeros = [1,2,3,4,5,6,7,8,9,5,7,3,6,2,8]

for x in numeros:
    if x >= 5:
        print(x)
"""

# Interrompendo a sequencia de código ao cegar no 5:

"""
numeros = [1,2,33,55,3,4,5,6,7,8,9,5,7,3,6,2,8]

for x in numeros:
    if x == 5:
        break
    print(x)"""

# Analisando filmes:

name = input("Digite o nome do filme: ")
quantAva = int(input("Digite a quatidade de avaliações desejada: "))

x = 0
for y in range(quantAva):
        av = float(input("Digite a avaliação: "))
        x += av

if quantAva > 0:
    print(f"A media do filme é {x/quantAva}")
else:
    print("Não há avaliação")