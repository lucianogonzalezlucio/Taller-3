#Solo ejecucion
import Opciones
import Extras

while True:
    Opciones.menu()
    opcion =  int(input("Seleccione una Opcion: "))
    Opciones.ciclo(opcion)
    if opcion == 6:
        print("Gracias por operar con nosotros")
        print("Saliendo...")
        Extras.carga()
        break
    