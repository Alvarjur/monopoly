import random
import os

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def seguirEnPrision(jugador):
    dado1, dado2, totalDado = tirarDados()

    if jugadores[jugador]["EstaEnPrision"] == True:
        if dado1 == dado2:
            jugadores[jugador]["EstaEnPrision"] = False
            actualizarHistorial(f"  Los dados son '{dado1}' y '{dado2}', sale de prisión!")
            #return moverJugador(jugador) #NO SÉ SI EN EL MISMO TURNO EN EL QUE TIRA LOS DADOS SE PODRÍA MOVER, SI ES QUE SÍ, DESCOMENTAR ESTA LÍNEA
            return None
        else:
            actualizarHistorial(f"  Los dados son '{dado1}' y '{dado2}', no han coincidido")

        if jugadores[jugador]["TurnosPrision"] < 3:

            jugadores[jugador]["TurnosPrision"] += 1
            if jugadores[jugador]["TurnosPrision"] == 1:
                actualizarHistorial(f"  '{jugador.capitalize()}' ha pasado {jugadores[jugador]['TurnosPrision']} turno en prisión")
            else:
                actualizarHistorial(f"  '{jugador.capitalize()}' ha pasado {jugadores[jugador]['TurnosPrision']} turnos en prisión")

            

            
        else:
            jugadores[jugador]["EstaEnPrision"] = False
            actualizarHistorial(f"  '{jugador.capitalize()}' sale de prisión tras 3 turnos!")

def pagarABanca(jugador, dinero, motivo=""):
    """Esta funcion se puede llamar con el argumento 'jugador' como ('V') o ('vermell')"""
    global banca

    if len(jugador) == 1:
        if jugador == "V":
            jugador = "vermell"
        elif jugador == "G":
            jugador = "groc"
        elif jugador == "T":
            jugador = "taronja"
        elif jugador == "B":
            jugador = "blau"


    if jugadores[jugador]["Diners"] > dinero:
        jugadores[jugador]["Diners"] -= dinero
        banca += dinero
        actualizarHistorial(f"'{jugador.capitalize()}' ha pagado '{dinero}' a la banca {motivo}")
    else:
        bancaRota(videojugador=jugador)

def buscarIndexCasilla(jugador):
    """Esta función se puede llamar con un parámetro que sea ('Vermell') o ('V')
    Devuelve el index en el array de calles y también devuelve el diccionario de la calle en la que está el jugador"""

    if len(jugador) > 0:
        jugador = jugador.lower()

    if jugador == "vermell":
        player = "V"
    elif jugador == "blau":
        player = "B"
    elif jugador == "groc":
        player = "G"
    elif jugador == "taronja":
        player = "T"

    for calle in calles:
        if player in calle["Ocupacion"]: 
            return calles.index(calle), calle
        
def pagarCasillaDeJugador(jugador):
    """El parámetro de esta funcion tiene que ser la incial del jugador ('V') por ejemplo"""
    if jugador == "V":
        player = "vermell"
    elif jugador == "B":
        player = "blau"
    elif jugador == "T":
        player = "taronja"
    elif jugador == "G":
        player = "groc"

    valorAPagar = 0

    for calle in calles:
        if jugador in calle["Ocupacion"]:
            if calle["Nombre"] not in jugadores[player]["Propiedades"]:
                for videojugador in jugadores:
                    if calle["Nombre"] in jugadores[videojugador]["Propiedades"]:
                        valorAPagar += jugadores[videojugador]["Propiedades"][calle["Nombre"]]["Casas"] * calle["LlCasa"]
                        valorAPagar += jugadores[videojugador]["Propiedades"][calle["Nombre"]]["Hoteles"] * calle["LlHotel"]

                        actualizarHistorial(f"  '{player.capitalize()}' tiene que pagar {valorAPagar}")
                        imprimir_tablero(calles)

                        if jugadores[player]["Diners"] > valorAPagar:
                            jugadores[player]["Diners"] -= valorAPagar
                            jugadores[videojugador]["Diners"] += valorAPagar

                            actualizarHistorial(f"  '{player.capitalize()}' ha pagado '{valorAPagar}' a '{videojugador.capitalize()}'")
                            imprimir_tablero(calles)
                            return

                        else:
                            print(f"  '{player}' está en bancarrota")
                            bancaRota(videojugador=player)
                            return "Bancarrota"

def moverJugador(jugador):

    callesEspeciales = ["Sort", "Sort2", "Anr pró", "Caixa", "Caixa2"]
    if jugador == "V":
        player = "vermell"
    elif jugador == "B":
        player = "blau"
    elif jugador == "G":
        player = "groc"
    elif jugador == "T":
        player = "taronja"

    if jugadores[player]["EstaEnPrision"] == True:
        seguirEnPrision(player)
        return None

    dado1, dado2, totalDado = tirarDados()

    for calle in calles:

        if jugador in calle["Ocupacion"]:
            
            casillaAlLlamar = calles.index(calle)
            #print(casillaAlLlamar)
            if casillaAlLlamar + totalDado >= len(calles):
                casillaAlLlamar -= 24
                print(casillaAlLlamar)
            #print(casillaAlLlamar + totalDado)
            print(casillaAlLlamar + totalDado)
            print(len(calles))
            calle["Ocupacion"].remove(jugador)
            calles[casillaAlLlamar + totalDado]["Ocupacion"].extend(jugador)
            nuevaCalle = calles[casillaAlLlamar + totalDado]

            actualizarHistorial(f"  Los dados han dado: '{dado1}' y '{dado2}' con un total de '{totalDado}'")
            actualizarHistorial(f"  '{player.capitalize()}' se ha movido hasta '{calles[casillaAlLlamar + totalDado]['Nombre']}'")

            clearScreen()
            imprimir_tablero(calles)

            break

    if pagarCasillaDeJugador(jugador) == "Bancarrota":
        return None

    #AQUÍ SE PUEDE HACER UN BUCLE QUE ABARCE EL RESTO DEL CÓDIGO DE ESTA FUNCION Y DURE HASTA QUE SE ACABE EL TURNO DEL JUGADOR O LE DE A PASS


    elif nuevaCalle["Nombre"] not in callesEspeciales:
        while True:
            clearScreen()
            imprimir_tablero(calles)
            print(f"Qué quieres hacer? (1. Passar / 2. Comprar Terreny / 3. Comprar Casa / 4. Comprar hotel / 5. Mirar precios / 6. Precio al banco / 7. Precio a un jugador / 8. Vender al banco / 9. Vender a un jugador)")
            eleccion = str(input())
            if eleccion == "1":
                jugadores[player]["Torn"] = False
                actualizarHistorial(f"  '{player.capitalize()}' pasa de turno.")
                return
            
            elif eleccion == "2":
                anadirCasa(player, nuevaCalle["Nombre"])
            elif eleccion == "3":
                if nuevaCalle["Nombre"] in jugadores[player]["Propiedades"]:
                    anadirCasa(player, nuevaCalle["Nombre"])
                else:
                    print(f"Error, '{nuevaCalle['Nombre']}' no es de tu propiedad")
            elif eleccion == "4":
                anadirHotel(player, nuevaCalle["Nombre"])
            elif eleccion == "5":
                pass
            
            elif eleccion == "6":
                valorTotal = 0
                for propiedad in jugadores[player]["Propiedades"]:
                    for calle in calles:
                        if calle["Nombre"] == propiedad:
                            for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                if construccion == "Casas":
                                    valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                if construccion == "Hoteles":
                                    valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                valorTotal += valorInd
                valorTotal = (valorTotal * 50) // 100
                actualizarHistorial(f"  Ganarías al vender tus propiedades al banco: {valorTotal}")

            elif eleccion == "7":
                valorTotal = 0
                for propiedad in jugadores[player]["Propiedades"]:
                    for calle in calles:
                        if calle["Nombre"] == propiedad:
                            for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                if construccion == "Casas":
                                    valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                if construccion == "Hoteles":
                                    valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                valorTotal += valorInd
                valorTotal = (valorTotal * 90) // 100 #Al ser otro jugador el comprador, es un 90% de lo que pagó el vendedor
                actualizarHistorial(f"  Ganarías al vender tus propiedades a un jugador: {valorTotal}")

            elif eleccion == "8":
                valorTotal = 0
                for propiedad in jugadores[player]["Propiedades"]:
                    for calle in calles:
                        if calle["Nombre"] == propiedad:
                            for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                if construccion == "Casas":
                                    valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                if construccion == "Hoteles":
                                    valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                valorTotal += valorInd
                valorTotal = (valorTotal * 50) // 100
                jugadores[player]["Diners"] += valorTotal
                jugadores[player]["Propiedades"] = {}
                actualizarHistorial(f"  {player.capitalize()} ha vendido sus propiedades al banco por {valorTotal}")
                
            elif eleccion == "9":
                jugadoresNoTurno = []
                for videojugador in jugadores:
                    if jugadores[videojugador]["Torn"] == False:
                        jugadoresNoTurno.append(videojugador)
                valorTotal = 0
                for propiedad in jugadores[player]["Propiedades"]:
                    for calle in calles:
                        if calle["Nombre"] == propiedad:
                            for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                if construccion == "Casas":
                                    valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                if construccion == "Hoteles":
                                    valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion]
                                valorTotal += valorInd
                valorTotal = (valorTotal * 90) // 100
                while True:
                    print(f"A quién quieres venderle?: " + ", ".join(jugadoresNoTurno))
                    comprador = input()
                    comprador = comprador.lower()
                    if comprador in jugadoresNoTurno:
                        break
                if comprador in jugadoresNoTurno:
                    if jugadores[comprador]["Diners"] >= valorTotal:
                            jugadores[comprador]["Diners"] -= valorTotal
                            jugadores[player]["Diners"] += valorTotal
                            propiedadesJugador = jugadores[player]["Propiedades"].items()
                            jugadores[comprador]["Propiedades"].update(propiedadesJugador)
                            jugadores[player]["Propiedades"] = {}
                            actualizarHistorial(f"  {player.capitalize()} ha vendido sus propiedades a {comprador.capitalize()} por {valorTotal}")

    else:
        #print(nuevaCalle["Nombre"])
        #input()
        if nuevaCalle["Nombre"] == "Sort2" or nuevaCalle["Nombre"] == "Sort":
            cartaSort(player)
        #HACER EL RESTO DE LAS CASILLAS ESPECIALES
        elif nuevaCalle["Nombre"] == "Caixa" or nuevaCalle["Nombre"] == "Caixa2":
            cartaCaixa(player)
       
        elif nuevaCalle["Nombre"] == "Anr pró":
            directoPrision(player)

        

        imprimir_tablero(calles)
        #Hacer que se mueva y eso
    
    

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
        mostrarInformacionJugador.append(f"Especial: {', '.join(jugadores[jugador]['CartasEspecials'])}")
        mostrarInformacionJugador.append("")
    
    #for mensaje in mostrarInformacionJugador:
    #    print(mensaje)

    return mostrarInformacionJugador

def anadirCasa(jugador, calle): #Esta función se puede usar para añadir una casa o para el momento de comprar la casilla.
    while True:
        clearScreen()
        imprimir_tablero(calles)
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
                    actualizarHistorial(f"  Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                    return None

            if calle in jugadores[key]["Propiedades"].keys():
                if jugadores[key]["Propiedades"][calle]["Casas"] >= 4:
                    actualizarHistorial(f"  Error: Se pueden tener cómo máximo 4 casas, compra un hotel.")
    
                elif jugadores[key]["Diners"] >= dicCalle["CmpCasa"]: #Si tiene dinero suficiente para comprar una casa.
                    jugadores[key]["Propiedades"][calle]["Casas"] += 1
                    jugadores[key]["Diners"] -= dicCalle["CmpCasa"] #Resta el dinero de la casa al dinero del jugador

                    actualizarHistorial(f"  '{jugador.capitalize()}' compra una casa en '{calle}'")
                    return None
                else:
                    actualizarHistorial(f"  Error: Una casa cuesta {dicCalle['CmpCasa']} y tienes {jugadores[key]['Diners']}")
                    return None
            else:
                #print(jugadores[key]["Diners"])
                #print(dicCalle["CmpTrrny"])
                if jugadores[key]["Diners"] >= dicCalle["CmpTrrny"]:
                    #print("wawa")
                    jugadores[key]["Propiedades"][calle] = dic
                    actualizarHistorial(f"  '{jugador.capitalize()}' ha comprado el terreno '{calle}'")
                    jugadores[key]["Diners"] -= dicCalle["CmpTrrny"] #Resta el dinero de la casilla al dinero del jugador
                    imprimir_tablero(calles)
                    return None
                else:
                    actualizarHistorial(f"  Error: La casilla cuesta {dicCalle['CmpTrrny']} y tienes {jugadores[key]['Diners']}")
                    print(f"Error: La casilla cuesta {dicCalle['CmpTrrny']} y tienes {jugadores[key]['Diners']}")
                    return None

        else:
            actualizarHistorial(f"  Error: '{calle}' no se puede comprar.")
            return None

def anadirHotel(jugador, calle):
    clearScreen()
    imprimir_tablero(calles)
    if calle != "Parking" and calle != "Sort" and calle != "Anr pró" and calle != "Caixa" and calle != "Caixa2" and calle != "Sort2" and calle != "Presó":
        dic = {
            "Casas" : 0,
            "Hoteles" : 0
        }

        key = jugador

        for street in calles:
            if calle in street.values():
                dicCalle = street

        if dicCalle["Nombre"] not in jugadores[jugador]["Propiedades"]:
            print(f"Error: Esta casilla no es de tu propiedad")
            actualizarHistorial(f"  Error: Esta casilla no es de tu propiedad")

        for player in jugadores.keys():
            dicComprobar = jugadores[player]["Propiedades"]
            
            if calle in dicComprobar and player != jugador:
                actualizarHistorial(f"  Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                return None

        if calle in jugadores[key]["Propiedades"].keys():
            if jugadores[key]["Propiedades"][calle]["Casas"] >= 2:
                if jugadores[key]["Propiedades"][calle]["Hoteles"] < 3: #Se comprueba que el jugador no tenga ya 2 hoteles en esa casilla.
                    if jugadores[key]["Diners"] >= dicCalle["CmpHotel"]:
                        jugadores[key]["Propiedades"][calle]["Casas"] -= 2
                        jugadores[key]["Propiedades"][calle]["Hoteles"] += 1
                        actualizarHistorial(f"  '{jugador.capitalize()}' compra un hotel en {calle}")
                    else:
                        actualizarHistorial(f"  Error: Un hotel cuesta {dicCalle['CmpHotel']} y tienes {jugadores[key]['Diners']}")
                        return None
                else:
                    actualizarHistorial(f"  Error: Ya tienes 2 hoteles en {calle}.")
                    return None
            else:
                actualizarHistorial(f"  Error: Para comprar un hotel hacen falta al menos 2 casas.")
                return None
  
    else:
        actualizarHistorial(f"  Error: '{calle}' no se puede comprar.")
        return None

jugadoresEnBancarrota = []

def bancaRota(rendirse = False, videojugador=""):
    global banca
    for jugador in jugadores.keys():
        if (jugadores[jugador]["Diners"] <= 0 and jugador not in jugadoresEnBancarrota and jugadores[jugador]["Torn"] == True) or videojugador in jugadores.keys():

            if videojugador in jugadores.keys(): #ESTO ES PARA QUE EN LA FUNCION DE PAGAR ALQUILER SE PUEDA LLAMAR A ESTA FUNCION AUNQUE EL DINERO NO SEA 0
                jugador = videojugador

            actualizarHistorial(f"'  {jugador.capitalize()}' está en bancarrota")
            imprimir_tablero(calles)

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
                    actualizarHistorial(f"  {jugador.capitalize()} ha vendido sus propiedades a la banca por {ValorAlVender}")
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

                        actualizarHistorial(f"  '{jugador.capitalize()}' ha vendido sus propiedades a '{comprador.capitalize()}' por '{ValorAlVender}'")
                        break
                    else:
                        print(f"'{comprador.capitalize()}' no tiene dinero")
                        actualizarHistorial(f"  '{comprador.capitalize()}' no tiene suficiente dinero")
                        
                elif eleccion == "3" or rendirse == True:
                    jugadores[jugador]["Propiedades"] = {}
                    jugadoresEnBancarrota.append(jugador)
                    actualizarHistorial(f"  '{jugador.capitalize()}' se ha dado en bancarrota, no jugará más")
                    return
            

def actualizarHistorial(info): #Esta función es la que usaremos para recoger todos los mensajes, lo malo es que para cada uno de los eventos, se tiene que llamar dentro de las funciones 
                              #I hacer .append en todas las funciones de evento

    historial.insert(0, info)
    while len(historial) <= 13:
        historial.append("")
    while len(historial) > 14:
        historial.pop(-1)
    


def imprimirCasasHoteles(posicionCasilla):
    if posicionCasilla == 40: #Obviamente no hay ninguna casilla 40, esto es para las lineas que no necesitan pasar por todo ese código
        return "+------------" * 5

    for jugador in jugadores:
        if calles[posicionCasilla]["Nombre"] in jugadores[jugador]["Propiedades"]:
            txt = f"+------{jugador[0].capitalize()}-" + str(jugadores[jugador]["Propiedades"][calles[posicionCasilla]["Nombre"]]["Casas"]) + "C" + str(jugadores[jugador]["Propiedades"][calles[posicionCasilla]["Nombre"]]["Hoteles"]) + "H"
            return txt
         

    return "+------------"

def desordenarDiccionario(dic):
    items = list(dic.items())

    random.shuffle(items)

    dicDesordenado = dict(items)

    return dicDesordenado

def inicioPartida(players):
    global jugadores

    playersDesordenado = desordenarDiccionario(players)
    jugadores = playersDesordenado
    listaJugadores = []
    
    for key in jugadores:
        listaJugadores.append(key)

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
    return inicialesJugadores

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


#FUNCIONES DE CASILLAS ESPECIALES
def directoPrision(jugador):
    """El parámetro (jugador) de esta funcion tiene que ser ('vermell') por ejemplo, no ('V')"""

    if jugador == "vermell":
        player = "V"
    elif jugador == "blau":
        player = "B"
    elif jugador == "groc":
        player = "G"
    elif jugador == "taronja":
        player = "T"

    #Primero te envian directo a prisión y se actualizan tus valores 
    mensajePrision = f"  El jugador '{jugador.capitalize()}' va directo a prisión"
    actualizarHistorial(mensajePrision)

    # jugadores[jugador]["Posicio"] = 18
    jugadores[jugador]["EstaEnPrision"] = True
    jugadores[jugador]["TurnosPrision"] = 0

    posActual, calleActual = buscarIndexCasilla(jugador)
    calles[posActual]["Ocupacion"].remove(player)
    calles[18]["Ocupacion"].extend(player)     #18 es el index de la prisión.

  
    #Aqui entra en juego si tiene o no la carta
    #Si la tienes puedes seguir jugando y se actualizan los valores del diccionario
    if "Sortir de la presó" in jugadores[jugador]["CartasEspecials"]:
        jugadores[jugador]["CartasEspecials"].remove("Sortir de la presó")
        jugadores[jugador]["EstaEnPrision"] = False
        mensajeSiCarta = f"  '{jugador.capitalize()}' ha usado la carta 'Sortir de la presó'"
        actualizarHistorial(mensajeSiCarta)

    else:#Si no la tienes vas a la carcel, y si es tu turno se suma 1 a la variable turnos en prision

        jugadores[jugador]["EstaEnPrision"] = True
        mensajeNoCarta = f"  '{jugador.capitalize()}' no tiene la carta para salvarse, está en prisión!"
        actualizarHistorial(mensajeNoCarta)

        if jugadores[jugador]["Torn"] == True:  # Si es el turno del jugador se va actualizando el valor de turnos en prisión 

            jugadores[jugador]["TurnosPrision"] += 1 #Aquí se actualizan
            mensajeTurnosPrision = f"  '{jugador.capitalize()}' ha pasado {jugadores[jugador]['TurnosPrision']} turno en prision"
            actualizarHistorial(mensajeTurnosPrision)

def cartaSort(jugador):
    if jugador == "vermell":
        player = "V"
    elif jugador == "blau":
        player = "B"
    elif jugador == "groc":
        player = "G"
    elif jugador == "taronja":
        player = "T"

    cartasSuerte = [
        "Sortir de la presó",
        "Anar a la presó",
        "Anar a la sortida",
        "Anar tres espais enrere",
        "Reparacions propietats",
        "Ets escollit alcalde"
    ]

    carta = random.choice(cartasSuerte)
    mensajeSuerte = f"  '{jugador.capitalize()}' recibió la carta: '{carta}'"
    actualizarHistorial(mensajeSuerte)

    if carta == "Sortir de la presó": #Basicamente est es actualizar los valores del diccionario
        jugadores[jugador]["CartaSalirDeLaPrision"] = True
        jugadores[jugador]["CartasEspecials"].append(carta)
        mensajeSalirPrision = f"  '{jugador.capitalize()}' podrá salir de la cárcel!"
        actualizarHistorial(mensajeSalirPrision)

    elif carta == "Anar a la presó": #Aqui se usa la funcion ir a la prision
         return directoPrision(jugador)
    
    elif carta == "Anar a la sortida": #Vuelves a la casilla de salida que es la numero 12 (tambien se podria usar con el nomnbre (?))
        posActual, calleActual = buscarIndexCasilla(jugador)
        calles[posActual]["Ocupacion"].remove(player)
        calles[12]["Ocupacion"].extend(player) 
        mensajeSalida = f"  '{jugador.capitalize()}' vuelve a la casilla de salida!"
        actualizarHistorial(mensajeSalida)

    elif carta == "Anar tres espais enrere":


        posActual, calleActual = buscarIndexCasilla(jugador)

        posNueva = posActual - 3

        if posNueva < 0:
            posNueva + len(calles)

        calles[posActual]["Ocupacion"].remove(player)
        calles[posNueva]["Ocupacion"].extend(player)

        mensajeTresEspacios = f"  El jugador retrocede 3 casillas hasta {calles[posNueva]['Nombre']}"
        actualizarHistorial(mensajeTresEspacios)

    elif carta == "Reparacions propietats":
        if len(jugadores[jugador]["Propiedades"]) > 0:
            totalCasas = 0
            totalHoteles = 0
            for propiedad in jugadores[jugador]["Propiedades"]:
                print(propiedad)
                input()
                totalCasas += jugadores[jugador]["Propiedades"][propiedad]["Casas"]
                totalHoteles += jugadores[jugador]["Propiedades"][propiedad]["Hoteles"]
            totalAPagar = (25 * totalCasas) + (100 * totalHoteles)
            pagarABanca(jugador, totalAPagar, "por reparaciones")

        else:
            actualizarHistorial(f"  '{jugador.capitalize()}' no tiene propiedades")

    elif carta == "Ets escollit alcalde":
        totalPago = 0
        for jugadorDiferente in jugadores: #Recorremos la lista de jugadores
            if jugadorDiferente != jugador: #Si el jugador que mira, es diferente al que tiene la carta
                jugadores[jugadorDiferente]["Diners"] -= 50 #Se le restan 50 euros
                totalPago += 50 #Que se suman a esta variable
        jugadores[jugador]["Diners"] += totalPago #I luego se actualiza con el valor de totalPago
        mensajeAlcalde = f"  '{jugador.capitalize()}' ha recibido {totalPago}€ al ser alcalde!"
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
    mensajeCaja = f"  A '{jugador.capitalize()}' le ha tocado: '{carta}'"
    actualizarHistorial(mensajeCaja)

    if carta == "Sortir de la presó":
        jugadores[jugador]["CartasEspecials"].append("Sortir de la presó")
        mensajeSlavarPrision = f"  '{jugador.capitalize()}' ha obtenido una carta para salir de la prisión!"
        actualizarHistorial(mensajeSlavarPrision)

    elif carta == "Error de la banca, guanyes 150€":
        jugadores[jugador]["Diners"] += 150
        mensajeErrorBanca = f"  '{jugador.capitalize()}' ha obtenido 150€ gracias a un error de la banca!"
        actualizarHistorial(mensajeErrorBanca)

    elif carta == "Despeses mèdiques, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
        mensajeMedico = f"  A '{jugador.capitalize()}' le ha tocado pagar 50€ a sanidad!"
        actualizarHistorial(mensajeMedico)

    elif carta == "Despeses escolars, pagues 50€":
        jugadores[jugador]["Diners"] -= 50
        mensajeEscuela = f"  A '{jugador.capitalize()}' le ha tocado pagar 50€ a educación"
        actualizarHistorial(mensajeEscuela)

    elif carta == "Reparacions al carrer, pagues 40€":
        jugadores[jugador]["Diners"] -= 40
        mensajeComunidad = f"  '{jugador.capitalize()}' tiene que aportar 40€ a la comunidad"
        actualizarHistorial(mensajeComunidad)

    elif carta == "Concurs de bellesa, guanyes 10€":
        jugadores[jugador]["Diners"] += 10
        mensajeBelleza = f"  A '{jugador.capitalize()}' le han dado un premio por su belleza, recibe 10€"
        actualizarHistorial(mensajeBelleza)

    elif carta == "Anar a la presó":
        if jugadores[jugador]["EstaEnPrision"] == False:
            return directoPrision(jugador)
        
def monopoly():
    orden = inicioPartida(jugadores)
    
    while True:
        for jugador in orden:
            if jugador == "V":
                player = "vermell"
            elif jugador == "B":
                player = "blau"
            elif jugador == "T":
                player = "taronja"
            elif jugador == "G":
                player = "groc"
            jugadores[player]["Torn"] = True
            clearScreen()
            actualizarHistorial(f"> Turno de {player.capitalize()}")
            imprimir_tablero(calles)
            moverJugador(jugador)
            actualizarHistorial(f"")

            clearScreen()
            imprimir_tablero(calles)
            input("Aceptar.")
            jugadores[player]["Torn"] = False


calles = [
    {"Nombre": "Parking", "Ocupacion": []},         #0
    {"Nombre": "Urquinoa", "Ocupacion": [], "LlCasa": 30, "LlHotel": 25, "CmpTrrny": 70, "CmpCasa": 400, "CmpHotel": 290},        #1
    {"Nombre": "Fontan", "Ocupacion": [], "LlCasa": 30, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 425, "CmpHotel": 300},          #2
    {"Nombre": "Sort", "Ocupacion": []},            #3
    {"Nombre": "Rambles", "Ocupacion": [], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 450, "CmpHotel": 310},         #4
    {"Nombre": "Pl.Cat", "Ocupacion": [], "LlCasa": 35, "LlHotel": 30, "CmpTrrny": 70, "CmpCasa": 475, "CmpHotel": 325},          #5
    {"Nombre": "Anr pró", "Ocupacion": []},         #6
    {"Nombre": "Angel", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 500, "CmpHotel": 330},           #7
    {"Nombre": "Augusta", "Ocupacion": [], "LlCasa": 40, "LlHotel": 35, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 340},         #8
    {"Nombre": "Caixa", "Ocupacion": []},           #9
    {"Nombre": "Balmes", "Ocupacion": [], "LlCasa": 50, "LlHotel": 40, "CmpTrrny": 80, "CmpCasa": 550, "CmpHotel": 350},          #10
    {"Nombre": "Gracia", "Ocupacion": [], "LlCasa": 50, "LlHotel": 50, "CmpTrrny": 80, "CmpCasa": 525, "CmpHotel": 360},          #11
    {"Nombre": "Sortida", "Ocupacion": []},         #12
    {"Nombre": "Lauria", "Ocupacion": [], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 200, "CmpHotel": 250},          #13
    {"Nombre": "Rosell", "Ocupacion": [], "LlCasa": 10, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 225, "CmpHotel": 255},          #14
    {"Nombre": "Sort2", "Ocupacion": []},           #15
    {"Nombre": "Marina", "Ocupacion": [], "LlCasa": 15, "LlHotel": 15, "CmpTrrny": 50, "CmpCasa": 250, "CmpHotel": 260},          #16
    {"Nombre": "Consell", "Ocupacion": [], "LlCasa": 15, "LlHotel": 20, "CmpTrrny": 50, "CmpCasa": 275, "CmpHotel": 265},         #17
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
        "Propiedades": {},
        "Diners":2000,
        "CartasEspecials": [],
        "EstaEnPrision": False,
        "TurnosPrision": 0
    },
    "groc":{
        "Torn":False,
        "Propiedades":{},
        "Diners":2000,
        "CartasEspecials": [],
        "EstaEnPrision": False,
        "TurnosPrision": 0
    },
    "taronja":{
         "Torn":False,
         "Propiedades":{},
         "Diners":2000,
         "CartasEspecials": [],
         "EstaEnPrision": False,
         "TurnosPrision": 0
     },
    "vermell":{
        "Torn":False,
        "Propiedades":{},
        "Diners":2000,
        "CartasEspecials": [],
        "EstaEnPrision": False,
        "TurnosPrision": 0
    }
}

banca = 1000000

historial = [
    "","","","","","","","","","","","","",""
]



# AQUÍ INICIA EL JUEGO

monopoly()

#FALTA HACER QUE GANE 200 CADA VEZ QUE PASA POR LA SALIDA.
#FALTAN LOS TRUCOS
#FALTA LO DE PONER LOS PRECIOS EN MEDIO DE LA PANTALLA