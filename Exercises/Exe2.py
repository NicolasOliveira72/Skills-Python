# Estoque de frutas:

estoque = {
    "Maçã": {"preço": 4.50, "quantidade": 50},
    "Banana": {"preço": 3.20, "quantidade": 120},
    "Laranja": {"preço": 2.99, "quantidade": 85},
    "Morango": {"preço": 7.50, "quantidade": 30},
    "Uva": {"preço": 8.90, "quantidade": 45},
    "Abacaxi": {"preço": 6.00, "quantidade": 25},
    "Manga": {"preço": 5.40, "quantidade": 60},
    "Melancia": {"preço": 12.00, "quantidade": 15},
    "Mamão": {"preço": 4.80, "quantidade": 40},
    "Limão": {"preço": 1.99, "quantidade": 150}
}

total = 0
carrinho = []

while True:
    requisicao = input('Digite a fruta desejada ou digite "Sair": ').strip().capitalize()
    if requisicao == "Sair":
        break
    if requisicao in estoque:
        if estoque[requisicao]["quantidade"] > 0:
            print(f"Produto {requisicao} adicionado!")
            total += estoque[requisicao]["preço"]
            estoque[requisicao]["quantidade"] -= 1
            carrinho.append(requisicao)
        else:
            print("Produto indisponível no momento")
    else:
        print("Produto não cadastrado")
    
def Recibo():
    line = "-"
    print(f"Carrinho: ", carrinho)
    print(line*30)
    print(f"Total: ", total)

def lines():
    line = "="
    print(line*30)



lines()
Recibo()
lines()