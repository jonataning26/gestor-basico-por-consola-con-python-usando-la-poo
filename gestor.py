class Tarea:
    def __init__(self, nombre):

        self.nombre = nombre

        self.estado = "pendiente"


class gestortarea:

    def __init__(self):

        self.Lista = []

    def agregar(self,nombre):

        while True:

            try:

                if nombre.strip():

                    nuevaT = Tarea(nombre)

                    self.Lista.append(nuevaT)

                    print("La tarea se agregó de manera exitosa")

                    return


                else:   

                    print("ERROR: TIPO DE DATO INVÁLIDA VERIFICA QUE EL CAMPO NOMBRE NO CONTENGA DÍGITOS OH ESTE VACÍO...")


            except ValueError:

                pass

    def mostrar(self):

        if len(self.Lista) > 0:

            contador = 0

            for tarea in self.Lista:

                contador += 1

                print(f"tarea {contador}: {tarea.nombre} en estado:{tarea.estado}")

        else:

            print ("LISTA DE TAREAS VACÍA!!!")



tareas = gestortarea()

while True:

    tareas.agregar(str(input("INGRESE SU TAREA AQUI:")))

    salir= input("Desea agregar más:")

    if salir in ["si","s"]:

        continue

    else:

        print(" saliendo del gestor !!!")

        break
print("LISTA ACTUAL:")
tareas.mostrar()