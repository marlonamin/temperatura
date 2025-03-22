# Función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento según el monto total y porcentaje.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
    float: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamada 1: Solo con el monto total, usando el descuento por defecto (10%)
monto_1 = 150.0
descuento_1 = calcular_descuento(monto_1)
total_1 = monto_1 - descuento_1

# Llamada 2: Con monto total y un descuento personalizado
monto_2 = 300.0
descuento_2 = calcular_descuento(monto_2,20)  # 20% de descuento
total_2 = monto_2 - descuento_2

# Mostrar los resultados
print("---- Resultado 1 ----")
print(f"Monto original: ${monto_1}")
print(f"Descuento aplicado (10%): ${descuento_1}")
print(f"Total a pagar: ${total_1}")

print("\n---- Resultado 2 ----")
print(f"Monto original: ${monto_2}")
print(f"Descuento aplicado (20%): ${descuento_2}")
print(f"Total a pagar: ${total_2}")
