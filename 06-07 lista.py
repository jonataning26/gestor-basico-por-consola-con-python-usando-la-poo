def text():
    texto = "La Ingeniería de Sistemas es una disciplina integral que diseña, desarrolla y gestiona sistemas complejos para optimizar la eficiencia y resolver problemas en diversas organizaciones, combinando conocimientos de informática, matemáticas y otras ciencias para crear soluciones innovadoras mediante el uso de hardware, software, procesos y datos. Su enfoque holístico asegura que todos los componentes del sistema funcionen de manera coordinada y eficaz, permitiendo la automatización, la mejora de la calidad de vida y la transformación digital de la sociedad.".upper()
    return texto

def buscador(txt):
    palabras =[]
    while True:
        buscar = input("INGRESE LA FRASE QUE DESEA BUSCAR:").upper()
        if buscar.strip() and not buscar.isdigit():

            if buscar in txt:
                print("SE CONTRO LA PALABRA Y SE AGREGO A LA LISTA DE MANERA EXITOSA")
                if buscar not in palabras:
                    palabras.append(buscar)
                    salir =input("quiere buscar otra palabra:").upper()
                    if salir in ["si","s","y","yes"]:
                        print("se salio del sistema!!!")
                    else:
                        print("GENIAL BUSQUEMOS OTRA PALABRA!!!")
                        continue
                else:
                    print("no se encontraron palabras")
                    salir =input("quiere buscar otra palabra:").upper()
                    if salir in ["si","s","y","yes"]:
                        print("se salio del sistema!!!")
                    else:
                        print("GENIAL BUSQUEMOS OTRA PALABRA!!!")
                        continue

            else:
                print("YA LA PALABRA SE ENCUENTRA EN LA LISTA!!!")
                continue
                
        else:
            print("error el campo no puede contener espacios en blanco ni numeros!!!")
    return palabras



palabra = buscador(text())