print("")
print("Alfaro Ibarra Sheccid, 3w, 1171. Completar datos.")
#Preguntar al usuario
nm=input("Ingrese su nombre: ")
#Crear diccionario para llenar
dicdinf={
    "Nombre": [],
    "Edad" : [],
    "Apellidos" : [],
    "Sexo" : [],
    "Telefono" : [],
    "Correo" : [],
}
#Actualizar diccionario
dicdinf.update({"Nombre" : nm})
#Variable y mostrar en pantalla
x= dicdinf["Nombre"]

print("Su nombre es: ", x)

print("")
#Preguntar al usuario
apmp=input("Ingrese sus apellidos: ")
#Actualizar diccionario
dicdinf.update({"Apellidos" : apmp})
#Variable y mostrar en pantalla
z=dicdinf["Apellidos"]

print("Sus apellidos son: ", z)

print("")
#Preguntar al usuario
ed=input("Ingrese su edad: ")
#Actualizar diccionario
dicdinf.update({"Edad" : ed})
#Variable y mostrar en pantalla
c=dicdinf["Edad"]

print("Su edad es: ", c)
print("")
#Preguntar al usuario
sx=input("Ingrese su sexo: ")
#Actualizar diccionario
dicdinf.update({"Sexo" : sx})
#Variable y mostrar en pantalla
y=dicdinf["Sexo"]

print("Es:", y)
print("")
#Preguntar al usuario
tl=input("Ingrese su numero de telefono: ")
#Actualizar diccionario
dicdinf.update({"Telefono" : tl})
#Variable y mostrar en pantalla
a=dicdinf["Telefono"]

print("Su numero es: ", a)
print("")
#Preguntar al usuario
correl=input("Ingrese su correo electronico: ")
#Actualizar diccionario
dicdinf.update({"Correo" : correl})
#Variable y mostrar en pantalla
b=dicdinf["Correo"]

print("Correo Electronico: ", b)
print("")
#Mostrar diccionario 
print(dicdinf)