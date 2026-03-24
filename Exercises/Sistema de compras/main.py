import cliente, repositor

def line():
    lines = "="
    print(lines*30)

line()
print("SISTEMA DE VENDAS EM PYTHON")
line()

request = int(input("Digite 1 para realizar compras:\nDigite 2 para editar estoque:"))

if int == 1:
    itens, valor_total = cliente.comprar([], 0)
    cliente.exportar_recibo(itens, valor_total)
elif int ==2:
    request_client = int(input("Escolha uma opção:\n 1 : Consultar.\n 2 : Inserir/Editar.\n 3 : Remover."))
    if request_client == 1:
        repositor.read()
    elif request_client == 2:
        repositor.create
    elif request_client == 3:
        repositor.delete
    elif request_client == 4:
        print("Compra encarrada!")
    print("Resposta inválida!")

line()