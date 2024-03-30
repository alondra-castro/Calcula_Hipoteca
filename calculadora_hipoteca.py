# Función para calcular la cuota mensual de una hipoteca
def calcular_cuota_mensual(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo):
    # Calcular el monto del préstamo
    monto_prestamo = valor_propiedad - abono_inicial

    # Aplicar un ajuste en la tasa de interés según si la propiedad es nueva o vieja
    if nuevo:
        tasa_interes -= 0.5  # Reducción de la tasa para propiedades nuevas

    # Calcular la tasa de interés mensual
    tasa_interes_mensual = tasa_interes / 12 / 100

    # Calcular el número de cuotas mensuales
    numero_cuotas = anos_financiamiento * 12

    # Calcular la cuota mensual
    cuota_mensual = monto_prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** numero_cuotas) / ((1 + tasa_interes_mensual) ** numero_cuotas - 1)

    return cuota_mensual

# Función para calcular el historial de pagos
def calcular_historial_de_pagos(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo):
    cuota_mensual = calcular_cuota_mensual(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo)

    historial_pagos = []
    saldo_pendiente = valor_propiedad - abono_inicial

    for mes in range(1, anos_financiamiento * 12 + 1):
        interes_mensual = saldo_pendiente * tasa_interes / 12 / 100
        principal_mensual = cuota_mensual - interes_mensual
        saldo_pendiente -= principal_mensual

        historial_pagos.append((mes, cuota_mensual, interes_mensual, principal_mensual, saldo_pendiente))

    return historial_pagos

# Ejemplo de uso
valor_propiedad = 200000  # Valor de la propiedad en dólares
tasa_interes = 4.5  # Tasa de interés anual en porcentaje
anos_financiamiento = 30  # Número de años de financiamiento
abono_inicial = 40000  # Abono inicial en dólares
nuevo = True  # True si la propiedad es nueva, False si es vieja

cuota_mensual = calcular_cuota_mensual(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo)
print(f"Cuota mensual: ${cuota_mensual:.2f}")

historial_pagos = calcular_historial_de_pagos(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo)

print("Historial de pagos:")
print("Mes\tCuota\tInterés\tPrincipal\tSaldo Pendiente")
for mes, cuota, interes, principal, saldo in historial_pagos:
    print(f"{mes}\t${cuota:.2f}\t${interes:.2f}\t${principal:.2f}\t${saldo:.2f}")
