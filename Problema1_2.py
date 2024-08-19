'''
Una red transmite datos a 100 megabits por segundo. Crea una función utilizando *Python* que permita calcular la cantidad de datos transmitidos en una cierta cantidad de tiempo (en segundos). Luego utiliza la función y calcula cuántos datos se transmiten en:

* 45 segundos
* 1,5 minutos
* 1 hora
'''

def Megabits():
    print("Ha ingresado a la maquina de calculo de Megabits")
    print("-" * 150)
    tiempo = float(input("Ingrese la cantidad tiempo para calcular: "))
    unidad_tiempo =input("Ingresa la unidad de tiempo que ultilizaras(seg, min ,hora)").lower()
    calculo = 100 * tiempo
    if unidad_tiempo == "seg":
        print(f"son {calculo} Megabits en {tiempo} segundos")
    elif unidad_tiempo == "min":
        calculo = calculo * 60
        print(f"son {calculo} Megabits en {tiempo} minutos")
    elif unidad_tiempo == "hora":
        calculo = calculo * 60 * 60
        print(f"son {calculo} Megabits en {tiempo} horas")
    else:
        print("ingreso no valido")

Megabits()

'Problema 2'

print("Listado de datos transmitidos (en Megabits) desde 0 hasta 1.000 segundos:")
print("-" * 150)
for i in range(0, 1001, 100):
    datos = 100 * i
    print(f"Tiempo: {i} segundos - Datos transmitidos: {datos} Megabits")