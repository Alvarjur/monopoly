import random

def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 
    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

def mostrarInformacion():

    mostrarInformacionJugador = []

    for jugador in jugadores:
        mostrarInformacionJugador.append(f"Jugador {jugador.capitalize()}")
        mostrarInformacionJugador.append(f"Carrers: {', '.join(list(jugadores[jugador]['Propiedades'].keys()))}")
        mostrarInformacionJugador.append(f"Diners: {jugadores[jugador]['Diners']}")
        mostrarInformacionJugador.append(f"Especial: {', '.join(jugadores[jugador]['Carta Especial'])}")
        mostrarInformacionJugador.append("")
    
    #for mensaje in mostrarInformacionJugador:
    #    print(mensaje)

    return mostrarInformacionJugador

def anadirCasa(jugador, calle): #Esta función se puede usar para añadir una casa o para el momento de comprar la casilla.

    if calle != "Parking" and calle != "Sort" and calle != "Anr pró" and calle != "Caixa" and calle != "Caixa2" and calle != "Sort2" and calle != "Presó":
        dic = {
            "Casas" : 0,
            "Hoteles" : 0
        }

        key = jugador

        for street in calles:
            if calle in street.values():
                dicCalle = street

        for player in jugadores.keys():
            dicComprobar = jugadores[player]["Propiedades"]
            
            if calle in dicComprobar and player != jugador:
                actualizarHistorial(f"Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                return None

        if calle in jugadores[key]["Propiedades"].keys():
            if jugadores[key]["Propiedades"][calle]["Casas"] >= 4:
                actualizarHistorial(f"Error: Se pueden tener cómo máximo 4 casas, compra un hotel.")
                return None
            elif jugadores[key]["Diners"] >= dicCalle["CmpCasa"]: #Si tiene dinero suficiente para comprar una casa.
                jugadores[key]["Propiedades"][calle]["Casas"] += 1
                jugadores[key]["Diners"] -= dicCalle["CmpCasa"] #Resta el dinero de la casa al dinero del jugador

                actualizarHistorial(f"'{jugador.capitalize()}' compra una casa en '{calle}'")

                #if jugadores[key]["Propiedades"][calle]["Casas"] >= 2: #Si tiene 4 casas las elimina y añade un hotel
                #    jugadores[key]["Propiedades"][calle]["Casas"] -= 2
                #    jugadores[key]["Propiedades"][calle]["Hoteles"] += 1
                #    actualizarHistorial(f"'{jugador.capitalize()}' ha conseguido 4 casas, se le suma un hotel")
            else:
                actualizarHistorial(f"Error: Una casa cuesta {dicCalle['CmpCasa']} y tienes {jugadores[key]['Diners']}")
                return None
        else:
            if jugadores[key]["Diners"] >= dicCalle["CmpCasa"]:
                jugadores[key]["Propiedades"][calle] = dic
                actualizarHistorial(f"'{jugador.capitalize()}' ha comprado la casilla '{calle}'")
                jugadores[key]["Diners"] -= dicCalle["CmpCasa"] #Resta el dinero de la casilla al dinero del jugador
                return None
            else:
                actualizarHistorial(f"Error: La casilla cuesta {dicCalle['CmpCasa']} y tienes {jugadores[key]['Diners']}")
                return None
    else:
        actualizarHistorial(f"Error: '{calle}' no se puede comprar.")
        return None

def anadirHotel(jugador, calle):
    if calle != "Parking" and calle != "Sort" and calle != "Anr pró" and calle != "Caixa" and calle != "Caixa2" and calle != "Sort2" and calle != "Presó":
        dic = {
            "Casas" : 0,
            "Hoteles" : 0
        }

        key = jugador

        for street in calles:
            if calle in street.values():
                dicCalle = street

        for player in jugadores.keys():
            dicComprobar = jugadores[player]["Propiedades"]
            
            if calle in dicComprobar and player != jugador:
                actualizarHistorial(f"Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                return None

        if calle in jugadores[key]["Propiedades"].keys():
            if jugadores[key]["Propiedades"][calle]["Casas"] >= 2:
                if jugadores[key]["Propiedades"][calle]["Hoteles"] < 3: #Se comprueba que el jugador no tenga ya 2 hoteles en esa casilla.
                    if jugadores[key]["Diners"] >= dicCalle["CmpHotel"]:
                        jugadores[key]["Propiedades"][calle]["Casas"] -= 2
                        jugadores[key]["Propiedades"][calle]["Hoteles"] += 1
                        actualizarHistorial(f"'{jugador}' compra un hotel en {calle}")
                    else:
                        actualizarHistorial(f"Error: Un hotel cuesta {dicCalle['CmpHotel']} y tienes {jugadores[key]['Diners']}")
                        return None
                else:
                    actualizarHistorial(f"Error: Ya tienes 2 hoteles en {calle}.")
                    return None
            else:
                actualizarHistorial(f"Error: Para comprar un hotel hacen falta al menos 2 casas.")
                return None
  
    else:
        actualizarHistorial(f"Error: '{calle}' no se puede comprar.")
        return None

jugadoresEnBancarrota = []
def bancaRota(rendirse = False):
    global banca
    for jugador in jugadores.keys():
        if jugadores[jugador]["Diners"] <= 0 and jugador not in jugadoresEnBancarrota and jugadores[jugador]["Torn"] == True:
            actualizarHistorial(f"{jugador.capitalize()} está en bancarrota")
            while True:
                jugadoresEnBancarrota.append(jugador)
                eleccion = ""
                if rendirse == False:
                    eleccion = input("1. Vender al banco 2. Vender a otro jugador 3. Darse en bancarrota")
                ValorAlVender = 0
                if eleccion == "1":
                    for propiedad in jugadores[jugador]["Propiedades"]:
                        for calle in calles:
                            if calle["Nombre"] == propiedad:
                                #print(propiedad + ":")
                                #print(calle)
                                for construccion in jugadores[jugador]["Propiedades"][propiedad].keys():
                                    if construccion == "Casas":
                                        valorInd = calle["CmpCasa"] * jugadores[jugador]["Propiedades"][propiedad][construccion]
                                    if construccion == "Hoteles":
                                        valorInd = calle["CmpHotel"] * jugadores[jugador]["Propiedades"][propiedad][construccion]
                                    ValorAlVender += valorInd
                    jugadores[jugador]["Propiedades"] = {} #Se vacían las propiedades del jugador
                    ValorAlVender = (ValorAlVender * 50) // 100
                    banca -= ValorAlVender
                    #print(jugadores[jugador]["Diners"])
                    jugadores[jugador]["Diners"] += ValorAlVender
                    actualizarHistorial(f"{jugador.capitalize()} ha vendido sus propiedades a la banca por {ValorAlVender}")
                    break
                elif eleccion == "2":
                    jugadoresNoTurno = []
                    for player in jugadores:
                        if player != jugador:
                            jugadoresNoTurno.append(player)
                    while True:
                        comprador = input(f"A quién le quieres vender?: "+ ", ".join(jugadoresNoTurno)+" ")
                        comprador = comprador.lower()
                        if comprador in jugadoresNoTurno:
                            break
                        
                    for propiedad in jugadores[jugador]["Propiedades"]:
                        for calle in calles:
                            if calle["Nombre"] == propiedad:
                                #print(propiedad + ":")
                                #print(calle)
                                for construccion in jugadores[jugador]["Propiedades"][propiedad].keys():
                                    if construccion == "Casas":
                                        valorInd = calle["CmpCasa"] * jugadores[jugador]["Propiedades"][propiedad][construccion]
                                    if construccion == "Hoteles":
                                        valorInd = calle["CmpHotel"] * jugadores[jugador]["Propiedades"][propiedad][construccion]
                                    ValorAlVender += valorInd
                    ValorAlVender = (ValorAlVender * 90) // 100 #Al ser otro jugador el comprador, es un 90% de lo que pagó el vendedor
                    if jugadores[comprador]["Diners"] >= ValorAlVender:
                        jugadores[comprador]["Diners"] -= ValorAlVender
                        jugadores[jugador]["Diners"] += ValorAlVender

                        propiedadesJugador = jugadores[jugador]["Propiedades"].items()

                        jugadores[comprador]["Propiedades"].update(propiedadesJugador)
                        jugadores[jugador]["Propiedades"] = {}

                        actualizarHistorial(f"{jugador.capitalize()} ha vendido sus propiedades a {comprador.capitalize()} por {ValorAlVender}")
                        break
                    else:
                        print(f"{comprador} no tiene dinero")
                        actualizarHistorial(f"{comprador.capitalize()} no tiene suficiente dinero")
                        
                elif eleccion == "3" or rendirse == True:
                    jugadores[jugador]["Propiedades"] = {}
                    jugadoresEnBancarrota.append(jugador)
                    actualizarHistorial(f"{jugador.capitalize()} se ha dado en bancarrota, no jugará más")
                    break
            

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
    alto_casilla = 2 #Solo funciona si es 2.

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
                if elemento == "Anr pró    |":
                    resultado += " " + elemento + f" {banca}"

                elif elemento == "Sortida    |":
                    resultado += " " + elemento + f" {mostrarInformacion()[16]}"
                else:
                    resultado += " " + elemento
                   

            iteracion += 1
        
        nuevoEl = "|" + resultado[1:] #Esto lo que hace es una vez este el texto completo, reemplaza el primer valor del string con "|", para cerrar la caja.
        resultado = nuevoEl  
        #print(resultado)
        #print(iteracion)
        #input()


        
        return resultado
    

    
    # Imprimir las filas con contenido
    iteracion = 0
    histIt = 13
    for fila in tablero:
                            #Esta serie de ifs crea las barras horizontales del tablero, poniendo el numero de casas y hoteles que tiene el jugador en la casilla en la que está
        if iteracion == 0:
            print(imprimirCasasHoteles(0) + imprimirCasasHoteles(1) + imprimirCasasHoteles(2) + imprimirCasasHoteles(3) + imprimirCasasHoteles(4) + imprimirCasasHoteles(5) + imprimirCasasHoteles(6) + "+ " + "Banca:")
        if iteracion == 1:
            print(imprimirCasasHoteles(23) + imprimirCasasHoteles(40) + imprimirCasasHoteles(7) + "+ " + mostrarInformacion()[0])
        if iteracion == 2:
            print(imprimirCasasHoteles(22) + "+ " + historial[11].ljust(63) + imprimirCasasHoteles(8) + "+ " + mostrarInformacion()[3])
        if iteracion == 3:
            print(imprimirCasasHoteles(21) + "+ " + historial[8].ljust(63) + imprimirCasasHoteles(9) + "+ " + mostrarInformacion()[6])
        if iteracion == 4:
            print(imprimirCasasHoteles(20) + "+ " + historial[5].ljust(63) + imprimirCasasHoteles(10) + "+ " + mostrarInformacion()[9])
        if iteracion == 5:
            print(imprimirCasasHoteles(19) + "+ " + historial[2].ljust(63) + imprimirCasasHoteles(11) + "+ " + mostrarInformacion()[12])
        if iteracion == 6:
            print(imprimirCasasHoteles(18) + imprimirCasasHoteles(17) + imprimirCasasHoteles(16) + imprimirCasasHoteles(15) + imprimirCasasHoteles(14) + imprimirCasasHoteles(13) + "+------------" + "+ " + mostrarInformacion()[15])
        
        
        for _ in range(alto_casilla):  # Altura de cada casilla (varias líneas por fila)
            
            if _ == 0:  # Contenido en la línea de arriba de la casilla
                if tablero.index(fila) >= 1 and tablero.index(fila) < 6:
                    txt = crear_fila_contenido(fila)
                    lineaSeparada = txt.split("|")
                    lineaSeparada[2] = historial[histIt]
                    lineaJunta = f"|" + f"{lineaSeparada[1]}" + "| " f"{lineaSeparada[2]}".ljust(65) + "|" + f"{lineaSeparada[3]}".ljust(12) + "| " + mostrarInformacion()[20 - (histIt + 6)]
                    histIt -= 3
                    
                    print(lineaJunta)
                else:
                    print(crear_fila_contenido(fila))
            else:  # Líneas vacías para la altura

                if iteracion == 0 or iteracion == 6:  #Según la iteracion del bucle for, añade barras verticales y la ocupacion de cada calle para la iteracion 0 y 6, es decir la primera y la última
                    if iteracion == 0:
                        txt = f"|" + f"".join(calles[0]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[1]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[2]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[3]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[4]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[5]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[6]['Ocupacion']).ljust(12) + f"| " 
                    if iteracion == 6:
                        txt = f"|" + f"".join(calles[18]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[17]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[16]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[15]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[14]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[13]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[12]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[17] 
                    print(txt)
                    
                else:
                    if iteracion == 1:
                        txt = f"|" + f"".join(calles[23]['Ocupacion']).ljust(12) + f"| " + f"{historial[12]}".ljust(63) + f"|" + f"".join(calles[7]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[2]
                    if iteracion == 2:
                        txt = f"|" + f"".join(calles[22]['Ocupacion']).ljust(12) + f"| " + f"{historial[9]}".ljust(63) + f"|" + f"".join(calles[8]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[5]
                    if iteracion == 3:
                        txt = f"|" + f"".join(calles[21]['Ocupacion']).ljust(12) + f"| " + f"{historial[6]}".ljust(63) + f"|" + f"".join(calles[9]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[8]
                    if iteracion == 4:
                        txt = f"|" + f"".join(calles[20]['Ocupacion']).ljust(12) + f"| " + f"{historial[3]}".ljust(63) + f"|" + f"".join(calles[10]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[11]
                    if iteracion == 5:
                        txt = f"|" + f"".join(calles[19]['Ocupacion']).ljust(12) + f"| " + f"{historial[0]}".ljust(63) + f"|" + f"".join(calles[11]['Ocupacion']).ljust(12) + f"| " + mostrarInformacion()[14]
                    
                    print(txt)
                iteracion += 1
    print(imprimirCasasHoteles(40) + "+------------+------------+ " + mostrarInformacion()[18]) #Esto crea el ultimo borde horizontal del tablero
        #print(crear_borde_horizontal(len(fila), fila))  # Bordes inferiores de cada fila
                


calles = [
    {"Nombre": "Parking", "Ocupacion": []},         #0
    {"Nombre": "Urquinoa", "Ocupacion": [], "LlCasa": 30, "LlHotel": 25, "CmpTrrny": 70, "CmpCasa": 400, "CmpHotel": 290},        #1
    {"Nombre": "Fontan", "Ocupacion": [], "LlCasa": 30, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 425, "CmpHotel": 300},          #2
    {"Nombre": "Sort", "Ocupacion": []},            #3
    {"Nombre": "Rambles", "Ocupacion": ["B","V"], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 450, "CmpHotel": 310},         #4
    {"Nombre": "Pl.Cat", "Ocupacion": [], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 475, "CmpHotel": 325},          #5
    {"Nombre": "Anr pró", "Ocupacion": []},         #6
    {"Nombre": "Angel", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 500, "CmpHotel": 330},           #7
    {"Nombre": "Augusta", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 340},         #8
    {"Nombre": "Caixa", "Ocupacion": []},           #9
    {"Nombre": "Balmes", "Ocupacion": ["B"], "LlCasa": 50, "LlHotel": 40, "CmpTrrny": 80, "CmpCasa": 550, "CmpHotel": 350},          #10
    {"Nombre": "Gracia", "Ocupacion": [], "LlCasa": 50, "LlHotel": 50, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 360},          #11
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
        "Torn":True,
        "Posicio":0,
        "Propiedades": {
            calles[2]["Nombre"]: {
                "Casas": 2,
                "Hoteles": 0
            },
            calles[14]["Nombre"]: {
                "Casas": 0,
                "Hoteles": 1
            },
            calles[16]["Nombre"]: {
                "Casas": 3,
                "Hoteles": 0
            }
        },

        "Diners":0,
        "Carta Especial": []
        
    },
    "groc":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":{},
        "Diners":20000,
        "Carta Especial": []
    },
    "taronja":{
        "Torn":False,
        "Posicio":0,
        "Propiedades":{},
        "Diners":2000,
        "Carta Especial": []
    },
    "vermell":{
        "Torn":False,
        "Posicio":0,
        "Propiedades":{

        },
        "Diners":2000,
        "Carta Especial": []
    }
}

banca = 1000000

historial = [
    
]

actualizarHistorial("Hola")
actualizarHistorial("Adios")
actualizarHistorial("Estamos haiendo un monopoly que no es muy divertido aaaaaaaa")

inicioPartida(jugadores)


anadirCasa("vermell",calles[4]["Nombre"])
anadirCasa("vermell",calles[4]["Nombre"])

anadirCasa("blau",calles[4]["Nombre"])
anadirCasa("blau",calles[14]["Nombre"])


#anadirCasa("groc",calles[5]["Nombre"])
#anadirCasa("groc","Pl.Cat")
#anadirCasa("groc","Pl.Cat")


imprimir_tablero(calles)
bancaRota()
imprimir_tablero(calles)

#print(mostrarInformacion())
