import random
def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 
    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

    
def anadirCasa(jugador, calle): #Esta función se puede usar para añadir una casa o para el momento de comprar la casilla.

    if calle != "Parking" and calle != "Sort" and calle != "Anr pró" and calle != "Caixa" and calle != "Caixa2" and calle != "Sort2" and calle != "Presó":
        dic = {
            "Casas" : 0,
            "Hoteles" : 0
        }
        key = jugador

        for player in jugadores.keys():
            dicComprobar = jugadores[player]["Propiedades"]
            
            if calle in dicComprobar and player != jugador:
                actualizarHistorial(f"Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                return None

        if calle in jugadores[key]["Propiedades"].keys():
            jugadores[key]["Propiedades"][calle]["Casas"] += 1
            actualizarHistorial(f"'{jugador.capitalize()}' compra una casa en '{calle}'")

            if jugadores[key]["Propiedades"][calle]["Casas"] >= 2: #Si tiene 4 casas las elimina y añade un hotel
                jugadores[key]["Propiedades"][calle]["Casas"] -= 2
                jugadores[key]["Propiedades"][calle]["Hoteles"] += 1
                actualizarHistorial(f"'{jugador.capitalize()}' ha conseguido 4 casas, se le suma un hotel")
        else:
            jugadores[key]["Propiedades"][calle] = dic
            actualizarHistorial(f"'{jugador.capitalize()}' ha comprado la casilla '{calle}'")
    else:
        actualizarHistorial(f"Error: {calle} no se puede comprar.")
        return None


def actualizarHistorial(info): #Esta función es la que usaremos para recoger todos los mensajes, lo malo es que para cada uno de los eventos, se tiene que llamar dentro de las funciones 
                              #I hacer .append en todas las funciones de evento

    historial.insert(0, info)
    while len(historial) <= 13:
        historial.append("")
    while len(historial) > 14:
        historial.pop(-1)
    


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
        print(f"Propiedades: {info['Propiedades']}")
        print(f"Diners: {info['Diners']}")
        print(f"Carta Especial: {info['Carta Especial']}")
        print("")

def imprimirCasasHoteles(posicionCasilla):
    if posicionCasilla == 40: #Obviamente no hay ninguna casilla 40, esto es para las lineas que no necesitan pasar por todo ese código
        return "+------------" * 5

    for jugador in jugadores:
        if calles[posicionCasilla]["Nombre"] in jugadores[jugador]["Propiedades"]:
            txt = f"+------{jugador[0].capitalize()}-" + str(jugadores[jugador]["Propiedades"][calles[posicionCasilla]["Nombre"]]["Casas"]) + "C" + str(jugadores[jugador]["Propiedades"][calles[posicionCasilla]["Nombre"]]["Hoteles"]) + "H"
            return txt
         

    return "+------------"

def inicioPartida(players):
    
    #print(jugadores)
    listaJugadores = []

    for key in players:
        listaJugadores.append(key)
    random.shuffle(listaJugadores)

    inicialesJugadores = []

    for players in listaJugadores:
        if players == "groc":
            inicialesJugadores.append("G")
        elif players == "vermell":
            inicialesJugadores.append("V")
        elif players == "blau":
            inicialesJugadores.append("B")
        elif players == "taronja":
            inicialesJugadores.append("T")

    calles[12]['Ocupacion'].extend(inicialesJugadores) #calles[12] es la casilla de salida
    #Verificar que establezca correctamente el orden y que inicialmente esten bien colocados
    #print(jugadores)
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
    """
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
        #if tablero.index(fila) == len(tablero) - 7:
        #    pass
        return "+" + ("-" * ancho_casilla + "+") * cantidad
    """
    

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

    #print(crear_borde_horizontal(len(tablero[0]), ["a", "a", "a"])) #Aquí el ["a", "a", "a"] es porque la funcion requiere un array como parámetro, pero no hace nada con el en esta ocasión
    
    # Imprimir las filas con contenido
    iteracion = 0
    histIt = 13
    for fila in tablero:
                            #Esta serie de ifs crea las barras horizontales del tablero, poniendo el numero de casas y hoteles que tiene el jugador en la casilla en la que está
        if iteracion == 0:
            print(imprimirCasasHoteles(0) + imprimirCasasHoteles(1) + imprimirCasasHoteles(2) + imprimirCasasHoteles(3) + imprimirCasasHoteles(4) + imprimirCasasHoteles(5) + imprimirCasasHoteles(6) + "+")
        if iteracion == 1:
            print(imprimirCasasHoteles(23) + imprimirCasasHoteles(40) + imprimirCasasHoteles(7) + "+")
        if iteracion == 2:
            print(imprimirCasasHoteles(22) + "+ " + historial[11].ljust(63) + imprimirCasasHoteles(8) + "+")
        if iteracion == 3:
            print(imprimirCasasHoteles(21) + "+ " + historial[8].ljust(63) + imprimirCasasHoteles(9) + "+")
        if iteracion == 4:
            print(imprimirCasasHoteles(20) + "+ " + historial[5].ljust(63) + imprimirCasasHoteles(10) + "+")
        if iteracion == 5:
            print(imprimirCasasHoteles(19) + "+ " + historial[2].ljust(63) + imprimirCasasHoteles(11) + "+")
        if iteracion == 6:
            print(imprimirCasasHoteles(18) + imprimirCasasHoteles(17) + imprimirCasasHoteles(16) + imprimirCasasHoteles(15) + imprimirCasasHoteles(14) + imprimirCasasHoteles(13) + "+------------" + "+")
        
        
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
    print(imprimirCasasHoteles(40) + "+------------+------------+") #Esto crea el ultimo borde horizontal del tablero
        #print(crear_borde_horizontal(len(fila), fila))  # Bordes inferiores de cada fila
                


calles = [
    {"Nombre": "Parking", "Ocupacion": []},         #0
    {"Nombre": "Urquinoa", "Ocupacion": [], "LlCasa": 30, "LlHotel": 25, "CmpTrrny": 70, "CmpCasa": 400, "CmpHotel": 290},        #1
    {"Nombre": "Fontan", "Ocupacion": [], "LlCasa": 30, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 425, "CmpHotel": 300},          #2
    {"Nombre": "Sort", "Ocupacion": []},            #3
    {"Nombre": "Rambles", "Ocupacion": ["B","V"], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 450, "CmpHotel": 310},         #4
    {"Nombre": "Pl.Cat", "Ocupacion": []},          #5
    {"Nombre": "Anr pró", "Ocupacion": []},         #6
    {"Nombre": "Angel", "Ocupacion": []},           #7
    {"Nombre": "Augusta", "Ocupacion": []},         #8
    {"Nombre": "Caixa", "Ocupacion": []},           #9
    {"Nombre": "Balmes", "Ocupacion": ["B"]},          #10
    {"Nombre": "Gracia", "Ocupacion": []},          #11
    {"Nombre": "Sortida", "Ocupacion": []},         #12
    {"Nombre": "Lauria", "Ocupacion": [], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 200, "CmpHotel": 250},          #13
    {"Nombre": "Rosell", "Ocupacion": ["B"], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 225, "CmpHotel": 255},          #14
    {"Nombre": "Sort2", "Ocupacion": []},           #15
    {"Nombre": "Marina", "Ocupacion": ["V", "B"], "LlCasa": 15, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 250, "CmpHotel": 260},          #16
    {"Nombre": "Consell", "Ocupacion": ["B"], "LlCasa": 15, "LlHotel": 20, "CmpTrrny": 50, "CmpCasa": 275, "CmpHotel": 265},         #17
    {"Nombre": "Presó", "Ocupacion": []},           #18
    {"Nombre": "Muntan", "Ocupacion": [], "LlCasa": 20, "LlHotel": 20, "CmpTrrny": 60, "CmpCasa": 300, "CmpHotel": 270},          #19
    {"Nombre": "Aribau", "Ocupacion": [], "LlCasa": 20, "LlHotel": 20, "CmpTrrny": 60, "CmpCasa": 325, "CmpHotel": 275},          #20
    {"Nombre": "Caixa2", "Ocupacion": []},          #21
    {"Nombre": "S.Joan", "Ocupacion": [], "LlCasa": 25, "LlHotel": 25, "CmpTrrny": 60, "CmpCasa": 350, "CmpHotel": 280},          #22
    {"Nombre": "Aragó", "Ocupacion": [], "LlCasa": 25, "LlHotel": 25, "CmpTrrny": 60, "CmpCasa": 375, "CmpHotel": 285}            #23
]#Podriamos guardar la ocupacion en el diccionario Jugadores (?) y asignar el calle["Nombre"] a "Jugadores[jugador]["Posició"]"

jugadores = {
    "blau":{
        "Torn":False,
        "Posicio":0,
        "Propiedades": {
            calles[2]["Nombre"]: {
                "Casas": 0,
                "Hoteles": 0
            },
            calles[14]["Nombre"]: {
                "Casas": 1,
                "Hoteles": 1
            },
            calles[16]["Nombre"]: {
                "Casas": 1,
                "Hoteles": 1
            }
        },

        "Diners":2000,
        "Carta Especial":None
        
    },
    "groc":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":{},
        "Diners":2000,
        "Carta Especial":None
    },
    "taronja":{
        "Torn":False,
        "Posicio":0,
        "Propiedades":{},
        "Diners":2000,
        "Carta Especial":None
    },
    "vermell":{
        "Torn":True,
        "Posicio":0,
        "Propiedades":{

            calles[16]["Nombre"]: {
                "Casas": 1,
                "Hoteles": 3
            },
        },
        "Diners":2000,
        "Carta Especial":None
    }
}



# Mi idea con el historial es que siempre tenga este número de valores, aunque estén vacíos y parezca que no haya nada (""), porque en el caso de que se borren valores dará error
# al intentar buscar el valor en el index 13 por ejemplo y esté fuera del rango del array
#Se podria inicializar en historial en historial = "" e ir actualizandolo ?

historial = [
    
]

actualizarHistorial("Hola")
actualizarHistorial("Adios")
actualizarHistorial("Estamos haiendo un monopoly que no es muy divertido aaaaaaaa")

inicioPartida(jugadores)
#print(jugadores)


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

#Las cartas especiales se me ha ocurrido hacerlas de tal forma
#def usarCartaEspecial(jugador)
    #Aqui el jugador debe poder permitir usar una carta especial. Antes crear una funcion random que te de el valor de la carta especial
    
#Luego funciones que decidan que acción toma el jugador en su turno
    #una funcion que se llame def turnoAccion()
        #Hacer una lista de str con las opciones que puede hacer y realizarlas




#propiedadDiccionario("blau", calles[2])
#print(jugadores)
#print(jugadores["blau"]["Propiedades"])


anadirCasa("vermell",calles[4]["Nombre"])
anadirCasa("vermell",calles[4]["Nombre"])

anadirCasa("blau",calles[4]["Nombre"])
anadirCasa("blau",calles[14]["Nombre"])

anadirCasa("groc",calles[5]["Nombre"])

imprimir_tablero(calles)