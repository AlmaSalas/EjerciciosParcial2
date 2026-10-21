nombre = "Alma" #aqui va la variable para tu nombre
edad = 17 #aqui va la variable para tu edad
estatura = 1.63 #aqui va la variable para tu estatura
colorfavorito = "morado" #aqui va la variable para tu color favorito

# aqui una forma de pedir los datos al usuario y guardarlos enlas variables correspondientes 
print ("ingrese su nombre")
nombre = input()
print ("ingrese su edad")
edad = int(input())
print ("ingrese su estatura")
estatura = float(input())
print ("ingrese su color favorito")
colorfavorito = input()
print ("Hola, mi nombre es " + nombre + ", tengo " + str(edad) + " años, mido " + str(estatura) + " metros y mi color favorito es " + colorfavorito)
