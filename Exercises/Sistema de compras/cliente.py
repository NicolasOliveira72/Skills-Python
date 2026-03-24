# Compras no hortfrut pelo cliente:

from data import estoque

def comprar(carrinho, total):
    carrinho = []
    total = 0
    
    while True: 
        pedido = input("Digite o produto desejado ou sair: ").strip().capitalize()

        if pedido == "Sair":
            print("Compra cancelada/finalizada! ")
            break

        if pedido in estoque:
            if estoque[pedido]["Quantidade"] > 0:
                quantidade = int(input(f"Digite a quantidade de produtos (apenas {estoque[pedido]["Quantidade"]} em estoque): "))
                if estoque[pedido]["Quantidade"] >= quantidade:
                    carrinho.extend([pedido] * quantidade)
                    estoque[pedido]["Quantidade"] -= quantidade
                    total += estoque[pedido]["Preco"] * quantidade
                else:
                    print("Quantidade insuficiente em estoque!")
            else:
                print("Produto esgotado.")
        else:
            print("Produto nao cadastrado. ")
    return carrinho, total

def exportar_recibo(carrinho, total):
    with open ("Exercises/Sistema de compras/recibo.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write("====== Recibo de compras ======\n")
        for item in carrinho:
            arquivo.write(f"Produto: {item}\n")
        arquivo.write("===============================\n")
        arquivo.write(f"Total final = {total:.2f}\n")
    print("Recibo exportado")

