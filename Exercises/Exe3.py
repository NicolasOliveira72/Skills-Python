from data_Exe3 import estoque

carrinho = []
total = 0

def lines():
    line = "="
    print(line*30)


while True:
    request = input('Digite o produto desejado ou digite "Sair": ').strip().capitalize()
    if request != "Sair":
        if request in estoque:
            if estoque[request]["quantidade"] > 0:
                lines()
                print("Produto adicionado. ")
                carrinho.append(request)
                total += estoque[request]["preco"]
                estoque[request]["quantidade"] -= 1
                lines()
            else:
                print("Produto esgotado, caro cliente. ")
        else:
            print("Produto não cadastrado, caro cliente.")
    else:
        lines()
        print("Obrigado pela compra, caro cliente.")
        lines()
        print(" =============== Recibo =============== ")
        print(f"Carrinho: {carrinho}")
        print(f"Total {total}")
        lines()
        break