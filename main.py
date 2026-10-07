from utils import Menu, Tabla, Trm

TASA_ANUAL = 28.7548
TASA_MENSUAL = 2.1285

Trm.get_trm()

monto =  int(input("Credito:"))

operaciones = {
    "Compra" : 0,
    "Avance" : 24,
    "Compra internacional" : 36
}

operacion, cuotas = Menu.menu(operaciones)

print(f"\nOperación seleccionada: {operacion}")

tabla = Tabla.actualizar_tabla_amortizacion(monto, cuotas, TASA_MENSUAL)

tabla_original, tabla_formateada = Tabla.formatear_tabla_amortizacion(tabla, operacion)

print(tabla_formateada)

Tabla.mostrar_detalles(tabla_original)