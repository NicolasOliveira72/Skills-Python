# Estrutura de repetição: FOR:

# Impriindo números menores que 6: 

numeros = [1,2,3,4,5,6,72,4,6,1,8,4,8,23,6,7,2,9,3]

'''for x in numeros:
    if x <= 5:
        print(x) 
'''
# Interrompendo a sequencia de código ao cegar no 5:

'''for x in numeros:
    if x == 5:
        break
    print(x)'''

# Analisando filmes:

name = input("Digite o nome do filme: ")
quant = int(input("Digite a quantidade de análises desejada: "))

x = 0
for x in range(quant):
    av = float(input("Digite a nota do filme: "))
    x += av

if quant > 0:
    print(f"A média do filme é: {x/quant}")
else:
    print("Não há avliações! ")


