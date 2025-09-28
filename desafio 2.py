cliente1 = {"id": "1", "nombre": "Ana"}
cliente2 = {"id": "2", "nombre": "Pedro", "ciudad": "Madrid"}
cliente3 = {"id": "3", "nombre": "Maria"}
cliente4 = {"id": "1", "email": "ana.lopez@email.com", "telefono": "555-1234"}
cliente5 = {"id": "2", "profesion": "Arquitecto"}

def crear_perfil(*datos_clientes):
    nuevo ={}
    for id in datos_clientes:
        clave = id["id"]
        if clave in datos_clientes:
            nuevo[clave]+=id
        else:
            nuevo[clave]=id
    return nuevo
datos=crear_perfil (cliente1,cliente2,cliente3,cliente4,cliente5)
print(datos)

