# Estoque de compras para a importação:

estoque = {
    "Abacate" : {"Preco": 6.85, "Quantidade": 3},
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

def exportar_recibo(carrinho, total):
    with open ("recibo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("====== Recibo de compras ======\n")
        for item in carrinho:
            arquivo.write(f"Produto: {item}\n")
        arquivo.write("===============================\n")
        arquivo.write(f"Total final = {total:.2f}\n")
    print("Recibo exportado")

exportar_recibo(carrinho, total)
