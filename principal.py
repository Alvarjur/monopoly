import random
def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 
    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

def moverJugador (jugador,posicionActual):

    dado1, dado2, totalDado = tirarDados()
    print(f"Ha salido {dado1} y {dado2}, en total te mueves {totalDado} casillas")

    nuevaPosicion = (posicionActual + totalDado) % len(calles)

    if nuevaPosicion < posicionActual:
        print(f"El jugador {jugador}, ha pasado por la casilla y recibe 200€")
        jugadores[jugador]["Diners"] += 200
    
    print(f"El jugador {jugador} se mueve a {calles[nuevaPosicion]['Nombre']}")
    #Aqui se podría añadir si el jugador cae en una casilla de suerte (if jugador in calles[casilla de la suerte])
    #Que salga una carta al azar de las de suerte
    #También si la casilla en la que recae no esta comprada por otro propietario ofrecer comprarlas
    #Si es de otro jugador cuanto de alquiler tiene que pagar
    return nuevaPosicion

def mostrarInformacion (jugador):
    for jugador, info in jugadores.items():
        print(f"Jugador {jugador.capitalize()}:")
        print(f"Carrers: {info['Carrers']}")
        print(f"Diners: {info['Diners']}")
        print(f"Carta Especial: {info['Carta Especial']}")
        print("")

def inicioPartida():
    global jugadores
    listaJugadores = []

    for key in jugadores:
        listaJugadores.append(key)
    random.shuffle(listaJugadores)

    inicialesJugadores = []

    for jugadores in listaJugadores:
        if jugadores == "groc":
            inicialesJugadores.append("G")
        elif jugadores == "vermell":
            inicialesJugadores.append("V")
        elif jugadores == "blau":
            inicialesJugadores.append("B")
        elif jugadores == "taronja":
            inicialesJugadores.append("T")

    calles[12]['Ocupacion'].extend(inicialesJugadores) #calles[12] es la casilla de salida
    #Verificar que establezca correctamente el orden y que inicialmente esten bien colocados
    return None


def imprimir_tablero(calles):
    # Tablero inicial con posiciones que serán llenadas por los nombres de las calles

    tablero = [
        [calles[0]["Nombre"], calles[1]["Nombre"], calles[2]["Nombre"], calles[3]["Nombre"], calles[4]["Nombre"], calles[5]["Nombre"], calles[6]["Nombre"]],
        [calles[23]["Nombre"], "", "", "", "", "",calles[7]["Nombre"]],
        [calles[22]["Nombre"], "", "", "", "", "",calles[8]["Nombre"]],
        [calles[21]["Nombre"], "", "", "", "", "",calles[9]["Nombre"]],
        [calles[20]["Nombre"], "", "", "", "", "",calles[10]["Nombre"]],
        [calles[19]["Nombre"], "", "", "", "", "",calles[11]["Nombre"]],
        [calles[18]["Nombre"], calles[17]["Nombre"], calles[16]["Nombre"], calles[15]["Nombre"], calles[14]["Nombre"], calles[13]["Nombre"], calles[12]["Nombre"]],
    ]

    # Definir el tamaño de las casillas
    ancho_casilla = 12 #Solo funciona si es 12
    alto_casilla = 2 #No funciona bien si este valor no es 1 o 2.
    
    # Función auxiliar para crear bordes horizontales
    def crear_borde_horizontal(cantidad, fila): #Esta función se usa dentro del bucle for para crear las líneas horizontales
        if fila[0] != "" and fila[1] == "": #Si el primer valor del array de la iteración del bucle no es "" y el segundo valor es "", quiere decir que es uno de los arrays
                                            #que tiene que dejar huecos en medio
                                            
            if tablero.index(fila) <= len(tablero) -3: #Si el index de la fila (que es cada iteracion del bucle for), es menor o igual que la cantidad de arrays en tablero
                if tablero.index(fila) == len(tablero) - 3:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[2].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 4:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[5].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 5:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[8].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 6:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[11].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                
        return "+" + ("-" * ancho_casilla + "+") * cantidad
    

    # Función auxiliar para crear contenido de una fila
    def crear_fila_contenido(fila):
        resultado = ""
        barra = "|"
        iteracion = 0

        for elemento in fila:
            if elemento == "":
                elemento = " " * ancho_casilla  # Espacio vacío si no hay casilla
            else:
                elemento = elemento.ljust(ancho_casilla)  # Poner el nombre a la izquierda de la casilla
                if iteracion == 0:
                    nuevaString = elemento[:-1] + " |"
                else:
                    nuevaString = elemento[:-1] + "|"
                elemento = nuevaString
                elemento = nuevaString
            if fila[0] and fila[1] == "":
                resultado += barra #la barra se añade al principio, aunque luego igualmente es reemplazada por otra barra igual, pero si no estuviera se reemplazarían letras o espacios,
                                    #por lo que no cerraría bien el cuadrado
                if barra != "":     #Sí la variable barra no está vacía (ya que después en esta misma iteracion se vacía para que solo se use una vez en todo el bucle)
                    resultado += elemento + "".ljust(0)
                    
                else:
                    if elemento.replace(" ", "") != "":
                        if fila.index(elemento[:-1].replace(" ","")) <= len(fila) -1: #elemento[:-1].replace(" ","") es porque elemento sin modificaciones es "ejemplo           |", así que
                                                                                        #no lo encontraría en el array de fila al no coincidir con ninguno de los valores
                            resultado += "| " + elemento

                barra = ""
            else:
                resultado += " " + elemento
                
            iteracion += 1
                     
        nuevoEl = "|" + resultado[1:] #Esto lo que hace es una vez este el texto completo, reemplaza el primer valor del string con "|", para cerrar la caja.
        resultado = nuevoEl  


        
        return resultado
    
    # Imprimir la parte superior del tablero
    print(crear_borde_horizontal(len(tablero[0]), ["a", "a", "a"])) #Aquí el ["a", "a", "a"] es porque la funcion requiere un array como parámetro, pero no hace nada con el en esta ocasión
    
    # Imprimir las filas con contenido
    iteracion = 0
    histIt = 13
    for fila in tablero:
        
        for _ in range(alto_casilla):  # Altura de cada casilla (varias líneas por fila)
            if _ == 0:  # Contenido en la línea de arriba de la casilla
                if tablero.index(fila) >= 1 and tablero.index(fila) < 6:
                    txt = crear_fila_contenido(fila)
                    lineaSeparada = txt.split("|")
                    lineaSeparada[2] = historial[histIt]
                    histIt -= 3
                    lineaJunta = f"|" + f"{lineaSeparada[1]}" + "| " f"{lineaSeparada[2]}".ljust(65) + "|" + f"{lineaSeparada[3]}".ljust(12) + "|"
                    print(lineaJunta)
                else:
                    print(crear_fila_contenido(fila))
            else:  # Líneas vacías para la altura

                if iteracion == 0 or iteracion == 6:  #Según la iteracion del bucle for, añade barras verticales y la ocupacion de cada calle para la iteracion 0 y 6, es decir la primera y la última
                    if iteracion == 0:
                        txt = f"|" + f"".join(calles[0]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[1]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[2]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[3]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[4]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[5]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[6]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 6:
                        txt = f"|" + f"".join(calles[18]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[17]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[16]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[15]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[14]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[13]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[12]['Ocupacion']).ljust(12) + f"|"
                    print(txt)
                    
                else:
                    if iteracion == 1:
                        txt = f"|" + f"".join(calles[23]['Ocupacion']).ljust(12) + f"| " + f"{historial[12]}".ljust(63) + f"|" + f"".join(calles[7]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 2:
                        txt = f"|" + f"".join(calles[22]['Ocupacion']).ljust(12) + f"| " + f"{historial[9]}".ljust(63) + f"|" + f"".join(calles[8]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 3:
                        txt = f"|" + f"".join(calles[21]['Ocupacion']).ljust(12) + f"| " + f"{historial[6]}".ljust(63) + f"|" + f"".join(calles[9]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 4:
                        txt = f"|" + f"".join(calles[20]['Ocupacion']).ljust(12) + f"| " + f"{historial[3]}".ljust(63) + f"|" + f"".join(calles[10]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 5:
                        txt = f"|" + f"".join(calles[19]['Ocupacion']).ljust(12) + f"| " + f"{historial[0]}".ljust(63) + f"|" + f"".join(calles[11]['Ocupacion']).ljust(12) + f"|"
                    
                    print(txt)
                iteracion += 1
        print(crear_borde_horizontal(len(fila), fila))  # Bordes inferiores de cada fila


calles = [
    {"Nombre": "Parking", "Casilla":0, "Ocupacion": [],},         
    {"Nombre": "Urquinoa", "Casilla":1, "Ocupacion": []},        
    {"Nombre": "Fontan", "Casilla":2,"Ocupacion": []},         
    {"Nombre": "Sort", "Casilla":3,"Ocupacion": []},            
    {"Nombre": "Rambles", "Casilla":4, "Ocupacion": []},         
    {"Nombre": "Pl.Cat", "Casilla":5,"Ocupacion": []},          
    {"Nombre": "Anr pró", "Casilla":6,"Ocupacion": []},         
    {"Nombre": "Angel", "Casilla":7,"Ocupacion": []},           
    {"Nombre": "Augusta", "Casilla":8, "Ocupacion": []},         
    {"Nombre": "Caixa", "Casilla":9,"Ocupacion": []},          
    {"Nombre": "Balmes", "Casilla":10, "Ocupacion": []},          
    {"Nombre": "Gracia", "Casilla":11,"Ocupacion": []},          
    {"Nombre": "Sortida", "Casilla":12,"Ocupacion": []},         
    {"Nombre": "Lauria", "Casilla":13,"Ocupacion": []},          
    {"Nombre": "Rosell", "Casilla":14, "Ocupacion": []},          
    {"Nombre": "Sort2", "Casilla":15,"Ocupacion": []},           
    {"Nombre": "Marina", "Casilla":16,"Ocupacion": []},          
    {"Nombre": "Consell", "Casilla":17,"Ocupacion": []},         
    {"Nombre": "Presó", "Casilla":18,"Ocupacion": []},           
    {"Nombre": "Muntan", "Casilla":19, "Ocupacion": []},          
    {"Nombre": "Aribau", "Casilla":20,"Ocupacion": []},          
    {"Nombre": "Caixa2", "Casilla":21,"Ocupacion": []},          
    {"Nombre": "S.Joan", "Casilla":22,"Ocupacion": []},          
    {"Nombre": "Aragó", "Casilla":23, "Ocupacion": []}            
]#Podriamos guardar la ocupacion en el diccionario Jugadores (?) y asignar el calle["Nombre"] a "Jugadores[jugador]["Posició"]"

jugadores = {
    "blau":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "Cartas especials": [],
        "Diners":2000,
        "Carta salir de la prisión":False,
        "Esta en prisión":False,
        "Turnos en prisión":0
    },
    "groc":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "Cartas especials": [],
        "Diners":2000,
        "Carta salir de la prisión":False,
        "Esta en prisión":False,
        "Turnos en prisión":0
    },
    "taronja":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "Cartas especials": [],
        "Diners":2000,
        "Carta salir de la prisión":False,
        "Esta en prisión":False,
        "Turnos en prisión":0
    },
    "vermell":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "Cartas especials": [],
        "Diners":2000,
        "Carta salir de la prisión":False,#Nos dice si tiene la carta de salir prisión o no para despues poder usarla
        "Esta en prisión":False,#Estos nos dice si esta en prisión o no
        "Turnos en prisión":0 #Como dice el nombre cuantos turnos lleva en prisión
    }
}

# Mi idea con el historial es que siempre tenga este número de valores, aunque estén vacíos y parezca que no haya nada (""), porque en el caso de que se borren valores dará error
# al intentar buscar el valor en el index 13 por ejemplo y esté fuera del rango del array
#Se podria inicializar en historial en historial = "" e ir actualizandolo ?

historial = [
    "1.  Ejemplo alguien hace algo",
    "2.  Pasa esto",
    "3.  ABCD",
    "4.  Compra una casa",
    "5.  Vende una propiedad",
    "6.  Ha pasado por la salida",
    "7.  A Vermell no se le ocurren ejemplos",
    "8.  Ejemplo",
    "9.  Hola",
    "10. que",
    "11. Vermell compra un hotel",
    "12. Blau ha ganado 2000€",
    "13. Groc ha entrado en la prisión",
    "14. Taronja hace algo no se me ocurren más ejemplos"
]

inicioPartida()
imprimir_tablero(calles)

#Hay varios problemas con este tablero, el primero es que seguramente al poner qué jugador está en X casilla, toda la linea se moverá, desencajando el tablero, #SOLUCIONADO
#El segundo problema es que el hueco del medio no está "vacio", simplemente son espacios en blanco así que no sabría cómo hacer que saliera el historial por ahí. #Solucionado????
#El tercer problema es que es un código muy complicado y ni yo sé del todo por qué funciona bien, así que cualquier modificación por mínima que sea será muy difícil de hacer.


#def compraPropiedad(jugador,propiedad)
    #Esta función tiene que permitir a un jugador comprar una propiedad
    #Tiene que verificar que el jugador tenga suficiente dinero y que la propiedad no esté ocupada por otro jugador
#def pagarAlquiler(jugador,propiedad)
    #Calcular lo que tiene que pagar un jugador si caen e una propiedad
    #Actualiza la key "diners"
    #Esta tiene que ir dentro de compraPropiedad, y meter un if si casilla es de otro jugador then pagaPropiedad

#Luego funciones que decidan que acción toma el jugador en su turno
    #una funcion que se llame def turnoAccion()
        #Hacer una lista de str con las opciones que puede hacer y realizarlas DDD
def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 
    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

def moverJugador (jugador,posicionActual):

    dado1, dado2, totalDado = tirarDados()
    print(f"Ha salido {dado1} y {dado2}, en total te mueves {totalDado} casillas")

    nuevaPosicion = (posicionActual + totalDado) % len(calles)

    if nuevaPosicion < posicionActual:
        print(f"El jugador {jugador}, ha pasado por la casilla y recibe 200€")
        jugadores[jugador]["Diners"] += 200
    
    print(f"El jugador {jugador} se mueve a {calles[nuevaPosicion]['Nombre']}")
    #Aqui se podría añadir si el jugador cae en una casilla de suerte (if jugador in calles[casilla de la suerte])
    #Que salga una carta al azar de las de suerte
    #También si la casilla en la que recae no esta comprada por otro propietario ofrecer comprarlas
    #Si es de otro jugador cuanto de alquiler tiene que pagar
    return nuevaPosicion

def mostrarInformacion (jugador):
    for jugador, info in jugadores.items():
        print(f"Jugador {jugador.capitalize()}:")
        print(f"Carrers: {info['Carrers']}")
        print(f"Diners: {info['Diners']}")
        print(f"Carta Especial: {info['Carta Especial']}")
        print("")

def inicioPartida():
    global jugadores
    listaJugadores = []

    for key in jugadores:
        listaJugadores.append(key)
    random.shuffle(listaJugadores)

    inicialesJugadores = []

    for jugadores in listaJugadores:
        if jugadores == "groc":
            inicialesJugadores.append("G")
        elif jugadores == "vermell":
            inicialesJugadores.append("V")
        elif jugadores == "blau":
            inicialesJugadores.append("B")
        elif jugadores == "taronja":
            inicialesJugadores.append("T")

    calles[12]['Ocupacion'].extend(inicialesJugadores) #calles[12] es la casilla de salida
    #Verificar que establezca correctamente el orden y que inicialmente esten bien colocados
    return None

def directoPrision(jugador):  #Esta funcion en teoria funciona, y maneja el que un jugador vaya a prisión
    print(f"El jugador{jugador} va directo a la prisión")
    jugadores[jugador]["Posicio"] = 18 #Aquí se actualiza con el numero, que tambien se podira usar con el nombre de la calle (?)
    jugadores[jugador]["Esta en prisión"] = True
    jugadores[jugador]["Turnos en prisión"] = 0

    if jugadores[jugador]["Carta salir de la prisión"] == True: #El primer If es por si tienen la carta
        print(f"El jugador {jugador} ha usado la carta 'Sortir de la presó'")
        jugadores[jugador]["Carta salir de la prisión"] = False #Se actualizan valores 
        jugadores[jugador]["Esta en prisión"] = False #Se sale de la prisión
        return f"El jugador {jugador} ha salido de prisión"
    else:
        print(f"El jugador {jugador} está en la prisión")
        jugadores[jugador]["Esta en prisión"] = True

    if jugadores[jugador]["Torn"] == True:  # Si es el turno del jugador se va actualizando el valor de turnos en prisión 
        jugadores[jugador]["Turnos en prisión"] += 1 #Aquí se actualizan
        return f"El jugador {jugador} ha pasado {jugadores[jugador]["Turnos en prisión"]} turnos en prision"
    return f"El jugador {jugador} continua en prisión"

def cartaSort(jugador):
    cartasSuerte = [
        "Sortir de la presó",
        "Anar a la presó",
        "Anar a la sortida",
        "Anar tres espais enrere",
        "Fer reparacions a les propietats",
        "Ets escollit alcalde"
    ]

    carta = random.choice(cartasSuerte)

    if carta == "Sortir de la presó": #Basicamente est es actualizar los valores del diccionario
        jugadores[jugador]["Carta salir de la prisión"] = True
        jugadores[jugador]["Cartas especials"].append(carta)
    elif carta == "Anar a la presó": #Aqui se usa la funcion ir a la prision
        directoPrision(jugador)
    elif carta == "Anar a la sortida": #Vuelves a la casilla de salida que es la numero 12 (tambien se podria usar con el nomnbre (?))
        jugadores[jugador]["Casilla"] = 12
        jugadores[jugador]["Diners"] += 200
        print(f"El jugador {jugador} esta de vuelta en la casilla de salida")
    elif carta == "Anar tres espais enrere":
        jugadores[jugador]["Posicion"] -= 3 #usar funcion buscaCasilla (?)
        #Esto en teoria no se si es correcto, porque me da a mi que entonces si estas en la salda no puedes retroceder (?)
        if jugadores[jugador]["Posicion"] < 0:
            jugadores[jugador]["Posicion"] = 0
        print(f"El jugador retrocede 3 casillas")
    elif carta == "Fer reparacions a les propietats":
        property = jugadores[jugador]["Propiedades"] #Esto lo uso para el len
        pagar = len(property)*25 + ((jugadores[jugador]["Construcciones"]["Casa"]*100)+(jugadores[jugador]["Construcciones"]["Hotel"]*100))#Aqui accedemos a cada uno de los valores de casa y hoteles y se suman
        jugadores[jugador]["Diners"] -= pagar #Te restan el dinero por tener propiedades
        print(f"Al jugador le toca pagar {pagar} por sus propiedades")
    elif carta == "Ets escollit alcalde":
        totalPago = 0
        for jugadorDiferente in jugadores: #Recorremos la lista de jugadores
            if jugadorDiferente != jugador: #Si el jugador que mira, es diferente al que tiene la carta
                jugadores[jugadorDiferente]["Diners"] -= 50 #Se le restan 50 euros
                totalPago += 50 #Que se suman a esta variable
        jugadores[jugador]["Diners"] += totalPago #I luego se actualiza con el valor de totalPago
        print(f"El jugador {jugador} ha recibido {totalPago}€, enhorabuena por ser alcalde")

def cartaCaixa(jugador):
    cartasCaixa = [
        "Sortir de la presó",
        "Anar a la presó",
        "Error de la banca, guanyes 150€",
        "Despeses mèdiques, pagues 50€",
        "Despeses escolars, pagues 50€",
        "Reparacions al carrer, pagues 40€",
        "Concurs de bellesa, guanyes 10€"
    ]

    carta = random.choice(cartasCaixa)
    print(f"El jugador {jugador} ha recibido la carta: {carta}")

    if carta == "Sortir de la presó":
        jugadores[jugador]["Carta salir de la prisión"] = True
        jugadores[jugador]["Cartas especials"].append("Sortir de la presó")
    elif carta == "Error de la banca, guanyes 150€":
        jugadores[jugador]["Diners"] += 150
    elif carta == "Despeses mèdiques, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
    elif carta == "Despeses escolars, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
    elif carta == "Reparacions al carrer, pagues 40€":
        jugadores[jugador]["Diners"] -= 40
    elif carta == "Concurs de bellesa, guanyes 10€":
        jugadores[jugador]["Diners"] += 10
    elif carta == "Anar a la presó":
        directoPrision(jugador)

#Esta tengo que revisarla
"""def buscaPosicion(nombreCasilla):
    for i, "Nombre", in enumerate(calles):
        if calles["Nombre"] == nombreCasilla:
            return i
        return "No se ha encontrado la posición"""
       