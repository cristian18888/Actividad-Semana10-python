class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.estado = "Dañado"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Estado: {self.estado}"


