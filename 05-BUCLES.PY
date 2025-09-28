#ejercicio practico de bucles

# bulce for
"""
archivos = ["trabajo.pdf","trabajo.xlxs","trabajo3.pdf","trabajo4.doc"]
print(F"PROCESANDO LA LISTA DE ARCHIVOS{archivos}")
for tipo in archivos:   
    if tipo[-4:] == ".pdf":
        print(f"documento:{tipo}")
    elif tipo[-5:] == ".xlxs":
        print(f"documento:{tipo}")
    elif tipo[-4:] == ".doc":
        print(f"documento:{tipo}")
"""

#imprimir vocales
"""
frase = input("ingrese una frase:").lower()
for vocal in frase:
    if vocal in ["a","e","i","o","u"]:
        print(f"{vocal} es una vocal.")
    else:
        print(f"{vocal} es una consonante")
"""


while True:
    ingresar = input("INGRESE UNA FRASE:").lower()
    for i in ingresar:
        if i in ["a"]:
            print(f"{i} en contrada")
            break
        else:
            print("NO SE ENCONTRARON LETRAS "+"A")

    
