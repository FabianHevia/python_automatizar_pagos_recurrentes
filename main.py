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

# print(calendario)

'''

Y si ingresaramos datos de varios clientes en un Json?

La idea es generar el calendario de cuotas mensuales para cada cliente y combinar
todo en un solo calendario ordenado por fecha más reciente.

'''

from datetime import date, timedelta

#  Sumamos los meses a una fecha simple
def add_months(orig_date: date, months: int) -> date:
    year = orig_date.year + (orig_date.month - 1 + months) // 12
    month = (orig_date.month - 1 + months) % 12 + 1
    day = orig_date.day
    # Ajuste simple para evitar días inválidos (p.ej. 31 feb -> último día válido del mes)
    # Buscamos el último día válido del mes objetivo:

    for d in range(day, 0, -1):

        try:

            return date(year, month, d)
        
        except ValueError:

            continue

    return date(year, month, 1)

# Datos del JSON
clientes = {
    "cliente1": {"nombre": "Ana Pérez", "monto": 150000, "cuotas": 3, "fecha_inicial": "2025-09-15"},
    "cliente2": {"nombre": "Luis Gómez", "monto": 90000,  "cuotas": 4, "fecha_inicial": "2025-08-01"},
    "cliente3": {"nombre": "María Ruiz", "monto": 200000, "cuotas": 5, "fecha_inicial": "2025-10-05"},
}

# Generamos todas las cuotas por cada cliente
pagos = []


for cid, info in clientes.items():

    nombre = info["nombre"]
    monto = float(info["monto"])
    cuotas = int(info["cuotas"])
    fecha_inicial = date.fromisoformat(info["fecha_inicial"])

    cuota_base = round(monto / cuotas, 2)
    suma_excepto_ultima = cuota_base * (cuotas - 1)
    ultima_cuota = round(monto - suma_excepto_ultima, 2)

    for i in range(cuotas):

        fecha_pago = add_months(fecha_inicial, i)
        numero = i + 1
        monto_pago = cuota_base if i < cuotas - 1 else ultima_cuota

        pagos.append({
            "fecha": fecha_pago,
            "cliente_id": cid,
            "cliente": nombre,
            "monto": monto_pago,
            "nro_cuota": numero,
            "total_cuotas": cuotas
        })

# Ordenamos por fecha más reciente
pagos_ordenados = sorted(pagos, key=lambda p: p["fecha"], reverse=True)

for p in pagos_ordenados:
    print(f"{p['fecha'].isoformat()} | {p['cliente']} | cuota {p['nro_cuota']}/{p['total_cuotas']} | ${p['monto']:,.2f}")

