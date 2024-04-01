def pedir_contraseña():
    while True:
        contraseña = input("Por favor, ingrese la contraseña: ")
        if contraseña == "1234":
            print("¡Bienvenido!")
            break
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo.")

pedir_contraseña()
