def lineas():
    return "************"
##############################
def elegir():
    while True:
        try:
             ELECCION = int(input("INGRESE UN NUMERO DE OPCION:"))
             if ELECCION in [1,2,3,4,5,6]:
                break
             elif ELECCION < 1:
                print("ERROR LA OPCION NO PUEDE SER UN NUMERO NEGATIVO!!!")
             else:
                print("==> OPCION INVALIDA <==")
        except ValueError:
            print("TIPO DE DATO INVALIDA")
    return ELECCION
######################
def menuP(): 
    print(lineas())
    titulo = "SISTEMA DE INVENTARIO"
    ancho = 60
    centrado = titulo.center(ancho,"/")
    print(centrado)
    print(lineas())
    linea2= "********"
    menu = f"""
    {linea2}  
    OPCION 1:  AGREGAR PRODUCTO
    OPCION 2:  VER INVENTARIO
    OPCION 3:  BUSCAR UN PRODUCTO
    OPCION 4:  ELIMINAR PRODUCTO
    OPCION 5:  MODIFICAR INVENTARIO
    OPCION 6:  SALIR DEL SISTEMA
    {linea2}
    """
    print(menu)
    ELECCION = elegir()
    return ELECCION
##############################
def agregarp(inventario):
    print(lineas())
    titu ="AGREGAR PRODUCTOS"
    ancho = 60
    centrar = titu.center(ancho,"/")
    print(centrar)
    print(lineas(),"\n")
    while True:
        producto = input("NOMBRE DEL PRODUCTO:")
        if not producto.isdigit() and producto.strip():           
            if not producto in inventario:
                break
            else:
                print(f"{producto} YA EXISTE EN INVENTARIO, SI DESEA CAMBIARLO OH MODIFICARLO DIRIJASE A LA OPCION 5.!!!")
        else:
            print("TIPO DE DATO INVALIDO EL CAMPO NOMBRE NO ADMITE ESPACIO EN BLANCO NI NUMEROS.!!")

    while True:   
        try: 
            cantidad= float(input("CANTIDAD DEL PRODUCTO:"))
            if cantidad > 0:
                print(f" {producto} SE AGREGO EXITOSAMENTE CON UNA CANTIDAD DE {cantidad}")
                break
            else:
                print("LA CANTIDAD A INGRESAR NO DEBE SER UN NUMERO NEGATIVO MENOR A 0.")
        except ValueError:
            print("ERROR EL SISTEMA NO ADMITE SIMBOLOS ESPECIALES.")
    inventario[producto]= cantidad 
##############################
def mostrarin(mostrar):
    print(lineas())
    titu ="INVENTARIO ACTUAL"
    ancho = 60
    centrar = titu.center(ancho,"/")
    print(centrar)
    print(lineas(),"\n")
    TEXTO = """ PRODUCTOS  | CANTIDAD  """
    if mostrar:
        print(TEXTO)
        for PRODUCTO, CANTIDAD in mostrar.items():
            print(f" {PRODUCTO:<10} | {CANTIDAD:<10}")
        print("\n\n")
    else:
        cen ="VACIO\n\n"
        ancho = 60
        centrar = cen.center(ancho)
        print(centrar)
##############################
def busqueda(buscar):
    print(lineas())
    titu ="BUSCAR ELEMENTOS"
    ancho = 60
    centrar = titu.center(ancho,"/")
    print(centrar)
    print(lineas(),"\n")
    TEXTO = """ PRODUCTOS  | CANTIDAD  """
    Buscar = input("QUE PRODUCTO BUSCA:")
    if Buscar in buscar:
       print(TEXTO)
       print( f"{Buscar:<10}  | {buscar[Buscar]:>10}")
    else:
        print(lineas())
        titu ="\n\nNO SE ENCONTRARON ELEMENTOS\n\n"
        ancho = 60
        centrar = titu.center(ancho,"/")
        print(centrar)
        print(lineas(),"\n")
##############################
def eliminar(Del):
    print(lineas())
    titu ="ELIMINAR ELEMENTOS"
    ancho = 60
    centrar = titu.center(ancho,"/")
    print(centrar)
    print(lineas(),"\n")
    TEXTO = """ PRODUCTOS  | CANTIDAD  """
    Buscar = input("QUE PRODUCTO BUSCA PARA ELIMINAR:")
    if Buscar in Del:
       print(TEXTO)
       print( f"{Buscar:<10}  | {Del[Buscar]:>10}")
       eliminar = input(f"DESEA ELIMINAR {Buscar} DEL INVENTARIO:").lower()
       if eliminar in ["si"]:
           del  Del[Buscar]
           print("ELEMENTO ELIMINADO EXITOSAMENTE\n\n")
    else:
       print("NO SE ENCONTRARON ELEMENTOS")
##############################
def modificacion(modificar):
    print(lineas())
    titu ="MODIFICAR ELEMENTOS"
    ancho = 60
    centrar = titu.center(ancho,"/")
    print(centrar)
    print(lineas(),"\n")
    while True:
        buscar = input("NOMBRE DEL PRODUCTO AH MODIFICAR:").lower()
        if not buscar.isdigit() and buscar.strip():
            if buscar in modificar:
                TEXTO = """ PRODUCTOS  | CANTIDAD  """
                print (TEXTO)
                print(f"{buscar:<10}  | {modificar[buscar]:>10}")
                CAMBIO = input("DESEA MODIFICAR LA CANTIDAD:").lower()
                if CAMBIO in ["si","s","y","yes"]:
                    while True:
                        try: 
                            cantidad= float(input("CANTIDAD DEL PRODUCTO:"))
                            if cantidad > 0:
                                modificar[buscar]= cantidad
                                print(f"LA CANTIDAD FUE MODIFICADA EXITOSAMENTE\n\n")
                                return
                            
                            else:
                                print("LA CANTIDAD A INGRESAR NO DEBE SER UN NUMERO NEGATIVO MENOR A 0.")
                        except ValueError:
                            print("ERROR EL SISTEMA NO ADMITE SIMBOLOS ESPECIALES.")

                else:
                    print("SE CANCELO LA MODIFICACION")
                    break
            else:
                print(F"ERROR {buscar} no se encuentra en inventario")
        else:
            print("TIPO DE DATO INVALIDO EL CAMPO NOMBRE NO ADMITE ESPACIO EN BLANCO NI NUMEROS.!!")

       
        
    
##############################     
#LOGICA PRINCIPAL
inventarioAC={"mango": 400}
while True:
    opcion = menuP()
    if opcion == 1:
        agregarp(inventarioAC)
        
        while True:
            AgregarM = input ("DESEA AGREGAR OTRO PRODUCTO:").lower()
            if AgregarM in ["si","s","y","yes","otro","mas"]:
                agregarp(inventarioAC)
            elif AgregarM in ["no","n","not"]:
                break
            else:
                print("OPCION INVALIDA!!!")
                continue
    elif opcion == 2:
        mostrarin(inventarioAC)
            
    elif opcion == 3:
        busqueda(inventarioAC)
    elif opcion == 4:
        eliminar(inventarioAC)
    elif opcion == 5:
        modificacion(inventarioAC)
    elif opcion == 6:
        print("SE CERRO EL SISTEMA DE MANERA EXITO.")
        break