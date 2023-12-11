# producto1 = {"nombre": "donut", "precio_de_venta":1.5, "aceptacion_publico":True}
# lista_nombres = ["anna", "pep", "eva", "sara","iker"]

# #  Sintaxis del bucle for en Python:

# for nombre in lista_nombres: #para cada nombre que esta en la lista pues voy hacer ....
#     print(f"¡ hola {nombre} !")    #imprimir
#     print(f"¡ hola {nombre.title()} !")

# bucle while, "mientras"
# esta_lloviendo = True

# while esta_lloviendo:           #mientras esta lloviendo
#     print("Llevare abierto el paraguas")        #pues muestro esto

#Hay que parar el bucle hay 2 maneras: poniendo un contador
esta_lloviendo = True
while esta_lloviendo:           
    print("Llevare abierto el paraguas")
    llueve = input("sigue lloviendo? S/N --->")
    if llueve.upper() == "N":
        esta_lloviendo = False
print("Ya no llueve")        
