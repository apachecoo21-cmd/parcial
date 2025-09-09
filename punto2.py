
total_a_pagar = 0

# Pedir al usuario los precios de tres productos
for i in range(3):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    descuento = 10  # Porcentaje de descuento
    descuento_aplicado = precio * descuento / 100 # Calcular el descuento
    precio_final = precio - descuento_aplicado # Calcular el precio final después del descuento


    # Mostrar el precio final de este producto
    print(f"El precio final del producto {i+1} después del descuento es: {precio_final:.2f}")

    # Acumular el precio final al total a pagar
    total_a_pagar += precio_final

# Mostrar el total a pagar
print(f"\nEl total a pagar por los tres productos es: {total_a_pagar:.2f}")
