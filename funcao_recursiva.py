# Trabalhando com função recursiva:

'''def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num + fatorial(num -1))

number = int(input("Digite o valor para oo cálculo: "))
print(f"O fatorial de {number} é: {fatorial(number)}")'''

# Soma total de um número:

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num -1))

number = int(input("Digite o valor para oo cálculo: "))
print(f"A soma tota de {number} é: {fatorial(number)}")