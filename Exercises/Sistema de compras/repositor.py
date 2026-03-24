from data import estoque

def read():
    busca = input("Digite o produto para consulta: ").strip().capitalize()
    if busca in estoque:
        print("Produto busca dicponível!")
        print(f"Preço: {estoque[busca]['Preco']} | Quantidade: {estoque[busca]['Quantidade']}")
    else:
        print("Produto não cadastrado")
    
def create():
    pedido = input("Digite o produto que deseja inserir: ").strip().capitalize()
    if pedido in estoque:
        print("Produto já cadastrado")
    else:
        preco = float(input("Digite o preço do produto: "))
        qtd = int(input("Digite a quantidade do produto: "))
        #Inserção ou atualização no dicionáqio:
        estoque[pedido] = {"Preco" : preco, "Quantidade" : qtd}
        print(f"Pedido {pedido} cadastrado com sucesso!")

def delete():
    pedido = input("Digite o produto que deseja excluir: ").strip().capitalize()
    if pedido in estoque:
        del estoque[pedido]
    else:
        print("Produto não cadastraddo!")
    