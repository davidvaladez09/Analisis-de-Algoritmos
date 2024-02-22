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
# subcadenas = [cadena_modificada[i:i+5] for i in range(0, len(cadena_modificada), 2) if i+5 <= len(cadena_modificada)]
subcadenas = [cadena[i:i+5] for i in range(0, len(cadena), 2) if i+5 <= len(cadena)]


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
print("\nSubcadenas de 5 caracteres:")
print(subcadenas)


ultima_cadena_modificada = cadenas_modificadas[-1]

# Ultimo elemento de las cadenas modificadas
print("\nUltima Cadena modificada:")
print(ultima_cadena_modificada)

subcadenas_modificadas = [ultima_cadena_modificada[i:i+5] for i in range(0, len(ultima_cadena_modificada), 2) if i+5 <= len(ultima_cadena_modificada)]
print("\nSubcadenas modificadas:")
print(subcadenas_modificadas)

print('\nCadenas con cambios')
for i in range(len(subcadenas)):
    if subcadenas[i] != subcadenas_modificadas[i]:
        print(subcadenas_modificadas[i])

print('\n')


if subcadenas_modificadas:
    for i, (subcadena_modificada, subcadena_original) in enumerate(zip(subcadenas_modificadas, subcadenas)):
        if subcadena_original != subcadena_modificada:
            print(f"La subcadena {i+1} '{subcadena_original}' fue modificada a '{subcadena_modificada}'")
        else:
            print(f"La subcadena {i+1} no fue modificada.")
else:
    print("No hay subcadenas modificadas para comparar.")

print('\n')

# Función para imprimir los cambios de manera ordenada
def imprimir_cambios(cambios):
    for cambio in cambios:
        print(cambio)

print('\n')

# Lista para almacenar los cambios en cada subcadena modificada
recorrido_cambios_subcadenas = []

for subcadena_modificada, subcadena_original in zip(subcadenas_modificadas, subcadenas):
    cambios_subcadena = [subcadena_original]

    # Verificar si la subcadena tuvo más de un cambio
    cantidad_cambios = sum(1 for a, b in zip(subcadena_modificada, subcadena_original) if a != b)
    if cantidad_cambios > 1:
        for i in range(len(subcadena_modificada)):
            if subcadena_modificada[i] != subcadena_original[i]:
                cambios_subcadena.append(subcadena_modificada[:i+1])
    recorrido_cambios_subcadenas.append(cambios_subcadena)

# Imprimir el recorrido de todos los cambios en cada subcadena modificada
for i, cambios_subcadena in enumerate(recorrido_cambios_subcadenas):
    if len(cambios_subcadena) > 1:
        print(f"Recorrido de todos los cambios en la subcadena {i + 1}:")
        imprimir_cambios(cambios_subcadena)
    else:
        print(f"La subcadena {i + 1} no tuvo más de un cambio.")

