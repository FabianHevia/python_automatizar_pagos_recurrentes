'''

Dado un monto inicial y una lista de fechas, 
genera un calendario de pagos con montos iguales.

'''

monto = 50000
fechas = ["2025-01-10", "2025-02-10", "2025-03-10"]

# El monto se divide en cuantas fechas de pago existen con un mismo monto
pago = monto / len(fechas)

'''

Entonces se crea un calendario el cual es capaz de según cada fecha en fechas,
asignar una fecha y un monto a cada pago redondeando en dos decimales.

'''
calendario = [{ "fecha": f, "monto": round(pago, 2) } for f in fechas]

print(calendario)