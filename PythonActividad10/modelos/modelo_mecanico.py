class Mecanico:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def iniciar_maquina(self, maquina):
        if not maquina.en_uso:
            print(f"{self.nombre} está iniciando la máquina '{maquina.nombre}'.")
            maquina.en_uso = True
        else:
            print(f"La máquina '{maquina.nombre}' ya está en uso.")

    def detener_maquina(self, maquina):
        if maquina.en_uso:
            print(f"{self.nombre} está deteniendo la máquina '{maquina.nombre}'.")
            maquina.en_uso = False
        else:
            print(f"La máquina '{maquina.nombre}' no está en uso.")

    def reparar_carro(self, carro, maquina):
        if maquina.en_uso:
            print(f"{self.nombre} está reparando el carro {carro.marca} {carro.modelo} usando la máquina {maquina.nombre}.")
            carro.estado = "Reparado"
        else:
            print(f"No se puede reparar el carro porque la máquina {maquina.nombre} no está en uso.")

    def __str__(self):
        return f"{self.nombre} ({self.experiencia} años de experiencia)"
