import random
import time

lista = []


def alta():
    fabricante = input("Ingrese el fabricante del producto: ")
    producto = input("Ingrese el nombre del producto: ")
    tipo = input("Ingrese el tipo del producto: ")
    ids = {producto["id"] for producto in lista}
    producto_id = random.randint(1, 100)
    while producto_id in ids:
        producto_id = random.randint(1, 100)
    lista.append({
        "id": producto_id,
        "nombre": producto,
        "tipo": tipo,
        "fabricante": fabricante,
    })
    print(f"Producto agregado con ID: {producto_id}")


def baja():
    producto_id = int(input("Ingrese el ID del producto a eliminar: "))
    for indice, producto in enumerate(lista):
        if producto["id"] == producto_id:
            lista.pop(indice)
            print("Producto eliminado.")
            return
    print("El ID indicado no existe.")


def modificacion():
    producto_id = int(input("Ingrese el ID del producto a modificar: "))
    producto = input("Ingrese el nuevo nombre del producto: ")
    tipo = input("Ingrese el nuevo tipo del producto: ")
    fabricante = input("Ingrese el nuevo fabricante del producto: ")
    for registro in lista:
        if registro["id"] == producto_id:
            registro.update(nombre=producto, tipo=tipo, fabricante=fabricante)
            print("Producto modificado.")
            return
    print("El ID indicado no existe.")


def listado():
    eleccion = int(input("Ingrese 1 para ver la lista en horizontal o 2 para ver en vertical: "))

    if eleccion == 1:
        print("ID | Nombre | Tipo | Fabricante")
        for registro in lista:
            print(f'{registro["id"]} | {registro["nombre"]} | '
                  f'{registro["tipo"]} | {registro["fabricante"]}')
    elif eleccion == 2:
        print("Lista de productos: ")
        for registro in lista:
            print("------")
            print(f'ID: {registro["id"]}')
            print(f'Nombre: {registro["nombre"]}')
            print(f'Tipo: {registro["tipo"]}')
            print(f'Fabricante: {registro["fabricante"]}')
            print("------")
            time.sleep(3)
    else:
        print("La opción indicada no existe.")




