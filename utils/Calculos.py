def calcular_cuota(tasa_mensual : float, monto : float, cuotas : int) -> float:
    cuota : float

    # Calcular la cuota mensual fija
    if tasa_mensual == 0:
        cuota = monto / cuotas
    else:
        cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** cuotas) / (((1 + tasa_mensual) ** cuotas) - 1)

    return cuota

def calcular_tasa(tasa : float, tasa_anual: bool = False) -> float:
    tasa_mensual : float

     # Convertir la tasa a formato decimal y mensual
    if tasa_anual:
        tasa_decimal_anual = tasa / 100
        tasa_mensual = (1 + tasa_decimal_anual) ** (1 / 12) - 1
    else:
        tasa_mensual = tasa / 100

    return tasa_mensual
