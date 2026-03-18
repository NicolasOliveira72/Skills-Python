# Estoque de compras para a importação:

estoque = {
    "Abacate" : {"Preco": 6.85, "Quantidade": 18},
    "Abóbora" : {"Preco": 6.85, "Quantidade": 18},
    "Tomate" : {"Preco": 6.85, "Quantidade": 18},
    "Banana" : {"Preco": 6.85, "Quantidade": 18},
    "Melancia" : {"Preco": 6.85, "Quantidade": 18}
}

carrinho = []
total = 0

while True: 
    pedido = input("Digite o produto desejado ou sair: ").strip().capitalize()

    if pedido == "Sair":
        print("Compra cancelada/finalizada! ")
        break

    if pedido in estoque:

        if estoque[pedido]["Quantidade"] > 0:
            carrinho.append(pedido)
            estoque[pedido]["Quantidade"] -= 1
            total += estoque[pedido]["Preco"]
        else:
            print("Produto esgotado.")
    else:
        print("Produto nao cadastrado. ")

def recibo(a,b):
    print(f"Os itens comprados foram: {a}")
    print(f"O total de compras é: {b}")

def estoque_final(a):
    print(f"O estoque final é: {a}")
    
recibo(carrinho,total)
estoque_final(estoque)