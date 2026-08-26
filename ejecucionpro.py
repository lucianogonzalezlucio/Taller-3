import menu

while True:
    print("------Bienvenido------")
    menu.menu_ABM()
    opcion = int(input("Ingrese su eleccion: "))
    menu.opciones(opcion)
    if opcion == 5:
        break
   
