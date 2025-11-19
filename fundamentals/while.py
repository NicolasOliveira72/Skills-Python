# Qunado valor for maior que 5, parar a implementação:

# filmes = [1,2,3,4,5,6,7,8]

'''x = 0
while x < len(filmes):
    if filmes[x] == 5:
        break
    print(filmes[x])
    x += 1'''

line = "="
print(line*30)

#  Pular o 5:

'''x = 0
while x < len(filmes):
    if filmes[x] == 5:
        x += 1
        continue
    print(filmes[x])
    x += 1'''


# Avaliação do filme:

name = input("Digite o nome do filme: ")
quant = int(input("Digite a quantidade de avaliações desejada: "))

incre = 0
total = 0

while incre < quant:
    av = float(input("Digite a nota do filme: "))
    total += av
    incre += 1

if quant > 0:
    print(f"A média é {total/quant}")
else:
    print("Não há avaliações!")