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

# Crear una lista de las modificaciones en las subcadenas
modificaciones_subcadenas = []

# Verificar modificaciones en las subcadenas
for subcadena_modificada in subcadenas_modificadas:
    modificaciones = []
    for i in range(len(subcadena_modificada)):
        if subcadena_modificada[i] != cadena_modificada[i]:
            modificaciones.append((i, subcadena_modificada[i]))
    modificaciones_subcadenas.append(modificaciones)

# Imprimir las listas de modificaciones en las subcadenas
print("\nModificaciones en las subcadenas:")
for i, modificaciones in enumerate(modificaciones_subcadenas):
    print(f"Subcadena {i+1}: {modificaciones}")
