# Buscando partes da string (slice):

movieName= "Cidade Nova"
print(movieName[0:7]) 
print(movieName[4:9])
print(movieName[:6])
print(movieName[0:])
print(movieName[:])

# Buscando a String de dois em dois caracteres:

line = "-"
print(line*30)
print(movieName[::2])
print(movieName[5::2])

# Inverter uma string de trás pra frente:

print(line*30)
print(movieName[::-1])

# Demaais funcionalidades em uma String:

print(line*30)
print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize())
print(movieName.title())
print(movieName.find("v"))
print(movieName.replace("Nova", "Vizinha"))
print(movieName.split(','))


# Qubrando o código onde apresenta ",":

print(line*30)
description = """

    Carro Azul é um filme, de ação e aventura muito, apreciado
    e com exclente venda nas bilheterias.
"""