import numpy as np

def resolver_ayuda(tablero):
    
    nfilas_tablero = len(tablero)
    nfilas = nfilas_tablero * nfilas_tablero
    matriz_Lights_Out = matriz_toggle_tablero(tablero)
    entradas = entradas_tablero(tablero)
    entradas = entradas.transpose()
    entradas.resize(nfilas, 1)
    aumentado = np.hstack((matriz_Lights_Out, entradas))

    for fila in range(nfilas - 1):
        if aumentado[fila, fila] == 0:
            fila_no_cero = np.argmax(aumentado[fila + 1 :, fila])
            aumentado[[fila, fila_no_cero + fila + 1]] = aumentado[[fila_no_cero + fila + 1, fila]]

        for i in range(fila + 1, nfilas):
            if aumentado[i, fila] == 1:
                aumentado[i] = (aumentado[i] + aumentado[fila]) % 2

    for columna in range(nfilas - 1, 0, -1):
        for i in range(columna - 1, -1, -1):
            if aumentado[i, columna] == 1:
                aumentado[i] = (aumentado[i] + aumentado[columna]) % 2

    respuesta = aumentado[:, -1]
    respuesta = respuesta.reshape((nfilas_tablero, nfilas_tablero))
    return respuesta

def matriz_toggle_tablero(tablero):
    nfilas_tablero = len(tablero)
    nrows = nfilas_tablero * nfilas_tablero
    matriz_toggle = np.zeros((nrows, nrows), dtype=int)
    for i in range(nrows):
        for j in range(nrows):
            if i == j:
                matriz_toggle[i, j] = 1
            elif (i // nfilas_tablero == j // nfilas_tablero and abs(i - j) == 1) or (
                i % nfilas_tablero == j % nfilas_tablero and abs(i - j) == nfilas_tablero
            ):
                matriz_toggle[i, j] = 1
    return matriz_toggle

def entradas_tablero(tablero):
    return np.array(tablero).flatten()

# Ejemplo de uso
print(resolver_ayuda(np.array([[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1]])))

