import random

def generar_numeros_aleatorios():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    return numero1, numero2

def pedir_suma():
    while True:
        try:
            respuesta = int(input("Por favor, ingrese la suma de los dos números: "))
            return respuesta
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")


numero1, numero2 = generar_numeros_aleatorios()


suma_correcta = numero1 + numero2


while True:
    suma_usuario = pedir_suma()
    if suma_usuario == suma_correcta:
        print("¡Respuesta correcta! La suma de", numero1, "y", numero2, "es igual a", suma_correcta)
        break
    else:
        print("Respuesta incorrecta. Inténtelo de nuevo.")

