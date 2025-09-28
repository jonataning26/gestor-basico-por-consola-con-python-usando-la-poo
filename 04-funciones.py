# tema de funciones en python argumento y parametros y valores de retornos


#palabra clave return de retorno 
"""def sumar(n1,n2,n3):
    resultado_implicito= n1 * n2 + n3
    return resultado_implicito

respuesta = sumar(1,2,3)
tipo = type(respuesta)
print(tipo)
"""
#parametros con valores por defecto.
"""
def saludar(nombre , idioma ="Español"):
    print (f"mucho gusto {nombre} veo que tu idioma nativo es el {idioma}")
saludar("ana")

"""
#ejercicio practico de programacion calculado.

#solucion 1:

"""
def calculado(a,b):
   if (isinstance(a,(int,float))) and (isinstance(b,(int,float))):
       if a >= b:
            return a
       else:
            return b
   else:
       print("error de tipo!!!")
       return False
   
quien_es_mayor = calculado(4,3.4)
TIPO= type(quien_es_mayor)
if type(quien_es_mayor) != bool:
    print("EL NUMERO MAYOR ES EL: "+str(quien_es_mayor)+" EL CUAL ES DE TIPO "+str(TIPO))
"""

TEXTO_MENU_DE_OPERACIONES= """
\t\t BIENVENIDO A MINI CALCULADORA DE OPERACIONES
*************************************************************************
OPCION 1: SUMA                                                          *
OPCION 2: RESTA                                                         *
OPCION 3: MULTIPLICACION                                                *
OPCION 4: DIVISION                                                      *    
OPCION 5: POTENCIACION                                                  *
*************************************************************************
"""
print(TEXTO_MENU_DE_OPERACIONES)
ENTRADA_DE_OPCION = int(input("QUE OPERACION DESEA REALIZAR: "))
print("***********************************************************")
def mini_calculadora(OPCION_ELEGIDA):
    if (isinstance (ENTRADA_DE_OPCION,(int)) <= 5):
       if OPCION_ELEGIDA == 1:
           nun1 = float(input("INGRESE EL PRIMER VALOR A SUMAR:"))
           nun2 = float(input("INGRESE EL SEGUNDO VALOR A SUMAR:"))
           print("SU OPERACION SE REALIZO CON EXITO")
           return nun1 + nun2
       elif OPCION_ELEGIDA == 2:
           nun1 = float(input("INGRESE LA CANTIDAD QUE DESEA USAR PARA RESTAR:"))
           nun2 = float(input("INGRESE LA CANTIDAD QUE DESEA RESTAR:"))
           print("SU OPERACION SE REALIZO CON EXITO")
           return nun1 - nun2
       elif OPCION_ELEGIDA == 3:
           nun1 = float(input("INGRESE EL VALOR QUE DESEA MULTIPLICAR:"))
           nun2 = float(input("INGRESE SU VALOR MULTIPLICADOR:"))
           print("SU OPERACION SE REALIZO CON EXITO")
           return nun1 * nun2
       elif OPCION_ELEGIDA == 4:
           
           nun1 = float(input("INGRESE EL PRIMER VALOR QUE DESEA DIVIDIR:"))
           nun2 = float(input("INGRESE EL VALOR POR EL CUAL DESEA DIVIDIRLO:"))
           if nun2 == 0:
               print("MATH ERROR NO SE PUEDE DIVIDIR ENTRE CERO")
               return False
           else:
              print("SU OPERACION SE REALIZO CON EXITO")
              return nun1 / nun2
       elif OPCION_ELEGIDA == 5:
           nun1 = float(input("INGRESE LA BASE DE SU POTENCIA:"))
           nun2 = float(input("INGRESE EL EXPONENTE DE SU POTENCIA:"))
           print("SU OPERACION SE REALIZO CON EXITO")
           return nun1 ** nun2
       else:
        print(F"OPCION {OPCION_ELEGIDA} INVALIDA ")
        return False
MOSTRA =mini_calculadora(ENTRADA_DE_OPCION)
if type(MOSTRA) != bool and ENTRADA_DE_OPCION <= 5:
    print(F"EL RESULTADO LA OPCION {ENTRADA_DE_OPCION} ES: "+ str(MOSTRA))
else:
    print("ERROR DE TIPO DESCONOCIDO")