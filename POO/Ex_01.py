# Working with class:

class Car:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O carro do modelo {self.modelo} da marca {self.marca} está ligado!")

novo_objeto = Car("Gurgel", "Elétrico")

print("Marca: " + novo_objeto.marca)
novo_objeto.ligar()