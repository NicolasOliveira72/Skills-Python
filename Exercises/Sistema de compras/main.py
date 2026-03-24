import cliente

def line():
    lines = "="
    print(lines*30)

line()
print("SISTEMA DE VENDAS EM PYTHON")
line()

itens, valor_total = cliente.comprar([], 0)
cliente.exportar_recibo(itens, valor_total)

line()