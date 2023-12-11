alumno_1 = {"nombre": "bill", "apellido" : "GAtes", "ciudad": "Seattle"}
alumno_2 = {"nombre": "Steve", "apellido" : "JobS", "ciudad": "Cupertino"}
alumno_2["nombre"] = "Paco"

lista_alumnos = [
{"nombre": "Elon", "apellido" : "mUsk", "ciudad": "Los Angeles"},
{"nombre": "donald", "apellido" : "truMp"}
]

lista_alumnos.append(alumno_1) #con append puedo ayudar mas valores a la lista
lista_alumnos.append(alumno_2)


# Para crear una funcion la llamamos con def
def gestion_alumnos():
    for alumno in lista_alumnos:
        alumno["nombre"] = alumno["nombre"].title()
        alumno["apellido"] = alumno["apellido"].title()

# para utilizarla, hay que llamarla
gestion_alumnos()
print(lista_alumnos)
