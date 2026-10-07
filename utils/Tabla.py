from typing import cast

from numpy import arange
from pandas import DataFrame, Series
from utils.Calculos import calcular_tasa
from utils.Formatos import formato_espanol
from utils.Trm import dolar


def actualizar_tabla_amortizacion(monto : float, cuotas : int, tasa : float) -> list:
    tabla = []
    saldo_pendiente = monto
    
    # En el sistema alemán, el abono a capital es estrictamente FIJO todos los meses
    capital_mes = monto / cuotas
    
    # Convertimos la tasa a decimal (asumiendo que llega como porcentaje, ej: 2.13)
    tasa_mensual = calcular_tasa(tasa)

    for mes in range(1, cuotas + 1):
        # El interés se calcula sobre el saldo pendiente actual
        interes_mes = saldo_pendiente * tasa_mensual
        
        # La cuota TOTAL cambia cada mes: es la suma del capital fijo + interés decreciente
        cuota_mes = capital_mes + interes_mes
        
        # Restamos el capital fijo del saldo pendiente
        saldo_pendiente -= capital_mes

        # Guardar registro
        tabla.append({
            "mes": mes,
            "cuota": round(cuota_mes, 2),
            "capital": round(capital_mes, 2),
            "intereses": round(interes_mes, 2),
            "saldo": max(0.0, round(saldo_pendiente, 2))
        })

    return tabla

def formatear_tabla_amortizacion (tabla : dict, operacion_tarjeta: str) -> tuple[DataFrame,DataFrame]:
    df_original = DataFrame(tabla)
    df_original.set_index('mes', inplace=True)
    df_original.columns = df_original.columns.str.title()

    if operacion_tarjeta == "Compra internacional":
        for col in df_original.columns:
            df_original[col+'_COP'] = round(df_original[col] * dolar,2)

    df_formateado = cast(DataFrame, df_original.map(formato_espanol))

    return df_original, df_formateado

def mostrar_detalles (tabla : DataFrame | Series) :
    deciles = arange(0.1, 1.1, 0.1)

    detalles = cast(Series, (
        tabla
        .drop(columns=["Capital"])
        .describe(percentiles=deciles)
        .map(formato_espanol)
    ))

    detalles = detalles.drop(["min", "max","count"])

    print(detalles)