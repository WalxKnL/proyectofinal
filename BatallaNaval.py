import random

def crearTablero (dimension):
    return [["~" for _ in range(dimension)]for _ in range(dimension)] 

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("\n Tablero de disparos: ")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\n Tablero de disparos del oponente: ")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))
        
def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado= False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocado {barco ['nombre']} de tamaño {barco['dimension']}")
                fila= int(input("Ingrese la fila: "))
                columna= int(input("Ingrese la columna: "))
                orientacion= input("Ingrese la orientacion (h para horizontal, v para vertical): "). lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice('h', 'v')
            if validarColocacion(tablero, fila, columna, barco ['dimension'], orientacion):
                colocarBarcos(tablero, fila, columna, barco ['dimension'], orientacion)
                colocado= True
            elif jugador == "jugador":
                print("Colocacion es invalida. Intenta de nuevo")
                
def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension> len(tablero):
            return False
        for i in range(dimension):
            if tablero [fila][columna+1] != "~":
                return False
        else:
            if fila + dimension> len(tablero):
                return False
            for i in range(dimension):
                if tablero[fila+i][columna] != "~":
                    return False
    return True

def colocarBarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero [fila][columna+i]="B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna]="B"
            
def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] =="X"
        tableroOculto[fila][columna] =="H"
        return "impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroOculto[fila][columna] == "O"
        return "Agua"
    return "Ya disparaste aqui"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True

def jugarContraComputadora():
    dimension =5
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tablerosDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre":"portaviones", "dimension":3},
        {"nombre":"submarino", "dimension":2}
    ]
    print("coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputadora, barcos, "computadora")
    turnoJugador=True
    while True:
        if turnoJugador:
            print("\nTu turno")
            mostrarTableros(tableroDisparosJugador, tablerosDisparosComputadora)
            fila = int(input("ingresa la fila del disparo: "))
            columna = int(input("ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("ganaste")
                return "jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosJugador, tablerosDisparosComputadora, fila, columna)
            print(f"la computadora disparo en 8({fila}, {columna}): {resultado}")
            if verificarVictoria(tableroJugador):
                print("la computadora gano ")
                return "computadora"
    turnoJugador = not turnoJugador

def jugarDosJugadores():
    dimension =5
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroDisparosJugador1 = crearTablero(dimension)
    tablerosDisparosJugador2 = crearTablero(dimension)
    barcos = [
        {"nombre":"portaviones", "dimension":3},
        {"nombre":"submarino", "dimension":2}
    ]
    print("Jugador 1 coloca tus barcos")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 coloca tus barcos")
    colocarBarcos(tableroJugador2, barcos, "computadora")
    turnoJugador1=True
    while True:
        if turnoJugador1:
            print("\nTu turno")
            mostrarTableros(tableroDisparosJugador1, tablerosDisparosJugador2)
            fila = int(input("ingresa la fila del disparo: "))
            columna = int(input("ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("jugador 1 Gano")
                return "jugador 1"
        else:
            print("\n Turno del jugador 2")
            mostrarTableros(tablerosDisparosJugador2, tableroDisparosJugador1)
            fila = int(input("ingresa la fila del disparo: "))
            columna = int(input("ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador1, tablerosDisparosJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("Jugador 2 Gano ")
                return "Jugador 2"   
    turnoJugador1 = not turnoJugador1
            
                
                
                
                   
                
        