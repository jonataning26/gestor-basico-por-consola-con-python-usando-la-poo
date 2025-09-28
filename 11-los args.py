#METODO *ARGS.
def calculo_de_promedio(*args):

    notas =sum(args)
    cantidades = len(args)
    return notas/ cantidades


print("tu promedio es:"+str(calculo_de_promedio(12,16,16,17,19)))




