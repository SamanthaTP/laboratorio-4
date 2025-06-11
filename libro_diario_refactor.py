class LibroDiario:
    ''' Esta clase almacena los datos de transacciones, calcula ingreso y egreso '''
    def __init__(self):
        ''' Es el constructor de la clase '''
        self.transacciones = []

    def agregar(self, fecha, descripcion, monto, tipo):
        ''' esta funcion almacena los datos de la transaccion'''

        self.transacciones.append({
          "fecha": fecha,
          "descripcion": descripcion,
          "monto": monto,
          "tipo": tipo
        })

    def resumen(self):
        ''' esta funcion calcula el total de ingresos y egresos'''
        ingresos = 0
        egresos = 0
        for t in self.transacciones:
            if t["tipo"] == "ingreso":
                ingresos += t["monto"]
            else:
                egresos += t["monto"]
        return "Total ingresos: " + str(ingresos) + " Total egresos: " + str(egresos)
