#funcion para saber si un numero es primo 
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#ingresar el numero que sea entero y positivo 
numero = int(input("Ingrese un número entero positivo: "))
contador_primos = 0
#funcion que nos muestra los numeros primos menores o iguales al numero ingresado
print("Números primos menores o iguales a", numero, ":")
for i in range(2, numero + 1):
    if es_primo(i):
        print(i)
        contador_primos += 1
#mostrar la cantidad de numeros primos encontrados
print("Cantidad de números primos encontrados:", contador_primos)


