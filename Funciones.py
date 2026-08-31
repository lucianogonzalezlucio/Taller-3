#Agregar, Eliminar, Modificar, Ordenar y Mostarar
import random
import Extras
import time

lista = []

def agregar():
    print("----Opcion Agregar dispositivo seleccionada----")
    id_dispositivo = random.randint(1, 100)
    nombre = input("Ingrese el Nombre del dispositivo: ")
    tipo = input("Ingrese el Tipo del dispositivo: ")
    fabricante = input("Ingrese el fabricante:  ")
    dispositivo = {
        "id": id_dispositivo,
        "Nombre": nombre,
        "Tipo": tipo,
        "Fabricante": fabricante,

     }
    lista.append(dispositivo)
    Extras.carga()
    print("----Dispositivo Agregado correctamente----")
    print("Id del dispositivo", id_dispositivo)

def eliminar():
    id_dispositivo = int(input("Que dispositivo desea eliminar (Agregue el ID): "))
    dispositivo_encontrado = None
    for dispositivo in lista:
        if dispositivo["id"] == id_dispositivo:
            dispositivo_encontrado = dispositivo
            break
    
    if dispositivo_encontrado:
        lista.remove(dispositivo_encontrado)
        Extras.carga()
        print(" El dispositivo fue eliminado con éxito ")
    else:
        print(" Error: el dispositivo que desea eliminar no se encuentra en la lista")

def modificar():
    id_dispositivo = int(input("Ingrese el ID del producto que desea modificar"))
    if len(lista) < 1:
                 Extras.carga()
                 print (" No hay dispositivos registrados para modificar ")
                 return

    print ("-- Datos --")
    dato1 = input (" Ingrese el nombre del dispositivo Nuevamente : ")
    dato2= input (" Ingrese el tipo de dispositivo Nuevamente : ")
    dato3 = input (" Ingrese el fabricante del dispositivo Nuevamente : ")
    
    dispositivo_modificar = { "nombre" : dato1, "Tipo": dato2, "Fabricante" : dato3 }

    if (dispositivo_modificar) in lista:
            dato4 = input(" Ingrese el nuevo nombre del dispositivo: ").strip()
            dato5 = input(" Ingrese el tipo del nuevo dispositivo: ").strip()
            dato6 = input(" Ingrese el fabricante del nuev dispositivo : ")
            lista.remove({ "nombre" : dato1, "Tipo": dato2, "Fabricante" : dato3 })
            lista.append({ "nombre" : dato4, "Tipo": dato5, "Fabricante" : dato6 })
            Extras.carga()
            print (" -- Dispositivo modificado con éxito -- ")
    else: 
            print ( " Opcion no valida " )

def ordenar():
    global lista
    lista = sorted(lista, key=lambda x: x["id"])
    Extras.carga()
    print("----Lista ordenada correctamente----")

def mostrar():
    if len(lista) < 1:
        Extras.carga()
        print("No hay dispositivos registrados para mostrar")
        return
    print("----Dispositivos Registrados----")
    for dispositivo in lista:
        print(f"\nID: {dispositivo['id']}")
        print(f"Nombre: {dispositivo['Nombre']}")
        print(f"Tipo: {dispositivo['Tipo']}")
        print(f"Fabricante: {dispositivo['Fabricante']}")
        print("-" * 30)
        time.sleep(2)

