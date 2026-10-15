# Sistema de supermercado:

estoque = {
    "Arroz": {"quantidade": 45, "preco": 7.89},
    "Feijão": {"quantidade": 30, "preco": 8.50},
    "Óleo": {"quantidade": 60, "preco": 6.20},
    "Açúcar": {"quantidade": 40, "preco": 4.15},
    "Café": {"quantidade": 25, "preco": 16.90},
    "Leite": {"quantidade": 120, "preco": 5.49},
    "Macarrão": {"quantidade": 50, "preco": 3.75},
    "Molho": {"quantidade": 80, "preco": 2.29},
    "Sal": {"quantidade": 3, "preco": 2.10},
    "Farinha": {"quantidade": 35, "preco": 5.30},
    "Manteiga": {"quantidade": 22, "preco": 11.40},
    "Queijo": {"quantidade": 18, "preco": 9.98},
    "Frango": {"quantidade": 14, "preco": 18.90},
    "Ovos": {"quantidade": 28, "preco": 10.50},
    "Detergente": {"quantidade": 75, "preco": 2.45},
    "Sabão": {"quantidade": 20, "preco": 14.99},
    "Creme": {"quantidade": 45, "preco": 4.20},
    "Papel": {"quantidade": 32, "preco": 17.80},
    "Biscoito": {"quantidade": 90, "preco": 3.15},
    "Suco": {"quantidade": 16, "preco": 12.60}
}

carrinho = []
total = 0
 
def lines():
    line = "="
    print(line*30)

lines()

while True:
    requisicao = input('Digite o produto  a ser comprado ou digite "Sair": ').strip().capitalize()
    if requisicao != "Sair": 
        if requisicao in estoque:
            if estoque[requisicao]["quantidade"] > 0:
                print("Produto adicionado ao carirnho, caro cliente")
                carrinho.append(requisicao)
                total += estoque[requisicao]["preco"]
                estoque[requisicao]["quantidade"] -= 1
            else:
                print("Produto esgotado, caro cliente")
        else:
            print("Produto indisponível no estoque, caro cliente")
    else:
        lines()

        print("Compra encerrada, caro cliente! Agradecemos sua preferência")
        
        print(" ========== Recibo ========== ")
        print(carrinho)
        print(total)
        lines()
        break

