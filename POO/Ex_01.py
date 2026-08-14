# Working with class:

class Car:

    def ligar(self):
        print("Carro ligado!")

    @staticmethod
    def ascender_farol():
        print("farois ligados")

carro1 = Car()

carro1.ligar()
carro1.ascender_farol()