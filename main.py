monto = 50000
fechas = ["2025-01-10", "2025-02-10", "2025-03-10"]

pago = monto / len(fechas)
calendario = [{ "fecha": f, "monto": round(pago, 2) } for f in fechas]

print(calendario)
