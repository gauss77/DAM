#imports
import random

# constantes
NUMERO_FILAS = 5
NUMERO_COLUMNAS = 5
MINA = '*'
CASILLA_INCOGNITO = '.'
CASILLA_LIBRE = '_'
FACTOR_MINAS = 0.1 # factor 10%
TOTAL_MINAS = int(FACTOR_MINAS * (NUMERO_FILAS * NUMERO_COLUMNAS))


# Crear variables
tablero = list()
tablero_de_minas = list()
input_fila = 0
input_columna = 0
continuar = True
pierdes = False
ganas = False
casillas_abiertas = 0


# definición de funciones
def generar_posicio_aleatoria():
    pos = list()
    pos.append(random.randint(0, NUMERO_FILAS - 1))
    pos.append(random.randint(0, NUMERO_COLUMNAS - 1))

    return pos

def inicializar_tablero():
    """
    Función que inicializa el tablero de juego
    :return: None
    """
    global tablero
    global NUMERO_COLUMNAS
    global NUMERO_FILAS
    global CASILLA_INCOGNITO

    tablero.append([' '])
    for _ in range(1, NUMERO_FILAS + 1):
        tablero.append(list())

    for fila in range(0, NUMERO_FILAS + 1):
        for columna in range(0, NUMERO_COLUMNAS + 1):
            if fila == 0:
                if columna > 0:
                    tablero[fila].append(str(columna))
            else:
                tablero[fila].append(str(fila) if columna == 0 else CASILLA_INCOGNITO)



def imprimir_tablero():
    """
    Función imprime por pantalla el tablero de minas
    :return: None
    """
    global tablero

    for fila in tablero:
        for columna in fila:
            print(columna, end = ' ')

        print()

def leer_datos_usuario():
    global input_fila
    global input_columna
    global NUMERO_FILAS
    global NUMERO_COLUMNAS

    input_fila = int(input("Introduce un valor de fila: "))
    input_columna = int(input("Introduce un valor de columna: "))

    return (0 < input_fila < NUMERO_FILAS + 1) and (0 < input_columna < NUMERO_COLUMNAS + 1)

def generar_minas():
    global tablero_de_minas
    global NUMERO_FILAS
    global NUMERO_COLUMNAS
    global CASILLA_INCOGNITO
    global MINA

    for _ in range(0, NUMERO_FILAS):
        tablero_de_minas.append([CASILLA_INCOGNITO] * NUMERO_COLUMNAS)

    # incrustar minas en el tablero de minas
    total = 0
    while (total < TOTAL_MINAS):
        posicion = generar_posicio_aleatoria()

        if tablero_de_minas[posicion[0]][posicion[1]] == MINA:
            # si la posición ya contiene una mina
            # generar una posición aleatoria nueva
            continue
        else:
            tablero_de_minas[posicion[0]][posicion[1]] = MINA

        total = total + 1


def procesar_entrada():
    global input_fila
    global input_columna
    global tablero
    global tablero_de_minas
    global CASILLA_LIBRE
    global MINA
    global ganas
    global pierdes
    global casillas_abiertas
    global NUMERO_FILAS
    global NUMERO_COLUMNAS

    if tablero_de_minas[input_fila - 1][input_columna - 1] != MINA:
        tablero[input_fila][input_columna] = CASILLA_LIBRE
        casillas_abiertas = casillas_abiertas + 1

        # ganamos si se han abierto todas las casillas que no contienen minas
        if casillas_abiertas == NUMERO_FILAS * NUMERO_COLUMNAS:
            ganas = True
    else:
        tablero[input_fila][input_columna] = MINA
        pierdes = True


# Este bloque se ejecuta cuando se invoca este módulo
# directamente (no cuando se importa)
if __name__ == '__main__':
    # Inicializar juego
    inicializar_tablero()
    generar_minas()
    imprimir_tablero()


    # Ejecutar Juego
    while continuar:

        if leer_datos_usuario():
            # si las posiciones introducidas son correctas
            # proceder con el juego, sino, volver a pedir
            procesar_entrada()
            imprimir_tablero()
        else:
            print('La posición introducida no es válida. Vuelve a introducir una posicón, por favor.')

        if pierdes or ganas:
            continuar = False

    if pierdes:
        print('¡Lástima! Has perdido.')

    if ganas:
        print('¡Felicidades! Has ganado la partida.')