#creamos la clase cuenta bancaria:
def obtener_fondos(mensaje):
    while True:
        try:
            entrada = float(input(mensaje))
            if entrada >= 0 :
                return entrada
            else:
                print("error has intentado ingresar un numero menor a 0 vuelve a intentarlo")
        except ValueError:
            print("error tipo de dato invalido vuelve a intentarlo!!!")
class cuentabancaria:
    def __init__(self,numero_de_cuenta,titular,saldo=0):
        self.nro = numero_de_cuenta
        self.dueño = titular
        self.fondo=saldo
    # metodos de una cuenta de banco...
    def datos_de_cuenta_actual(self):
        mostrador = f"""
*********************************
CUENTA DE:{self.dueño}
*********************************
--------------------------------
NUMERO DE CUENTA: {self.nro}

SALDO ACTUAL: {self.fondo}$
--------------------------------
                    """
        print(mostrador)

    def depositar(self,cantidad):
        self.fondo += cantidad
        
    def retirar(self,cantidad):
        if self.fondo >= cantidad:
            self.fondo -= cantidad
            return True            
        else:
            print("SALDO INSUFICIENTE!!! HAGA UN DEPOSITO")
            return False
    def transferir(self,otra_cuenta,cantidad):
        if self.retirar(cantidad):
            print("TRANSFERENCIA REALIZADA EXITOSAMENTE!!!")
            otra_cuenta.depositar(cantidad)
        else:
            print("ERROR NO SE PUDO REALIZAR LA TRANSFERENCIA")

#cuentas actuales
CUENTA1 = cuentabancaria("01020334","JONATAN CHIRINO",500)
CUENTA2 = cuentabancaria("01050000","YEISI ARIAS")
CUENTA1.datos_de_cuenta_actual()
CUENTA2.datos_de_cuenta_actual()
CUENTA1.transferir(CUENTA2,obtener_fondos("CUANTO DESEA TRANSFERIR DE SU CUENTA:"))
CUENTA2.datos_de_cuenta_actual()
