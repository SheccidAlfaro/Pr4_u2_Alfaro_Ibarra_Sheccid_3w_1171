print("")
print("Alfaro barra Sheccid, Traduccion de palabras, Ingles-Español.")
#Definir diccionario
palsnie={
    "Hola" : "Hello",
    "adios" : "Goodbye",
    "Buenas tardes" : "Good afternoon",
    "Buenos dias" : "Good morning",
    "Por favor" : "Please",
    "Gracias" : "Thanks"

}
#Se pregunta al usuario 
print(palsnie)
print("")
pleesp=input("Ingresa una palabra en español: ")
#Utilizar if paratener una respuesta
if pleesp in palsnie:
    print ("Esto significa: ",palsnie[pleesp])
else:
    print("Esa palbra no esta en el diccionario")
