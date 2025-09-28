def crear_perfil(nombre,apellido= "Chirino",**kwargs):
    nuevo ={}
    nuevo["nombre"]= nombre
    nuevo["apellido"]= apellido
    for clave , valor in kwargs.items():
        nuevo[clave]=valor
    return nuevo   
datos=crear_perfil ("jonatan",ciudad = "caracas",edad=26,genero="masculino",nacion="Venezuela")
print(datos)

