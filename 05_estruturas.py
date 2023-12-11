# Estructura diccionario, se reconoce por {}
alumno_1 = {"nombre": "Bill", "apellido" : "Gates", "ciudad": "Seattle"}
alumno_2 = {"nombre": "Steve", "apellido" : "Jobs", "ciudad": "Cupertino", "direccion":"x", "nif":"1234"}
alumno_2["nombre"] = "Paco" #cambio el nombre del alumno

print(alumno_2)

# Tupla: otra estructura, se reconoce por los parentesis, es inmutable, es decir, 
# no se pueden modificar los valores ya creados. Va mas rápido que una lista
tupla = ("Ana",16,"Python")
print(tupla) #todo
print(tupla[1]) #un campo
#para cambiar un valor
tupla = list(tupla)  #lo paso a lista
tupla[0] = "Sara"   #cambio el valor
tupla = tuple(tupla) # lo vuelvo a pasar a tupla
print(tupla)


# Otra estructura es el conjunto, en ingles set. Es una estructura que no permite repeticiones
lista = ["Ana P","Paco J", "Ana P", "Josep M", "Paco P"]
conjunto = set(lista)
print(conjunto)

