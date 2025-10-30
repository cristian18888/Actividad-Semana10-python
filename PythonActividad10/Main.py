from modelos.modelo_mecanico import Mecanico
from modelos.modelo_carro import Carro
from modelos.modelo_maquina import Maquina


carro1 = Carro("Toyota", "Corolla", 2018)
carro2 = Carro("Ford", "Mustang", 2016)
carro3 = Carro("Honda", "Civic", 2019)
carros = [carro1, carro2, carro3]


maquina1 = Maquina("Elevador hidráulico", "Elevación de vehículos")
maquina2 = Maquina("Banco de pruebas", "Diagnóstico de motor")
maquina3 = Maquina("Pulidora automática", "Acabado y pulido")
maquinas = [maquina1, maquina2, maquina3]


nombre_mec = input("Ingrese nombre del mecánico: ")
exp = input("Ingrese años de experiencia: ")
while not exp.isdigit():
    print("Por favor ingrese un número válido para los años de experiencia.")
    exp = input("Ingrese años de experiencia: ")

mecanico = Mecanico(nombre_mec, int(exp))


print(f"\nMecánico: {mecanico.nombre}")
print("Carros disponibles para reparación:")
contador = 1
for carro in carros:
    print(f"{contador}. {carro}")
    contador += 1


seleccion = input("Seleccione el número del carro a reparar: ")
while not (seleccion.isdigit() and 1 <= int(seleccion) <= len(carros)):
    print("Número inválido. Intente nuevamente.")
    seleccion = input("Seleccione el número del carro a reparar: ")

carro_seleccionado = carros[int(seleccion) - 1]


print("\nMáquinas disponibles:")
contador = 1
for maquina in maquinas:
    print(f"{contador}. {maquina}")
    contador += 1


seleccion_maquina = input("Seleccione el número de la máquina a usar: ")
while not (seleccion_maquina.isdigit() and 1 <= int(seleccion_maquina) <= len(maquinas)):
    print("Número inválido. Intente nuevamente.")
    seleccion_maquina = input("Seleccione el número de la máquina a usar: ")

maquina_seleccionada = maquinas[int(seleccion_maquina) - 1]


print(f"\nMáquina seleccionada: {maquina_seleccionada.nombre}")
print("La máquina se inicia...")
maquina_seleccionada.en_uso = True

print(f"El carro {carro_seleccionado.marca} {carro_seleccionado.modelo} se eleva.")
print("Se realiza la reparación del carro...")
carro_seleccionado.estado = "Reparado"

print("El carro se baja de la máquina.")
print("La máquina se detiene...")
maquina_seleccionada.en_uso = False

print(f"\nEstado final del carro: {carro_seleccionado}")
print("Reparación completada.")
