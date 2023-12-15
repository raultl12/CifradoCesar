# Diccionarios
dict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
    'Z': 25, ' ': 26, '0': 27, '1': 28, '2': 29,
    '3': 30, '4': 31, '5': 32, '6': 33, '7': 34,
    '8': 35, '9': 36
}

numCh = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
    25: 'Z', 26: ' ', 27: '0', 28: '1', 29: '2',
    30: '3', 31: '4', 32: '5', 33: '6', 34: '7',
    35: '8', 36: '9'
}

# Funcion cifradoCesar: Cifra un mensaje con el algoritmo de Cifrado Cesar
# Parametros de entrada: mensaje (str), desplazamiento (int)
# Salida: mensajeCifrado (str)
def cifradoCesar(mensaje, desplazamiento):
    mensajeCifrado = ""
    # Convertir el mensaje a mayusculas
    mensaje = mensaje.upper()
    # Recorrer el mensaje y cifrar usando el diccionario
    for ch in mensaje:
        if ch in dict:
            pos = dict[ch]
            pos = (pos + desplazamiento) % len(dict)
            mensajeCifrado += numCh[pos]
        else:
            mensajeCifrado += ch
    return mensajeCifrado

# Funcion descifradoCesar: Descifra un mensaje con el algoritmo de Cifrado Cesar
# Parametros de entrada: mensaje (str), desplazamiento (int)
# Salida: mensajeDescifrado (str)
def descifradoCesar(mensaje, desplazamiento):
    mensajeDescifrado = ""
    # Convertir el mensaje a mayusculas
    mensaje = mensaje.upper()
    # Recorrer el mensaje y descifrar usando el diccionario
    for ch in mensaje:
        if ch in dict:
            pos = dict[ch]
            pos = (pos - desplazamiento) % len(dict)
            mensajeDescifrado += numCh[pos]
        else:
            mensajeDescifrado += ch
    return mensajeDescifrado

# Funcion main: Funcion principal del programa
# Parametros de entrada: Ninguno
# Salida: Ninguno
def main():
    mensaje = input("Ingrese el mensaje a cifrar: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    mensajeCifrado = cifradoCesar(mensaje, desplazamiento)
    print("Mensaje cifrado: " + mensajeCifrado)
    mensajeDescifrado = descifradoCesar(mensajeCifrado, desplazamiento)
    print("Mensaje descifrado: " + mensajeDescifrado)

# Llamado a la funcion main
main()
