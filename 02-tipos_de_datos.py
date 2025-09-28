"""Ejercicio 1: Calculadora de Costos de Automatización Simple

Imagina que estás automatizando un proceso donde se descargan "paquetes" de datos, 
y cada paquete tiene un costo base y un costo adicional por cada megabyte (MB) descargado.

Tu tarea es:

Define una variable costo_base_paquete (por ejemplo, 50.00).

Define una variable costo_por_mb (por ejemplo, 0.15).

Define una variable mb_descargados (por ejemplo, 150).

Calcula el costo_total sumando el costo_base_paquete y el producto de costo_por_mb por 
mb_descargados.

Imprime el costo_total de una manera legible, por ejemplo: "El costo total
 de la descarga es: [valor del costo total]"."""


"""costo_base = 50.00
costo_por_mb = 0.15
descargado = 150

costo_total= costo_por_mb * descargado + costo_base

print("EL COSTO TOTAL ES:",str(costo_total))

"""
#ejercicio 2 generador de reportes 

activo =False

if activo:
    MENSAJE ="GENERAR ESTA ACTIVO"
else:
    MENSAJE = "GENERADOR ESTA INACTIVO"


print(f"EL {MENSAJE} ")
