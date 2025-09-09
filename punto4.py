
try:
    # Pedir al usuario dos números enteros
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    
    # calcular la división
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
    
# Manejar el error si el usuario ingresa algo que no sea un número entero
except ValueError:
    print("Error: Debe ingresar números enteros.") 
    
# error si el usuario intenta dividir entre cero
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
