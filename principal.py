import random
import json

calles = [
    {"Nombre": "Parking", "Ocupacion": [],"Casilla" : 0},         #0
    {"Nombre": "Urquinoa", "Ocupacion": [], "LlCasa": 30, "LlHotel": 25, "CmpTrrny": 70, "CmpCasa": 400, "CmpHotel": 290,"Casilla" : 1},        #1
    {"Nombre": "Fontan", "Ocupacion": [], "LlCasa": 30, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 425, "CmpHotel": 300,"Casilla" : 2},          #2
    {"Nombre": "Sort", "Ocupacion": [],"Casilla" : 3},            #3
    {"Nombre": "Rambles", "Ocupacion": ["B","V"], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 450, "CmpHotel": 310,"Casilla" : 4},         #4
    {"Nombre": "Pl.Cat", "Ocupacion": [], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 475, "CmpHotel": 325,"Casilla" : 5},          #5
    {"Nombre": "Anr pró", "Ocupacion": [],"Casilla" : 6},         #6
    {"Nombre": "Angel", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 500, "CmpHotel": 330,"Casilla" : 7},           #7
    {"Nombre": "Augusta", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 340,"Casilla" : 8},         #8
    {"Nombre": "Caixa", "Ocupacion": [],"Casilla" : 9},           #9
    {"Nombre": "Balmes", "Ocupacion": ["B"], "LlCasa": 50, "LlHotel": 40, "CmpTrrny": 80, "CmpCasa": 550, "CmpHotel": 350,"Casilla" : 10},          #10
    {"Nombre": "Gracia", "Ocupacion": [], "LlCasa": 50, "LlHotel": 50, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 360,"Casilla" : 11},          #11
    {"Nombre": "Sortida", "Ocupacion": [],"Casilla" : 12},         #12
    {"Nombre": "Lauria", "Ocupacion": [], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 200, "CmpHotel": 250,"Casilla" : 13},          #13
    {"Nombre": "Rosell", "Ocupacion": ["B"], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 225, "CmpHotel": 255,"Casilla" : 14},          #14
    {"Nombre": "Sort2", "Ocupacion": [],"Casilla" : 15},           #15
    {"Nombre": "Marina", "Ocupacion": ["V", "B"], "LlCasa": 15, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 250, "CmpHotel": 260,"Casilla" : 16},          #16
    {"Nombre": "Consell", "Ocupacion": ["B"], "LlCasa": 15, "LlHotel": 20, "CmpTrrny": 50, "CmpCasa": 275, "CmpHotel": 265,"Casilla" : 17},         #17
    {"Nombre": "Presó", "Ocupacion": [],"Casilla" : 18},           #18
    {"Nombre": "Muntan", "Ocupacion": [], "LlCasa": 20, "LlHotel": 20, "CmpTrrny": 60, "CmpCasa": 300, "CmpHotel": 270,"Casilla" : 19},          #19
    {"Nombre": "Aribau", "Ocupacion": [], "LlCasa": 20, "LlHotel": 20, "CmpTrrny": 60, "CmpCasa": 325, "CmpHotel": 275,"Casilla" : 20},          #20
    {"Nombre": "Caixa2", "Ocupacion": [],"Casilla" : 21},          #21
    {"Nombre": "S.Joan", "Ocupacion": [], "LlCasa": 25, "LlHotel": 25, "CmpTrrny": 60, "CmpCasa": 350, "CmpHotel": 280,"Casilla" : 22},          #22
    {"Nombre": "Aragó", "Ocupacion": [], "LlCasa": 25, "LlHotel": 25, "CmpTrrny": 60, "CmpCasa": 375, "CmpHotel": 285,"Casilla" : 23}            #23
]
#Podriamos guardar la ocupacion en el diccionario Jugadores (?) y asignar el calle["Nombre"] a "Jugadores[jugador]["Posició"]"

jugadores = {
    "blau":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "CartasEspecials": [],
        "Diners":2000,
        "CartaSalirDeLaPrision":False,
        "EstaEnPrision":False,
        "TurnosEnPrision":0
    },
    "groc":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "CartasEspecials": [],
        "Diners":2000,
        "CartaSalirDeLaPrision":False, #Aquí esto puede que sea mejor ponerlo como un if "CartaSalirDePrision" in jugadores[jugador]["Cartas especials"] #como idea solo.
        "EstaEnPrision":False, #También como estándar seguramente sería mejor poner los nombres de las keys sin espacios ni acentos, por si acaso da errores.
        "TurnosEnPrision":0
    },
    "taronja":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "CartasEspecials": [],
        "Diners":2000,
        "CartaSalirDeLaPrision":False,
        "EstaEnPrision":False,
        "TurnosEnPrision":0
    },
    "vermell":{
        "Torn":False,
        "Posicio":0,#Para indicar en que posición esta
        "Propiedades":[],
        "Construcciones":{
            "Casa":0,
            "Hotel":0
        },
        "CartasEspecials": [],
        "Diners":2000,
        "CartaSalirDeLaPrision":False,#Nos dice si tiene la carta de salir prisión o no para despues poder usarla
        "EstaEnPrision":False,#Estos nos dice si esta en prisión o no
        "TurnosEnPrision":0 #Como dice el nombre cuantos turnos lleva en prisión
    }
}
banca = 1000000
historial = []

def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 
    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

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

    calles[12]['Ocupacion'].extend(inicialesJugadores) 
    return None
#Falataria modificar la ocupacion a la primera Letra del jugador /////////////////
#Añadir los mensajes de la banca ////////////
#Verificar que el jugador que construya casa o hotel sea el dueño de la propiedad
def moverJugador (jugador,posicionActual):

    callesNoCompra = ["Parking","Sort","Anr pró","Caixa","Sortida","Sort2","Presó","Caixa2"]
    dado1, dado2, totalDado = tirarDados()
    print(f"Ha salido {dado1} y {dado2}, en total te mueves {totalDado} casillas")

    nuevaPosicion = (posicionActual + totalDado) % len(calles)
    jugadores[jugador]["Posicion"] = nuevaPosicion
    calleEnJuego = calles[nuevaPosicion] #Esto es para que me devuelva el valor de la entrada según la posicion del jugador (es como un indice)

    if jugadores[jugador]["Posicion"] == calleEnJuego["Casilla"]: #Esto siempre se va a dar
        if not calleEnJuego["Ocupacion"] and calleEnJuego["Nombre"] not in callesNoCompra:
            opcion = input("Que desea hacer ['Pass','CmpTerreny','CmpCasa','CmpHotel','verPrecios','preuBanc','preuJugador','vendreBanc',vendreJugador'? ")
            if opcion == 'Pass':
                jugadores[jugador]["Torn"] = False
                mensajePasar = f"El jugador {jugador} ha pasado turno. No ha realizadno ningún movimient"
                actualizarHistorial(mensajePasar)
            elif opcion == "CmpTerreny":
                if jugadores[jugador]["Diners"] >= calleEnJuego["CmpTerreny"]:
                    jugadores[jugador]["Diners"] -= calleEnJuego["CmpTerreny"]
                    calleEnJuego["Ocupacion"] = jugadores[jugador]
                    banca = banca + calleEnJuego["CmpTerreny"]
                    mensajeCompraTerreno = f"El jugador {jugador}, ha comprado un terreno en la calle {calleEnJuego["Nombre"]}"
                    actualizarHistorial(mensajeCompraTerreno)
                    #jugadores[jugador]["Torn"] = False // Finalizamos el turno ? (esto para todos los casos)
                else:
                    mensajeNoDinero = f"El jugador {jugador} no tiene suficiente dinero para comprar el terrno"
                    actualizarHistorial(mensajeNoDinero)
            elif opcion == "CmpCasa":
                if jugadores[jugador]["Diners"] >= calleEnJuego["CmpCasa"]:
                    if jugadores[jugador]["construcciones"]["casa"] < 4:
                        jugadores[jugador]["Diners"] -= calleEnJuego["CmpCasa"]
                        banca = banca + calleEnJuego["CmpCasa"]
                        mensajeCompraCasa = f"El jugador {jugador} ha compraro una casa en {calleEnJuego["Nombre"]}"
                        actualizarHistorial(mensajeCompraCasa)
                    else:
                        mensajeMaxCasa = input(f"Ya tienes 4 casas construidas, desea comprar un hotel ? [s/n]")
                        if mensajeMaxCasa == "s":
                            jugadores[jugador]["construcciones"]["casa"] -= 2
                            jugadores[jugador]["construcciones"]["Hotel"] += 1
                            mensajeCompraHotel = f"El jugador {jugador} ha cambiao 2 casas por un hotel en la calle {calleEnJuego['Nombre']}"
                            actualizarHistorial(mensajeCompraHotel)
                else:
                    mensajeNoDineroCasa = f"El jugador {jugador}, no tiene suficiente dinero para comprar una casa"
                    actualizarHistorial(mensajeNoDineroCasa)
            elif opcion == "CmpHotel":
                if jugadores[jugador]["construcciones"]["Casa"] < 2:
                    print("No puedes constuir un hotel debido a que no tienes casas suficientes")
                if jugadores[jugador]["Diners"] < calleEnJuego["CmpHotel"]:
                    mensajeNoDineroHotel = f"El jugador {jugador} no puede comprar un hotel porque no tiene suficiente dinero"
                    actualizarHistorial(mensajeNoDineroHotel)
                elif jugadores[jugador]["Diners"] >= calleEnJuego["CmpHotel"]:
                    if jugadores[jugador]["construcciones"]["Hotel"] == 2 and jugadores[jugador]["construcciones"]["casa"] < 4:
                        mensajeMaxHotel = input(f"No puede comprar mas hoteles, deseas comprar mas casas ? [s/n]")
                        if mensajeMaxHotel == "s":
                            jugadores[jugador]["diners"] -= calleEnJuego["CmpCasa"]
                            jugadores[jugador]["construcciones"]["casa"] += 1
                            actualizarHistorial(mensajeCompraCasa)
                        elif jugadores[jugador]["construcciones"]["Hotel"] == 2 and jugadores[jugador]["construcciones"]["casa"] == 4:
                            mensajeCalleCompleta = f"No puedes construir mas propiedades, la calle esta completa"
                            actualizarHistorial(mensajeCalleCompleta)
                    elif jugadores[jugador]["construcciones"]["Hotel"] < 2 and jugadores[jugador]["construcciones"]["Casa"] >= 2:
                        jugador[jugador]["Diners"] -= calleEnJuego["CmpHotel"]
                        banca = banca + calleEnJuego["CmpHotel"]
                        mensajeCompraHotel = f"El jugador {jugador} ha comprado un hotel en {calleEnJuego["Nombre"]}"
                        actualizarHistorial(mensajeCompraHotel)
            elif opcion == "preus":
                mensajePreus = f"Casa: {calleEnJuego['CmpCasa']}, Hotel: {calleEnJuego['cmpHotel']}"
                print(mensajePreus)
                actualizarHistorial(mensajePreus)
                #"""elif opcion == "banc" and jugadores[jugador]["Diners"] < // aqui me faltaria poner, preuBanc, preuJugador, vendreBanc, vendreJugador"""
        elif calleEnJuego["Nombre"] not in callesNoCompra and calleEnJuego["Ocupacion"] is not None and jugadores[jugador[0]].upper() not in calleEnJuego["Ocupacion"]:
            #Este bloque de codigo es para cuando el jugado cae en una casilla con alquiler
            #Modificar en base
            if calleEnJuego["Ocupacion"] == "V":
                pagojugador = (jugadores["vermell"]["construcciones"]["casa"]*calleEnJuego["Ll.Casa"]) + (jugadores["vermell"]["construcciones"]["hotel"]*calleEnJuego["Ll.Hotel"])
                jugadores[jugador]["Diners"] -= pagojugador
                jugadores[jugador]["vermell"] += pagojugador
                mensajeVermell = f"El jugador {jugador} paga {pagojugador}€ al jugador {jugadores["vermell"]} por sus propiedades"
                actualizarHistorial(mensajeVermell)
            elif calleEnJuego["Ocupacion"] == "T":
                pagojugador = (jugador["taronja"]["construcciones"]["casa"]*calleEnJuego["Ll.Casa"]) + (jugadores["taronja"]["construcciones"]["casa"]*calleEnJuego["Ll.Hotel"])
                jugadores[jugador]["Diners"] -= pagojugador
                jugadores[jugador]["taronja"] += pagojugador
                mensajeTaronja = f"El jugador {jugador} paga {pagojugador}€ al jugador {jugadores["Taronja"]} por sus propiedades"
                actualizarHistorial(mensajeTaronja)
            elif calleEnJuego["Ocupacion"] == "B":
                pagojugador = (jugador["blau"]["construcciones"]["casa"]*calleEnJuego["Ll.Casa"]) + (jugadores["blau"]["construcciones"]["casa"]*calleEnJuego["Ll.Hotel"])
                jugadores[jugador]["Diners"] -= pagojugador
                jugadores[jugador]["blau"] += pagojugador
                mensajeBlau = f"El jugador {jugador} paga {pagojugador}€ al jugador {jugadores["blau"]} por sus propiedades"
                actualizarHistorial(mensajeBlau)
            elif calleEnJuego["Ocupacion"] == "G":
                pagojugador = (jugador["groc"]["construcciones"]["casa"]*calleEnJuego["Ll.Casa"]) + (jugadores["groc"]["construcciones"]["casa"]*calleEnJuego["Ll.Hotel"])
                jugadores[jugador]["Diners"] -= pagojugador
                jugadores[jugador]["groc"] += pagojugador
                mensajeGroc = f"El jugador {jugador} paga {pagojugador}€ al jugador {jugadores["groc"]} por sus propiedades"
                actualizarHistorial(mensajeGroc)
            #A partir de aqui son las casillas de evento
        elif calleEnJuego["Nombre"] in callesNoCompra:
            if calleEnJuego["Nombre"] == "Sort" or calleEnJuego["Nombre"] == "Sort2":
                cartaSort(jugador)
            elif calleEnJuego["Nombre"] == "Anr pró" or calleEnJuego["Nombre"] == "Presó":
                directoPrision(jugador)
            elif calleEnJuego["Nombre"] == "Caixa" or calleEnJuego["Nombre"] == "Caixa2":
                cartaCaixa(jugador)
            elif calleEnJuego["Nombre"] == "Sortida" and jugadores[jugador]["Posicion"] >= calles["Casilla"][12]: #Esta tiene que ir dentro o fuera del if ?
                mensajeSalida = f"El jugador {jugador}, ha pasado por la casilla y recibe 200€"
                jugadores[jugador]["Diners"] += 200
                actualizarHistorial(mensajeSalida)
            elif calleEnJuego["Nombre"] == "Parking":
                mensajeParking = f"El jugador a caído en el Parking, pasa su turno"
                actualizarHistorial(mensajeParking)
                
    #if nuevaPosicion < posicionActual:
        #print(f"El jugador {jugador}, ha pasado por la casilla y recibe 200€")
        #jugadores[jugador]["Diners"] += 200
    
    print(f"El jugador {jugador} se mueve a {calles[nuevaPosicion]['Nombre']}")

    return nuevaPosicion
print(moverJugador("groc",18))
# Mi idea con el historial es que siempre tenga este número de valores, aunque estén vacíos y parezca que no haya nada (""), porque en el caso de que se borren valores dará error
# al intentar buscar el valor en el index 13 por ejemplo y esté fuera del rango del array
#Se podria inicializar en historial en historial = "" e ir actualizandolo ? #No porque solo tendría un valor, en todo caso sería historial = ["","",""...hasta 14] 

historial = [] #Esta variable almacena el array completo del historial que sera <= 10


def actualizarHistorial(info): #Esta función es la que usaremos para recoger todos los mensajes, lo malo es que para cada uno de los eventos, se tiene que llamar dentro de las funciones 
                               #I hacer .append en todas las funciones de evento
    historial.insert(0, info)
    while len(historial) <= 13:
        historial.append("")
    while len(historial) > 14:
        historial.pop(-1)

def directoPrision(jugador):

    #Primero te envian directo a prisión y se actualizan tus valores 
    mensajePrision = f"El jugador {jugador} va directo a la prisión"
    actualizarHistorial(mensajePrision)
    jugadores[jugador]["Posicio"] = 18
    jugadores[jugador]["EstaEnPrision"] = True
    jugadores[jugador]["TurnosEnPrision"] = 0
  
    #Aqui entra en juego si tiene o no la carta
    #Si la tienes puedes seguir jugando y se actualizan los valores del diccionario
    if jugadores[jugador]["CartaSalirDeLaPrision"] == True:
        jugadores[jugador]["CartaSalirDeLaPrision"] = False
        jugadores[jugador]["EstaEnPrision"] = False
        mensajeSiCarta = f"El jugador {jugador} ha usado la carta 'Sortir de la presó'"
        actualizarHistorial(mensajeSiCarta)
    else:#Si no la tienes vas a la carcel, y si es tu turno se suma 1 a la variable turnos en prision

        jugadores[jugador]["EstaEnPrision"] = True
        mensajeNoCarta = f"El jugador {jugador} no tiene la carta especial para salvarse, está en la prisión !"
        actualizarHistorial(mensajeNoCarta)

        if jugadores[jugador]["Torn"] == True:  # Si es el turno del jugador se va actualizando el valor de turnos en prisión 
            jugadores[jugador]["EstaEnPrision"] += 1 #Aquí se actualizan
            mensajeTurnosPrision = f"El jugador {jugador} ha pasado {jugadores[jugador]["EstaEnPrision"]} turnos en prision"
            actualizarHistorial(mensajeTurnosPrision)
        elif jugadores[jugador]["Torn"] == True and jugadores[jugador]["Turnos en prision"] == 3:
            jugadores[jugador]["Turnos en prision"] = 0
            mensajeSalidaPrision = f"El jugador {jugador} ha salido de la carcel despues de 3 turnos !"
            actualizarHistorial(mensajeSalidaPrision)


    return None  #En un futuro lo suyo sería que las funciones devolvieran none pero que añadan una línea al historial,
                              #haría falta una función que mantenga la cantidad de valores del historial en 10, que elimine las antiguas y meta nuevas lineas.
                              # ^
                              #En teoria de esta forma ya estaría solucionado

def moverJugador (jugador,posicionActual): #Me falta por completarla

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
    # ^
    # Para esto es mejor hacerlo en esta función o crear otra? #Seguramente crear otra sea lo mejor

    return nuevaPosicion

def mostrarInformacion(jugador):

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
    mensajeSuerte = f"El jugador {jugador} ha recibido la carta: {carta}"
    actualizarHistorial(mensajeSuerte)

    if carta == "Sortir de la presó": #Basicamente est es actualizar los valores del diccionario
        jugadores[jugador]["CartaSalirDeLaPrision"] = True
        jugadores[jugador]["CartasEspecials"].append(carta)
        mensajeSalirPrision = f"El jugador {jugador} ha obtenido una carta para salir de la prisión !"
        actualizarHistorial(mensajeSalirPrision)
    elif carta == "Anar a la presó": #Aqui se usa la funcion ir a la prision
         return directoPrision(jugador)
    elif carta == "Anar a la sortida": #Vuelves a la casilla de salida que es la numero 12 (tambien se podria usar con el nomnbre (?))
        jugadores[jugador]["Posicio"] = 12
        jugadores[jugador]["Diners"] += 200
        mensajeSalida = f"El jugador {jugador} esta de vuelta en la casilla de salida !"
        actualizarHistorial(mensajeSalida)
    elif carta == "Anar tres espais enrere":
        jugadores[jugador]["Posicio"] -= 3 #usar funcion buscaCasilla (?)
        #Esto en teoria no se si es correcto, porque me da a mi que entonces si estas en la salida no puedes retroceder (?)
        if jugadores[jugador]["Posicio"] < 0:
            jugadores[jugador]["Posicio"] = 0
        mensajeTresEspacios = f"El jugador retrocede 3 casillas"
        actualizarHistorial(mensajeTresEspacios)
    elif carta == "Fer reparacions a les propietats":
        property = jugadores[jugador]["Propiedades"] #Esto lo uso para el len
        pagar = len(property)*25 + ((jugadores[jugador]["Construcciones"]["Casa"]*100)+(jugadores[jugador]["Construcciones"]["Hotel"]*100))#Aqui accedemos a cada uno de los valores de casa y hoteles y se suman
        jugadores[jugador]["Diners"] -= pagar #Te restan el dinero por tener propiedades
        mensajePropietats = f"Al jugador le toca pagar {pagar} por sus propiedades"
        actualizarHistorial(mensajePropietats)
    elif carta == "Ets escollit alcalde":
        totalPago = 0
        for jugadorDiferente in jugadores: #Recorremos la lista de jugadores
            if jugadorDiferente != jugador: #Si el jugador que mira, es diferente al que tiene la carta
                jugadores[jugadorDiferente]["Diners"] -= 50 #Se le restan 50 euros
                totalPago += 50 #Que se suman a esta variable
        jugadores[jugador]["Diners"] += totalPago #I luego se actualiza con el valor de totalPago
        mensajeAlcalde = f"El jugador {jugador} ha recibido {totalPago}€, enhorabuena por ser alcalde"
        actualizarHistorial(mensajeAlcalde)
    

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
    mensajeCaja = f"El jugador {jugador} ha recibido la carta: {carta}"
    actualizarHistorial(mensajeCaja)

    if carta == "Sortir de la presó":
        jugadores[jugador]["CartaSalirDeLaPrision"] = True
        jugadores[jugador]["CartasEspecials"].append("Sortir de la presó")
        mensajeSlavarPrision = f"El jugador {jugador} ha obtenido una carta para salir de la prisión !"
        actualizarHistorial(mensajeSlavarPrision)
    elif carta == "Error de la banca, guanyes 150€":
        jugadores[jugador]["Diners"] += 150
        mensajeErrorBanca = f"El jugador {jugador} ha obtenido 150€ gracias a un error de la banca !"
        actualizarHistorial(mensajeErrorBanca)
    elif carta == "Despeses mèdiques, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
        mensajeMedico = f"El jugador {jugador} le ha tocado pagar 50€ a sanidad !"
        actualizarHistorial(mensajeMedico)
    elif carta == "Despeses escolars, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
        mensajeEscuela = f"El jugador {jugador} le ha tocado pagar 50€ a educación"
        actualizarHistorial(mensajeEscuela)
    elif carta == "Reparacions al carrer, pagues 40€":
        jugadores[jugador]["Diners"] -= 40
        mensajeComunidad = f"El jugador {jugador} tiene que aportar 40€ a la comunidad"
        actualizarHistorial(mensajeComunidad)
    elif carta == "Concurs de bellesa, guanyes 10€":
        jugadores[jugador]["Diners"] += 10
        mensajeBelleza = f"El jugador {jugador} le han dado un premio por su belleza, recibe 10€"
        actualizarHistorial(mensajeBelleza)
    elif carta == "Anar a la presó":
        if jugadores[jugador]["EstaEnPrisión"] == False:
            return directoPrision(jugador)
    
def buscaPosicion(nombreCasilla):
    for i,Casilla in enumerate(calles):
        if calles[Casilla] == nombreCasilla:
            posicion = i
            return posicion
        else:
            return "No se ha encontrado la posicion"

#Esta tengo que revisarla
"""def buscaPosicion(nombreCasilla):
    for i, "Nombre", in enumerate(calles):
        if calles["Nombre"] == nombreCasilla:
            return i
        return "No se ha encontrado la posición"""
       

