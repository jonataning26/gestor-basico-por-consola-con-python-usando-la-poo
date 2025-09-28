#entradas de datos por teclado
"""
edad = input("Ingresar su edad porfavor:")
print(f"Tu edad es: {edad}")
"""
#identificar los tipos de datos ingresados funcion type

"""edad = type(edad)
print(edad)
"""
#boleanos IF
"""
verdadero = True
falso= False

if verdadero == True:
    print(f"el valor de la variable es {verdadero}")

if falso == False:
    print(f"no se cumple la condicion")

"""
#ejercicio practico:
"""
edad = int(input("CUAL ES TU EDAD:"))

if edad <= 17 and edad != 0:
    print(f"TIENES {edad} POR LO TANTO ERES MENOR DE EDAD Y NO PUEDES PASAR.")
elif edad > 18:
    print(f"TIENES {edad} ERES MAYOR DE EDAD POR LO TANTO PUEDES PASAR.")
elif edad == 0:
    print(f"haz ingresado {edad} y es incorrecto para obtener el acceso.")"""

#operadores logicos and or y not
"""
segundo = 7850
horas = segundo // 3600
print("el equipo tardo:",str(horas),"hrs")
segundo2 = segundo % 3600
minutos = segundo2 // 60
segundo3 = segundo2 % 60
print(f"minutos que se demoro {minutos}","min")
print(f"segundos despues de minutos:{segundo3 }","Seg")
if segundo %2 == 0:
    print(f"el numero total de segundo {segundo} es un numero par")
else:
    print(f"la cantidad de segundo {segundo}es impar ")"""


#ejercicio propuesto
TEXTO_DE_ENTRADA="""
OPCION 1:PENDIENTE
OPCION 2:  PROCESO
OPCPION 3: COMPLETADA
OPCION 4: FALLIDA
"""
print(TEXTO_DE_ENTRADA)
estado_de_tarea = int(input("INGRESE UN NUMERO DE OPCION:"))

if estado_de_tarea == 1:
    print("LA TAREA ESTA PENDIENTE RECUERDA TERMINARLA INICIARLA TIEMPO.")
elif estado_de_tarea == 2:
    print("EXCELENTE TRABAJO, LA TAREA ESTA EN PROCESO")
elif estado_de_tarea == 3:
    print("TAREA COMPLETADA EXITOSAMENTE")
elif estado_de_tarea == 4: # Esta sería la nueva opción para "fallida"
    print("La tarea ha FALLADO.")
    # Aquí es donde pedimos el código de error para el escenario de fallo
    codigo_error = int(input("Ingrese el código de error (0 si no hay específico): "))
    if codigo_error == 0:
        print("No se encontró un código de error específico para el fallo.")
    else:
        print(f"Código de error: {codigo_error}. ¡Investigar la causa del fallo!")


else:
    print(f"CODIGO_ERROR {estado_de_tarea} !!! ESTADO DE TAREA DESCONOCIDO VERIFICA TU VALOR DE ENTRADA.")
    