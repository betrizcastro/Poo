class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        print(f"O {self.marca} {self.modelo} está desligado.")

    def andar(self):
        print(f"O {self.marca} {self.modelo} está andando.")


carro = Veiculo("Fiat", "Uno")
carro.ligar()
carro.desligar()
carro.andar()


