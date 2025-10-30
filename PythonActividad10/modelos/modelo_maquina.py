class Maquina:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.en_uso = False

    def __str__(self):
        estado = "En uso" if self.en_uso else "Disponible"
        return f"{self.nombre} ({self.tipo}) - Estado: {estado}"
