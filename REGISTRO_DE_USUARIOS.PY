#MINI PROYECTO SISTEMA DE REGISTRO DE USUARIOS 1.0

def CREAR_USUARIOS():
    ACCESO = True
    while ACCESO:
        NOMBRE_USER =input("INGRESE UN NOMBRE PARA SU USUARIO: ")
        CONTRASEÑA = input("INGRESE UNA CONTRASEÑA CON 8 O MAS DIGITOS: ")
        CONFIRMACION = input("VUELVA A INGRESAR SU CONTRASEÑA PARA CONFIRMAR: ")
###############################################################################################
################### =========> VALIDACION DE DATOS <===========################################
        if len(NOMBRE_USER) <= 0:
            print("ERROR EL CAMPO NOMBRE NO PUEDE ESTAR VACIO!!!")
            continue
        elif len(CONTRASEÑA) <= 7:
            print("ERROR LA CONTRASEÑA NO PUEDE TENER MENOS DE 8 DIGITOS!!!")
            continue
        elif len(CONFIRMACION) != len(CONTRASEÑA):           
            print("ERROR LAS CONTRASEÑAS NO COINCIDEN")
            continue
        if CONTRASEÑA != CONFIRMACION:
            print("ERROR LAS CONTRASEÑAS NO COINCIDEN")
            continue
        print ("USUARIO CREADO EXITOSAMENTE!!!")
        return [NOMBRE_USER,CONTRASEÑA]
###############################################################################################

LISTA_USUARIOS = []
while True:
    crear_mas =input("desea crear un usuario s/n: ").lower()
    if crear_mas == "si" or crear_mas == "s":
        nuevo = CREAR_USUARIOS()
        LISTA_USUARIOS.append(nuevo)
    else:
        print("CIERRE DE SECION DE MANERA EXITOSA!!!")
        break
for MOSTRAR in LISTA_USUARIOS:
    print(F"USUARIO: {MOSTRAR[0]} CONTRASEÑA: {MOSTRAR[1]}")