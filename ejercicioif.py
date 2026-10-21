nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18:# el if va seguido de la mcondicion y dos puntos
    print("Eres mayor de edad")
else:# el else va seguido de dos puntos para decidir que se hace si no se cumple la condicion del if
    print("No eres mayor de edad")
    print("no puedes ingresar a la pagina")