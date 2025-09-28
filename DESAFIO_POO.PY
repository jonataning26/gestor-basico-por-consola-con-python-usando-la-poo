#SCRIP DE BANCO BASICO USANDO LA PROGRAMACION ORIENTADA A OBJETOS
def opcion(mensaje):
    while True:
        try:
            entrada1 = int(input(mensaje))
            if entrada1 in [1, 2, 3, 4, 5]:
                return entrada1
            else:
                print("Número de operación no existe")
        except ValueError:
            print("Tipo de dato inválido!!!")

def cantidad(mensajes):
    while True:
        try:
            entrada2 = float(input(mensajes))
            if entrada2 >= 0:
                return entrada2
            else:
                print("Error: La cantidad no debe ser menor a 0")
        except ValueError:
            print("Tipo de dato inválido!!!")

# CLASE DEL SCRIPT OH EL CEREBRO DEL NEGOCIO!!!
class cuentabancaria:
    def __init__(self, cuenta, titular, saldo=0):
        self.nro = cuenta
        self.titular = titular
        self.saldo = saldo

    def mostrar(self):
        print("•" * 60)
        print("BANCA MOVIL".center(60))
        print(f"NRO DE CUENTA: {self.nro}".center(60))
        print(f"TITULAR:{self.titular}".center(60))
        print(f"SALDO:{self.saldo}$".center(60))
        print("•" * 60)

    def depositar(self, cantidad): #METODO UNO DEPOSITAR
        self.saldo += cantidad
        print("DEPÓSITO REALIZADO EXITOSAMENTE")

    def retirar(self, cantidad): #RETIRAR
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print("RETIRO REALIZADO EXITOSAMENTE")
            return True
        else:
            print("SALDO INSUFICIENTE")
            return False

    def transferencia(self, otra_cuenta, cantidad):# AQUI ESTE METODO PERMITE QUE LOS OBJETOS SE COMUNIQUE ENTRE SI
    
        if self.retirar(cantidad):
            otra_cuenta.depositar(cantidad)
            print("\n¡Transferencia realizada con éxito!")
        else:
            print("\nTransferencia fallida: Saldo insuficiente en tu cuenta.")


def mostrar_cuentas_actuales(cuentas): 
    print("\n--- CUENTAS ACTUALES ---")
    for cuenta in cuentas:
        cuenta.mostrar()
    print("-------------------------")

#MENU DE OPCIONES DE OPERACION MANEJO DEL NEGOCIO
def operaciones(cuenta1, cuenta2):
    cuentas = [cuenta1, cuenta2]  #AQUI SE AÑADEN A UNA LISTA LOS OBJETOS CREADOS Y SON FILTRADOS POR LA FUNCION Y EL METODO .MOSTRAR()
    while True:
        print("-" * 40)
        menu = """ 
                  MENU DE OPCION DE OPERACIÓN
OPCION - 1) DEPOSITAR
OPCION - 2) RETIRAR
OPCION - 3) TRANSFERIR
OPCION - 4) CUENTAS ACTUALES
OPCION - 5) SALIR
"""
        print(menu)
        eleccion = opcion("INGRESE EL NUMERO DE LA OPERACIÓN:")
        print("-" * 40)

        if eleccion == 1:
            monto = cantidad("CUANTO DESEA DEPOSITAR:")
            cuenta1.depositar(monto)
            cuenta1.mostrar()
        elif eleccion == 2:
            monto = cantidad("CUANTO DESEAS RETIRAR:")
            cuenta1.retirar(monto)
            cuenta1.mostrar()
        elif eleccion == 3:
            monto_transferir = cantidad("INGRESE EL MONTO A TRANSFERIR:")
            cuenta1.transferencia(cuenta2, monto_transferir)
            print("\n--- Estado de las cuentas después de la transferencia ---")
            cuenta1.mostrar()
            cuenta2.mostrar()
        elif eleccion == 4:
            mostrar_cuentas_actuales(cuentas)  
        elif eleccion == 5:
            print("SISTEMA CERRADO")
            break

#AQUI ESTA LOS METODO CREADOS APARTIR DE LA CLASE CUENTABANCARIA:
cuenta1 = cuentabancaria("010210002000", "Jonatan Chirino", 500)
cuenta2 = cuentabancaria("010510002000", "Yeisi Arias", 500)

operaciones(cuenta1, cuenta2)

#VAMOS A DARLE UNA PROBADA AL CODIGO!!!