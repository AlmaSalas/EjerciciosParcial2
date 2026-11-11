nombre = ""
apellidos = ""
edad = 0
fechadenacimiento = ""
correo = ""
contraseña = ""
confirmarcontrasena = ""
opcion = 0


print ("Bienvenido al sistema de registro de clientes")
print ("---------Menú principal---------")
print ("1. Registrar clientes")
print ("2. ver información de clientes")
print ("3. Borrar información de clientes")
print ("4. Modificar información de clientes")
print ("5. Salir")
print ("---------------------------------")
opcion = int(input("Seleccione una opción: "))

match opcion:#AQUI INICIA EL MATCH, QUE ES UNA VALIDACION DE CASO

    case 1:
        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        edad = int(input("Ingrese su edad: "))
        fechadenacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmarcontrasena = input("Confirme su contraseña: ")
    case 2:
        print ("Nombre: ", nombre, "Apellidos: ", apellidos, "Edad: ", edad, "Fecha de nacimiento: ", fechadenacimiento, "Correo electrónico: ", correo, "Contraseña: ", contraseña, "Confirmar contraseña: ", confirmarcontrasena)
    case 3:
        nombre = ""
        apellidos = ""
        edad = 0
        fechadenacimiento = ""
        correo = ""
        contraseña = ""
        confirmarcontrasena = ""
    case 4:
        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        edad = int(input("Ingrese su edad: "))
        fechadenacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmarcontrasena = input("Confirme su contraseña: ")
    case 5:
        print ("Hasta luego")
    case _:
        print ("Opción no válida")    