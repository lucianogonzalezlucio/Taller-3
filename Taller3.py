#PracticaListasDiccionarios
#Listas
lista1 = [1,2,3]
#print(lista1)
palabra= ("Hola")
lista1.insert(0,palabra)
#print(lista1)
lista1.insert(2, [4,5,6 ])
#print(lista1)
lista1[2].insert(0, "Hola")
#print(lista1)
lista1.count("Hola") 
#print ("La palabra " + palabra + " en la lista se repite " + str(lista1.count("Hola")) + " vez")
lista1.remove(3)
#print(lista1)
#print(len(lista1))
#print(len(lista1[2]))
lista2 = ["hamburguesa", "pizza", "tacos", "pancho", "papas fritas"]
#for Comida in lista2:
    #print(Comida)

#Asi se define un diccionario
# { clave : valor , clave : valor }
#persona = {"Nombre": "Luciano", "edad": 19}
#Tipos de metodo de acceso a datos
#print(persona["Nombre"])
#print(persona.get("edad"))
#print(persona.get("Altura", "No existe la clave"))

#listamaterias = {"Matematica": 7, "Fisica": 6, "Programacion": 10, "Electronica": 8}
#carrera= {"Nombre": "Telecomunicaciones","Alumno": "Luciano Silva ", "Materias": ["Matematica", "Fisica", "Programacion", "Electronica"]}
#print(carrera["Alumno"])
#print(carrera["Nombre"])
#print(carrera["Materias"])
#print (" === Notas === ")
#print (" Matematicas : " + str(listamaterias["Matematica"]))
#print (" Fisica : " + str(listamaterias["Fisica"]))
#print (" Programacion : " + str(listamaterias["Programacion"]))
#print (" Electronica : " + str(listamaterias["Electronica"]))

#carrera2 = input("Ingrese la nueva carrera que cursara : ")
#carrera["Nombre"] = carrera2
#carrera["Carreras en curso"] = carrera2
#carrera2 = {"Nombre": carrera2, "Alumno": "Luciano Silva ", "Materias": ["Matematica", "Fisica", "Programacion", "Electronica"]}
#print (carrera2)
#print (carrera)