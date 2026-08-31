#Menu y ciclo
import Funciones
import Extras

def menu():
    print("----Menu ABM----")
    print("1. Agregar Dispositivo")
    print("2. Eliminar Dispositivo")
    print("3. Modificar Dispositivo")
    print("4. Ordenar Lista")
    print("5. Mostrar Lista")
    print("6. Cerrar Programa")

def ciclo(opcion):
    if opcion == 1:
        Funciones.agregar()
    elif opcion == 2:
        Funciones.eliminar()
    elif opcion == 3:
        Funciones.modificar()
    elif opcion == 4:
        Funciones.ordenar()
    elif opcion == 5:
        Funciones.mostrar()

