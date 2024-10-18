import random
import json
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

    calles[12]['Ocupacion'].extend(inicialesJugadores) #calles[12] es la casilla de salida
    #Verificar que establezca correctamente el orden y que inicialmente esten bien colocados
    return None

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

# Mi idea con el historial es que siempre tenga este número de valores, aunque estén vacíos y parezca que no haya nada (""), porque en el caso de que se borren valores dará error
# al intentar buscar el valor en el index 13 por ejemplo y esté fuera del rango del array
#Se podria inicializar en historial en historial = "" e ir actualizandolo ? #No porque solo tendría un valor, en todo caso sería historial = ["","",""...hasta 14] 

#Luego funciones que decidan que acción toma el jugador en su turno
    #una funcion que se llame def turnoAccion()
        #Hacer una lista de str con las opciones que puede hacer y realizarlas DDD
#Esta variable almacena el array completo del historial que sera <= 10

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

    return None  #En un futuro lo suyo sería que las funciones devolvieran none pero que añadan una línea al historial,
                              #haría falta una función que mantenga la cantidad de valores del historial en 10, que elimine las antiguas y meta nuevas lineas.
                              # ^
                              #En teoria de esta forma ya estaría solucionado

def mostrar_lista_bonita(lista):
    lista_bonita = json.dumps(lista, indent=4)
    print(lista_bonita)

def mostrarInformacion(jugador):

    mostrarInformacionJugador = []

    for jugador in jugadores:
        mostrarInformacionJugador.append(f"Jugador {jugador}")
        mostrarInformacionJugador.append(f"Carrers: {jugadores[jugador]["Propiedades"]}")
        mostrarInformacionJugador.append(f"Diners: {jugadores[jugador]["Diners"]}")
        mostrarInformacionJugador.append(f"Especial: {jugadores[jugador]["Cartas especials"]}")
        mostrarInformacionJugador.append("")
    
    for mensaje in mostrarInformacionJugador:
        print(mensaje)


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

#cartaSort("groc")
#He tenido que cambiarlo todo para que se pudiera ver de forma automatica, en teoria así todos los mensajes son variables que se llevan a actualizarHistorial que es la función que lo maneja
#En teoria se van acumulando hasta que haya un total de 10, i luego se elimina el primero que sería el más antiguo. Es un poco tedioso de ver el código pero es la única forma que he tenido de soluciona
#Las funciones sería lo suyo que en vez de mostrar la información de la función con un print, se añadan al historial, no digo que lo hagas ahora es solo para tenerlo en mente