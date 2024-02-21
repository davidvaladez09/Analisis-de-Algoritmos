# Leer la cadena
cadena = input("Ingrese la cadena: ")

# Solicitar al usuario la posición a cambiar
posicion = int(input("Ingrese la posición que desea cambiar (0-" + str(len(cadena)-1) + "): "))

# Solicitar al usuario el nuevo carácter
nuevo_caracter = input("Ingrese el nuevo carácter: ")

# Cambiar la posición en la cadena
cadena_modificada = cadena[:posicion] + nuevo_caracter + cadena[posicion + 1:]

# Crear una lista de todas las cadenas modificadas
cadenas_modificadas = [cadena_modificada]

# Recorrer la cadena de dos en dos posiciones y generar subcadenas de 5 caracteres
subcadenas_modificadas = [cadena_modificada[i:i+5] for i in range(0, len(cadena_modificada), 2) if i+5 <= len(cadena_modificada)]

# Realizar modificaciones a la cadena principal
while True:
    # Solicitar al usuario la posición a cambiar
    posicion = int(input("Ingrese la posición que desea cambiar (0-" + str(len(cadena)-1) + "), o ingrese -1 para terminar: "))
    
    # Verificar si el usuario quiere terminar
    if posicion == -1:
        break
    
    # Solicitar al usuario el nuevo carácter
    nuevo_caracter = input("Ingrese el nuevo carácter: ")
    
    # Cambiar la posición en la cadena
    cadena = cadena[:posicion] + nuevo_caracter + cadena[posicion + 1:]
    
    # Agregar la cadena modificada a la lista de cadenas modificadas
    cadenas_modificadas.append(cadena)

# Imprimir todas las cadenas modificadas
print("\nTodas las cadenas modificadas:")
for i, cadena_modificada in enumerate(cadenas_modificadas):
    print(f"Cadena {i+1}: {cadena_modificada}")

# Ingresar las subcadenas a una lista e imprimir la lista
print("Subcadenas de 5 caracteres:")
print(subcadenas_modificadas)

# Comparar subcadenas modificadas con cadenas modificadas y mostrar las subcadenas que han sido modificadas
print("\nSubcadenas modificadas:")
for subcadena_modificada, cadena_modificada in zip(subcadenas_modificadas, cadenas_modificadas):
    if subcadena_modificada != cadena_modificada:
        print(subcadena_modificada)
