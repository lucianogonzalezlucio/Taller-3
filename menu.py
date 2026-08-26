import os
import time
import lista




def menu_ABM():
    print("===Menu ABM===")
    print("1. Alta")
    print("2. Baja")
    print("3. Modificación")
    print("4. Listado")
    print("5. Salir")
    print("===============")


def opciones(opcion):

    if opcion == 1:
        print("---Alta seleccionada---")
        lista.alta()
    elif opcion == 2:
        print("---Baja seleccionada---")
        lista.baja()
    elif opcion == 3:
        print("---Modificación seleccionada---")
        lista.modificacion()
    elif opcion == 4:
        print("---Listado seleccionado---")
        lista.listado()
    elif opcion == 5:
        print("---Saliendo del programa---")
        print("Gracias por operar, vuelva pronto")
    else:
        print("Opción no válida")



   