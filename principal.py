
import random
import os

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def trucs():
    global banca
    global skipTurnoA

    text = input("Que truco quieres utilizar ? [1. Ir a X casilla, 2. Añadir X casas, 3. Añadir X hoteles, 4. Siguiente X, 5. Dineros X, YY, 6. Dineros Banca]\n")
    
    #Truco para mover al jugador a una casilla deseada
    """ Para el primer truco se vamos a seleccionar al jugaor mediante un input
        - Una vez seleccioando se recorre la lista de calles, si la inicial de ese jugador esta en la 'calle', se eliminará de la ocupación
        - Se vuelve a recorrer el array de calles, esta vez para que coincida con la calle a la que nos queremos desplazar (desplazarJugador)
        - Comprobamos que el jugador seleccionado no se encuentre en la ocupación de destino, si no lo está, se añade mediante extend, para asegurar
          que aparezca al final, en caso de esa casilla estar ocupada
        - Se muestra el mensaje en el centro del tablero mediante la funcion actualizaHistorial"""
    if text == "1":
        callesEspeciales = ["Sort", "Sort2", "Anr pró", "Caixa", "Caixa2", "Presó", "Sortida", "Parking"]
        selectJugador = input("A que jugador quieres desplazar ? [1. Blau 2. Groc 3. Taronja 4. Vermell]\n") #Seleccionar al jugador mediante el numero establecido 
        
        #Jugador azul
        if selectJugador == "1": 
            desplazarJugador = input("A que casilla deseas desplazarlo ? \n") #Se desplaza hasta la casilla deseada (poner nombre exacto)
            for calle in calles :
                if "B" in calle["Ocupacion"]:
                    calle["Ocupacion"].remove("B")

            for calle in calles:
                if calle["Nombre"] == desplazarJugador:
                    if "B" not in calle["Ocupacion"]: #Esto creo que es redundante porque antes lo estoy eliminando en el anterior for
                        if desplazarJugador not in callesEspeciales:
                            calle["Ocupacion"].extend("B")
                            #jugadores["blau"]["Posicion"] = calle
                            actualizarHistorial(f"El jugador 'blau' se ha movido hasta la casilla {desplazarJugador}")
                        #Casilla evento
                        elif desplazarJugador in callesEspeciales:
                            if desplazarJugador == "Sort" or desplazarJugador == "Sort2":
                                calle["Ocupacion"].extend("B")
                                actualizarHistorial(f"El jugador 'blau' se ha movido hasta la casilla {desplazarJugador}")
                                cartaSort("blau")
                            elif desplazarJugador == "Anr pró":
                                calle["Ocupacion"].extend("B")
                                actualizarHistorial(f"El jugador 'blau' se ha movido hasta la casilla {desplazarJugador}")
                                directoPrision("blau")
                            elif desplazarJugador == "Caixa" or desplazarJugador == "Caixa2":
                                calle["Ocupacion"].extend("B")
                                actualizarHistorial(f"El jugador 'blau' se ha movido hasta la casilla {desplazarJugador}")
                                cartaCaixa("blau")

        #Jugador amarillo       
        if selectJugador == "2":
            desplazarJugador = input("A que casilla deseas desplazarlo ?\n")
            for calle in calles :
                if "G" in calle["Ocupacion"]:
                    calle["Ocupacion"].remove("G")

            for calle in calles:
                if calle["Nombre"] == desplazarJugador:
                    if "G" not in calle["Ocupacion"]:
                        if desplazarJugador not in callesEspeciales:
                            calle["Ocupacion"].extend("G")
                            actualizarHistorial(f"El jugador 'Groc' se ha movido hasta la casilla {desplazarJugador}")
                        #Casilla evento
                        elif desplazarJugador in callesEspeciales:
                            if desplazarJugador == "Sort" or desplazarJugador == "Sort2":
                                calle["Ocupacion"].extend("G")
                                actualizarHistorial(f"El jugador 'Groc' se ha movido hasta la casilla {desplazarJugador}")
                                cartaSort("groc")
                            elif desplazarJugador == "Anr pró":
                                calle["Ocupacion"].extend("G")
                                actualizarHistorial(f"El jugador 'Groc' se ha movido hasta la casilla {desplazarJugador}")
                                directoPrision("groc")
                            elif desplazarJugador == "Caixa" or desplazarJugador == "Caixa2":
                                calle["Ocupacion"].extend("G")
                                actualizarHistorial(f"El jugador 'Groc' se ha movido hasta la casilla {desplazarJugador}")
                                cartaCaixa("groc")
        #Jugador naranja
        if selectJugador == "3":
            desplazarJugador = input("A que casilla deseas desplazarlo ?\n") 
            for calle in calles :
                if "T" in calle["Ocupacion"]:
                    calle["Ocupacion"].remove("T")
            for calle in calles:
                if calle["Nombre"] == desplazarJugador:
                    if "T" not in calle["Ocupacion"]:
                        if desplazarJugador not in callesEspeciales:
                            calle["Ocupacion"].extend("T")
                            actualizarHistorial(f"El jugador 'Taronja' se ha movido hasta la casilla {desplazarJugador}")
                        #Casillas de evento
                        elif desplazarJugador in callesEspeciales:
                            if desplazarJugador == "Sort" or desplazarJugador == "Sort2":
                                calle["Ocupacion"].extend("T")
                                actualizarHistorial(f"El jugador 'Taronja' se ha movido hasta la casilla {desplazarJugador}")
                                cartaSort("taronja")
                            elif desplazarJugador == "Anr pró":
                                calle["Ocupacion"].extend("T")
                                actualizarHistorial(f"El jugador 'Taronja' se ha movido hasta la casilla {desplazarJugador}")
                                directoPrision("taronja")
                            elif desplazarJugador == "Caixa" or desplazarJugador == "Caixa2":
                                calle["Ocupacion"].extend("T")
                                actualizarHistorial(f"El jugador 'taronja' se ha movido hasta la casilla {desplazarJugador}")
                                cartaCaixa("taronja")
        #Jugador rojo      
        elif selectJugador == "4":
            desplazarJugador = input("A que casilla deseas desplazarlo ? \n") 
            for calle in calles :
                if "V" in calle["Ocupacion"]:
                    calle["Ocupacion"].remove("V")
            for calle in calles:
                if calle["Nombre"] == desplazarJugador:
                    if "V" not in calle["Ocupacion"]:
                        if desplazarJugador not in callesEspeciales:
                            calle["Ocupacion"].extend("V")
                            actualizarHistorial(f"El jugador 'Vermell' se ha movido hasta la casilla {desplazarJugador}")
                        #Casillas de evento
                        elif desplazarJugador in callesEspeciales:
                            if desplazarJugador == "Sort" or desplazarJugador == "Sort2":
                                calle["Ocupacion"].extend("V")
                                actualizarHistorial(f"El jugador 'Vermell' se ha movido hasta la casilla {desplazarJugador}")
                                cartaSort("vermell")
                            elif desplazarJugador == "Anr pró":
                                calle["Ocupacion"].extend("V")
                                actualizarHistorial(f"El jugador 'Vermell' se ha movido hasta la casilla {desplazarJugador}")
                                directoPrision("vermell")
                            elif desplazarJugador == "Caixa" or desplazarJugador == "Caixa2":
                                calle["Ocupacion"].extend("V")
                                actualizarHistorial(f"El jugador 'Vermell' se ha movido hasta la casilla {desplazarJugador}")
                                cartaCaixa("vermell")

    #TRUCO PARA AÑADIR CASAS A UN JUGADOR
    elif text == "2":
        selectJugadorCasa = input("A que jugador quieres anadir (1 - 4) casas ? [1. Blau, 2. Groc, 3. Taronja, 4. Vermell]\n")
        #Jugador Azul
        if selectJugadorCasa == "1":
            calleCasa = input("A que calle quieres añadrile una casa\n")
            numeroAnadirCasas = int(input(" Cuantas casas quieres añadir ? [1 - 4]\n"))
            if 1 <= numeroAnadirCasas <= 4: #En este caso el numero seleccionado debe estar entre 1 i 4
                if calleCasa in jugadores["blau"]["Propiedades"]: #Se comprueba que el jugador seleccionado tenga la calle (propiedad) seleccionada
                    #Aqui inicio el diccionario para añadir Casas en propiedades
                    if "Casas" not in jugadores["blau"]["Propiedades"][calleCasa]:
                        jugadores["blau"]["Propidades"][calleCasa]["Casas"] = 0
                    jugadores["blau"]["Propiedades"][calleCasa]["Casas"] += numeroAnadirCasas #Se añade el numero de casas seleccionada a la calle seleccionada  
                    actualizarHistorial(f"Se han añadido {numeroAnadirCasas} casas") #Se actualiza el historial con el numero de casas añadidas en la propiedad
                else:
                    actualizarHistorial(f"No puedes añadir una casa porque no es de tu propiedad !") #Aun que se dispongan de trucos, solo funcionaran si esa propiedad es del jugador
            else:
                actualizarHistorial("No se pueden añadir mas de cuatro casas")
        #Jugador amarillo
        if selectJugadorCasa == "2":
            calleCasa = input("A que calle quieres añadrile una casa\n")
            numeroAnadirCasas = int(input(" Cuantas casas quieres añadir ? [1 - 4]\n"))
            if 1 <= numeroAnadirCasas <= 4:
                if calleCasa in jugadores["groc"]["Propiedades"]:
                    if "Casas" not in jugadores["groc"]["Propiedades"][calleCasa]:
                        jugadores["groc"]["Propiedades"][calleCasa]["Casas"] = 0
                    jugadores["groc"]["Propiedades"][calleCasa]["Casas"] += numeroAnadirCasas   
                    actualizarHistorial(f"Se han añadido {numeroAnadirCasas} casas")
                else:
                    actualizarHistorial(f"No puedes añadir una casa porque no es de tu propiedad !")
            else:
                actualizarHistorial("No se pueden añadir mas de cuatro casas")
        #Jugador naranja
        if selectJugadorCasa == "3":
            calleCasa = input("A que calle quieres añadrile una casa\n")
            numeroAnadirCasas = int(input(" Cuantas casas quieres añadir ? [1 - 4] "))
            if 1 <= numeroAnadirCasas <= 4:
                if calleCasa in jugadores["taronja"]["Propiedades"]:
                    if "Casas" not in jugadores["taronja"]["Propiedades"][calleCasa]:
                        jugadores["taronja"]["Propiedades"][calleCasa]["Casas"] = 0
                    jugadores["taronja"]["Propiedades"][calleCasa]["Casas"] += numeroAnadirCasas   
                    actualizarHistorial(f"Se han añadido {numeroAnadirCasas} casas")
                else:
                    actualizarHistorial(f"No puedes añadir una casa porque no es de tu propiedad !")
            else:
                actualizarHistorial("No se pueden añadir mas de cuatro casas")
        #Jugador rojo
        if selectJugadorCasa == "4":
            calleCasa = input("A que calle quieres añadrile una casa\n")
            numeroAnadirCasas = int(input(" Cuantas casas quieres añadir ? [1 - 4]\n"))

            if 1 <= numeroAnadirCasas <= 4:
                if calleCasa in jugadores["vermell"]["Propiedades"]:
                    if "Casas" not in jugadores["vermell"]["Propiedades"][calleCasa]:
                        jugadores["vermell"]["Propiedades"][calleCasa]["Casas"] = 0
                    jugadores["vermell"]["Propiedades"][calleCasa]["Casas"] += numeroAnadirCasas   
                    actualizarHistorial(f"Se han añadido {numeroAnadirCasas} casas a '{calleCasa}'")

                else:
                    actualizarHistorial(f"No puedes añadir una casa porque no es de tu propiedad !")

            else:
                actualizarHistorial("No se pueden añadir mas de cuatro casas")
    #TRUCO PARA AÑADIR HOTELES A UN JUGADOR
    #Este truco es igual que el truco de añadir casas con la peculiaridad que hemos añadido la regla del juego que dicta que solo se pueden 
    #construir hoteles si se dispone de 2 casas
    elif text == "3":
        selectJugadorHotel = input("Aque jugador quieres añadir Hoteles ?[1. Blau, 2. Groc , 3. Taronja, 4. Vermell]\n")
        #Jugador azul
        if selectJugadorHotel == "1":
            calleHotel = input("A que calle quieres añadirle un hotel ?\n")
            numeroAnadirHotel = int(input("Cuantos hoteles quieres anadir ? [1 o 2]\n"))
            if  1 <= numeroAnadirHotel <= 2: #Se comprueba que no se añadan mas de 2 hoteles i menos de 1
                if calleHotel in jugadores["blau"]["Propiedades"]: #Accedemos a propiedades para comprobar que el jugador disponga de la calle seleccionada
                    if "Hoteles" not in jugadores["blau"]["Propiedades"][calleHotel]: #Se crea un diccionaro en Propiedades, con llave hoteles para ir almacenando el numero de hoteles
                        jugadores["blau"]["Propiedades"][calleHotel]["Hoteles"] = 0

                    #Aqui se realiza el filtrado de hoteles
                    elif jugadores["blau"]["Propiedades"][calleHotel]["Hoteles"] == 2:
                        actualizarHistorial(f"No se pueden añadir mas hoteles")

                    elif jugadores["blau"]["Propiedades"][calleHotel]["Hoteles"] < 2:
                        if jugadores["blau"]["Propiedades"][calleHotel]["Hoteles"] == 1 and numeroAnadirHotel == 2:
                            actualizarHistorial(f"Añadir 2 hoteles superaría el límite")
                        else:
                            jugadores["blau"]["Propiedades"][calleHotel]["Hoteles"] += numeroAnadirHotel
                            actualizarHistorial(f"+{numeroAnadirHotel} hoteles en '{calleHotel}' de 'Blau'")


                else:
                    actualizarHistorial(f"No puedes añadir un hotel porque no es de tu propiedad !")
            else:
                    actualizarHistorial("No se pueden añadir mas de 2 hoteles")
        #Jugador amarillo
        elif selectJugadorHotel == "2":
            calleHotel = input("A que calle quieres añadirle un hotel ?\n")
            numeroAnadirHotel = int(input("Cuantos hoteles quieres anadir ? [1 o 2]\n"))
            if  1 <= numeroAnadirHotel <= 2:
                if calleHotel in jugadores["groc"]["Propiedades"]:
                    if "Hoteles" not in jugadores["groc"]["Propiedades"][calleHotel]:
                        jugadores["groc"]["Propiedades"][calleHotel]["Hoteles"] = 0

                    
                    elif jugadores["groc"]["Propiedades"][calleHotel]["Hoteles"] == 2:
                        actualizarHistorial(f"No se pueden añadir mas hoteles")

                    elif jugadores["groc"]["Propiedades"][calleHotel]["Hoteles"] < 2:
                        if jugadores["groc"]["Propiedades"][calleHotel]["Hoteles"] == 1 and numeroAnadirHotel == 2:
                            actualizarHistorial(f"Añadir 2 hoteles superaría el límite")
                        else:
                            jugadores["groc"]["Propiedades"][calleHotel]["Hoteles"] += numeroAnadirHotel
                            actualizarHistorial(f"+{numeroAnadirHotel} hoteles en '{calleHotel}' de 'Groc'")


                else:
                    actualizarHistorial(f"No puedes añadir un hotel porque no es de tu propiedad !")
            else:
                    actualizarHistorial("No se pueden añadir mas de 2 hoteles")
        #Jugador naranja
        elif selectJugadorHotel == "3":
            calleHotel = input("A que calle quieres añadirle un hotel ?\n")
            numeroAnadirHotel = int(input("Cuantos hoteles quieres anadir ? [1 o 2]\n"))
            if  1 <= numeroAnadirHotel <= 2:
                if calleHotel in jugadores["taronja"]["Propiedades"]:
                    if "Hoteles" not in jugadores["taronja"]["Propiedades"][calleHotel]:
                        jugadores["taronja"]["Propiedades"][calleHotel]["Hoteles"] = 0

                    
                    elif jugadores["taronja"]["Propiedades"][calleHotel]["Hoteles"] == 2:
                        actualizarHistorial(f"No se pueden añadir mas hoteles")

                    elif jugadores["taronja"]["Propiedades"][calleHotel]["Hoteles"] < 2:
                        if jugadores["taronja"]["Propiedades"][calleHotel]["Hoteles"] == 1 and numeroAnadirHotel == 2:
                            actualizarHistorial(f"Añadir 2 hoteles superaría el límite")
                        else:
                            jugadores["taronja"]["Propiedades"][calleHotel]["Hoteles"] += numeroAnadirHotel
                            actualizarHistorial(f"+{numeroAnadirHotel} hoteles en '{calleHotel}' de 'Taronja'")


                else:
                    actualizarHistorial(f"No puedes añadir un hotel porque no es de tu propiedad !")
            else:
                    actualizarHistorial("No se pueden añadir mas de 2 hoteles")
        #Jugador rojo
        elif selectJugadorHotel == "4":
            calleHotel = input("A que calle quieres añadirle un hotel ?\n")
            numeroAnadirHotel = int(input("Cuantos hoteles quieres anadir ? [1 o 2]\n"))
            if  1 <= numeroAnadirHotel <= 2:
                if calleHotel in jugadores["vermell"]["Propiedades"]:
                    if "Hoteles" not in jugadores["vermell"]["Propiedades"][calleHotel]:
                        jugadores["vermell"]["Propiedades"][calleHotel]["Hoteles"] = 0

                    elif jugadores["vermell"]["Propiedades"][calleHotel]["Hoteles"] == 2:
                        actualizarHistorial(f"No se pueden añadir mas hoteles")

                    elif jugadores["vermell"]["Propiedades"][calleHotel]["Hoteles"] < 2:
                        if jugadores["vermell"]["Propiedades"][calleHotel]["Hoteles"] == 1 and numeroAnadirHotel == 2:
                            actualizarHistorial(f"Añadir 2 hoteles superaría el límite")
                        else:
                            jugadores["vermell"]["Propiedades"][calleHotel]["Hoteles"] += numeroAnadirHotel
                            actualizarHistorial(f"+{numeroAnadirHotel} hoteles en '{calleHotel}' de 'Vermell'")
                else:
                    actualizarHistorial(f"No puedes añadir un hotel que no es de tu propiedad !")
            else:
                    actualizarHistorial("No se pueden añadir mas de 2 hoteles")
        else:
            actualizarHistorial(f"No existe el jugador seleccionado")

    #TRUCO PARA ADELANTAR TURNOS
    elif text == "4":
        
        adelantarTurno = input("De que jugador quieres adelantar su turno ? [1. Blau 2. Groc 3. Taronja 4. Vermell]\n")
        #Jugador azul
        if adelantarTurno == "1":
            skipTurnoA = "blau"

        #Jugador amarillo
        elif adelantarTurno == "2":
            skipTurnoA = "groc"

        #Jugador taronja
        elif adelantarTurno == "3":
            skipTurnoA = "taronja"

        elif adelantarTurno == "4":
            skipTurnoA = "vermell"

        else:
            actualizarHistorial("No existe el jugador seleccionado")

    #TRUCO PARA AÑADIR DINERO
    elif text == "5":
        anadirQuitar = input("Quieres añadir o quitar dinero de un jugador? [1. Añadir, 2.Quitar]\n")
        #Para añadir dinero 
        if anadirQuitar == "1":
            trucoJugador = input("A que jugador deseas añadir dinero ? [1. Blau 2. Groc 3. Taronja 4. Vermell]\n")
            #Jugador azul
            if trucoJugador == "1":
                cantidadAnadir = int(input("Que cantidad quieres añadir ?\n")) #Se selecciona la cantidad a añadir
                jugadores["blau"]["Diners"] += cantidadAnadir #Se suma la cantidad que hemos añadido
                actualizarHistorial(f"Se han añadido {cantidadAnadir} al jugador 'blau', total: {jugadores['blau']['Diners']}") #Actualizamos mensaje en el historial
            #Jugador amarillo
            elif trucoJugador == "2":
                cantidadAnadir = int(input("Que cantidad quieres añadir?\n"))
                jugadores["groc"]["Diners"] += cantidadAnadir
                actualizarHistorial(f"Se han añadido {cantidadAnadir} al jugador 'Groc', total: {jugadores['groc']['Diners']}")
            #Jugador naranja
            elif trucoJugador == "3":
                cantidadAnadir = int(input("Que cantidad quieres añadir?\n"))
                jugadores["taronja"]["Diners"] += cantidadAnadir
                actualizarHistorial(f"Se han añadido {cantidadAnadir} al jugador 'Taronja', total: {jugadores['taronja']['Diners']}")
            #Jugador rojo
            elif trucoJugador == "4":
                cantidadAnadir = int(input("Que cantidad quieres añadir ?\n"))
                jugadores["vermell"]["Diners"] += cantidadAnadir
                actualizarHistorial(f"Se han añadido {cantidadAnadir} al jugador 'Vermell', total: {jugadores['vermell']['Diners']}")

        #Quitar dinero
        #Igual que añadir pero restando la cantidad a jugadores[juador]["Diners"]
        if anadirQuitar == "2":
            trucoJugador = input("A que jugador deseas quitar dinero? [1. Blau 2. Groc 3. Taronja 4. Vermell]\n")
            #Jugador azul
            if trucoJugador == "1":
                cantidadQuitar = int(input("Que cantidad quieres quitar?\n"))
                jugadores["blau"]["Diners"] -= cantidadQuitar
                actualizarHistorial(f"Se han quitado {cantidadQuitar} al jugador 'Blau', total: {jugadores['blau']['Diners']}")
            #Jugador amarillo
            elif trucoJugador == "2":
                cantidadQuitar = int(input("Que cantidad quieres quitar?\n"))
                jugadores["groc"]["Diners"] -= cantidadQuitar
                actualizarHistorial(f"Se han quitado {cantidadQuitar} al jugador 'Groc', total: {jugadores['groc']['Diners']}")
            #Jugador naranja
            elif trucoJugador == "3":
                cantidadQuitar = int(input("Que cantidad quieres quitar?\n"))
                jugadores["taronja"]["Diners"] -= cantidadQuitar
                actualizarHistorial(f"Se han quitado {cantidadQuitar} al jugador 'Taronja', total: {jugadores['taronja']['Diners']}")
            #Jugador rojo
            elif trucoJugador == "4":
                cantidadQuitar = int(input("Que cantidad quieres quitar?\n"))
                jugadores["vermell"]["Diners"] -= cantidadQuitar
                actualizarHistorial(f"Se han quitado {cantidadQuitar} al jugador 'Vermell', total: {jugadores['vermell']['Diners']}")

    #TRUCO PARA AÑADIR DINERO A LA BANCA
    elif text == "6":
        dinersBanca = input("Quieres añadir o quitar dinero a la banca ?[1.Añadir, 2.Quitar]\n")
        if dinersBanca == "1":
            anadirDinero = int(input("Que canitad quieres añadir ?\n"))
            banca += anadirDinero #Añadimos el dinero
            actualizarHistorial(f"Se ha añadido la cantidad de {anadirDinero} a banca: Total = {banca}")
        else:
            quitarDinero = int(input("Que canitad quieres quitar ?\n"))
            banca -= quitarDinero #Se quita el dinero
            actualizarHistorial(f"Se ha sacado la cantidad de {quitarDinero} a banca: Total = {banca}")
            

def seguirEnPrision(jugador):
    dado1, dado2, totalDado = tirarDados()
    """En esta opcion comprobamos que los dados no son los mismo
       - Si son los mimos el jugador sale de la prision
       - Se actualiza 'EstanEn prision' a False, i salimos de la prision
       - Si los dados no son los mismos el jugador continua en prision"""
    if jugadores[jugador]["EstaEnPrision"] == True:
        if dado1 == dado2:
            jugadores[jugador]["EstaEnPrision"] = False
            actualizarHistorial(f"  Los dados son '{dado1}' y '{dado2}', sale de prisión!")
            #return moverJugador(jugador) #NO SÉ SI EN EL MISMO TURNO EN EL QUE TIRA LOS DADOS SE PODRÍA MOVER, SI ES QUE SÍ, DESCOMENTAR ESTA LÍNEA
            return None
        else:
            actualizarHistorial(f"  Los dados son '{dado1}' y '{dado2}', no han coincidido")
        """Comprobamos los turnos que lleva el jugador en prisión:
           - Si lleva meos de 3, se suma 1 a la entrada 'TurnosPrision'
           - Se actualiza en historial el numero de turnos que lleva el jugador en prision
           - Una vez el primer if < 3 deja de cumplirse, 'EstaEnPrision', se actualiza a False i se muestra mensaje en historial conforme ha salido"""
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
    """Esta funcion se puede llamar con el argumento 'jugador' como ('V') o ('vermell')
       - Se comprueba que el jugador tenga el suficiente dinero para pagar a la banca
       - Si lo tiene, se realiza el pago, sino se llama a bancarrota, donde se le mostrarán diferentes opciones"""
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
       - Devuelve el index en el array de calles y también devuelve el diccionario de la calle en la que está el jugador"""

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
    """El parámetro de esta funcion tiene que ser la incial del jugador ('V') por ejemplo
       - Se recorre la lista completa de calles i se inician condicionales
       - Se selecciona al jugador que esta ocupando la calle
       - Si la calle del jugador en la casilla no pertence a sus propiedades, recorremos los jugadores buscando el jugador(videojugador) con dicha propiedad
       - Una vez se encuentra, se calcula el valorAPagar:
         - Si el jugador tiene el suficiente dinero para pagar, se realiza el pago correspondiente 
         - Si no lo tiene se llama a bancarrota()"""
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
                        valorAPagar += jugadores[videojugador]["Propiedades"][calle["Nombre"]]["Casas"] * calle["LlCasa"] #Pago por cada casa
                        valorAPagar += jugadores[videojugador]["Propiedades"][calle["Nombre"]]["Hoteles"] * calle["LlHotel"] #Pago por cada hotel

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

    callesEspeciales = ["Sort", "Sort2", "Anr pró", "Caixa", "Caixa2", "Presó", "Sortida", "Parking"]
    if jugador == "V":
        player = "vermell"
    elif jugador == "B":
        player = "blau"
    elif jugador == "G":
        player = "groc"
    elif jugador == "T":
        player = "taronja"
    #Antes de mover al jugador se comprueba 'EstaEnPrision', si el valor es True, se llama a seguirEnPrision para comprobar su estado
    if jugadores[player]["EstaEnPrision"] == True:
        seguirEnPrision(player)
        return None

    dado1, dado2, totalDado = tirarDados()
    """Recorremos el listado de calles, i seleccionamos al jugador que se encuentra ocupando la calle
    - Se usa casillaAlLlamar para alacenar el indice de la calle
    - Se comprueba que el indice de la calle + el total del dado no supere el total de casillas del tablero
      - Si lo hace se restan -24 i se vuelve a empezar
    - Se elimina al jugador de la ocupación de la calle actual y se añade a la calle (usando el indice almacenado + los dados) destino mediante extend para 
      asegurar el orden de llegada
    - Para comprobar su paso por salida se comprueba, en nuestro caso, que la casilla destino sea mas pequeña que 12 i el indice sea mayor o igual a 12
     - Si ha pasado, se le suman 200 a 'Diners'"""
    for calle in calles:

        if jugador in calle["Ocupacion"]:
            
            casillaAlLlamar = calles.index(calle)

            if casillaAlLlamar + totalDado >= len(calles):
                casillaAlLlamar -= 24
                print(casillaAlLlamar)

            print(casillaAlLlamar + totalDado)
            print(len(calles))
            calle["Ocupacion"].remove(jugador)
            calles[casillaAlLlamar + totalDado]["Ocupacion"].extend(jugador)
            nuevaCalle = calles[casillaAlLlamar + totalDado] #Aqui almacenamos el indice de la calle destino

            actualizarHistorial(f"  Los dados han dado: '{dado1}' y '{dado2}' con un total de '{totalDado}'")
            actualizarHistorial(f"  '{player.capitalize()}' se ha movido hasta '{calles[casillaAlLlamar + totalDado]['Nombre']}'")

            if casillaAlLlamar < 12 and calles.index(nuevaCalle) >= 12:
                actualizarHistorial(f"  '{player.capitalize()}' ha pasado por la casilla de salida, +200")
                jugadores[player]["Diners"] += 200

            clearScreen()
            imprimir_tablero(calles)

            break

    if pagarCasillaDeJugador(jugador) == "Bancarrota":
        return None
    
    elif nuevaCalle["Nombre"] not in callesEspeciales: #Si no es casilla de evento se muestran las diferentes opciones a hacer
        while True:
            clearScreen()
            imprimir_tablero(calles)
            print(f"Qué quieres hacer? (1. Passar / 2. Comprar Terreny / 3. Comprar Casa / 4. Comprar hotel / 5. Mirar precios / 6. Precio al banco / 7. Precio a un jugador / 8. Vender al banco / 9. Vender a un jugador)")

            eleccion = str(input())
            #Para pasar de turno
            if eleccion == "1":
                jugadores[player]["Torn"] = False
                actualizarHistorial(f"  '{player.capitalize()}' pasa de turno.")
                return
            #Comprar Terreno
            elif eleccion == "2":
                anadirCasa(player, nuevaCalle["Nombre"]) #Se utiliza anadirCasa para añadir la propiedad al jugador
            #Comprar Casa en tu propiedad
            elif eleccion == "3":
                if nuevaCalle["Nombre"] in jugadores[player]["Propiedades"]:
                    anadirCasa(player, nuevaCalle["Nombre"])
                else:
                    print(f"Error, '{nuevaCalle['Nombre']}' no es de tu propiedad")
            #Comprar Hotel en tu propiedad
            elif eleccion == "4":
                anadirHotel(player, nuevaCalle["Nombre"])
            #Se mira los precios de la calle actual
            elif eleccion == "5":
                if nuevaCalle["Nombre"] not in callesEspeciales:
                    txt = f"    Alquiler casa: {nuevaCalle['LlCasa']}                 Alquiler hotel: {nuevaCalle['LlHotel']}"
                    txt2 = f"    Terreno: {nuevaCalle['CmpTrrny']}       Casa: {nuevaCalle['CmpCasa']}       Hotel: {nuevaCalle['CmpHotel']}"
                    actualizarHistorial(f"- Precios {nuevaCalle['Nombre']}:")
                    actualizarHistorial(txt)
                    actualizarHistorial(txt2)
                else:
                    actualizarHistorial("Nada que mostrar")
            #Se mira el precio que ganarias si vendes tus propiedaes al banco
            elif eleccion == "6":
                valorTotal = 0
                for propiedad in jugadores[player]["Propiedades"]: #Recorre todas las propiedaes del jugador
                    for calle in calles:
                        if calle["Nombre"] == propiedad: #Se comprueba que la calle este en propiedad del jugador
                            for construccion in jugadores[player]["Propiedades"][propiedad].keys(): #Por cada construccion del jugador en esa propiedad
                                if construccion == "Casas":
                                    valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion] #Se calcula el valor que se pagaria por las casas
                                if construccion == "Hoteles":
                                    valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion] #Se calcula el valor que se pagaria por los hoteles
                                valorTotal += valorInd
                valorTotal = (valorTotal * 50) // 100 #Se muestra el valor que obtendria al vender sus propiedades
                actualizarHistorial(f"  Ganarías al vender tus propiedades al banco: {valorTotal}")
            #Se mira lo que ganaria si se vendiese a otro jugador (similar a la elección anterior)
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
            #Para vender las propiedades al banco
            elif eleccion == "8":
                if len(jugadores[player]["Propiedades"]) > 0: #Se comprueba que se tengan propiedades
                    valorTotal = 0
                    for propiedad in jugadores[player]["Propiedades"]:
                        for calle in calles:
                            if calle["Nombre"] == propiedad:
                                for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                    if construccion == "Casas":
                                        valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion] #Se venden las casas
                                    if construccion == "Hoteles":
                                        valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion] #Se venden los hoteles
                                    valorTotal += valorInd
                    valorTotal = (valorTotal * 50) // 100 #Se obtiene el valor de la venta
                    if input(f"Estás segur@ que quieres vender tus propiedades por {valorTotal}? (s/n)").lower() == "s":
                        jugadores[player]["Diners"] += valorTotal #Aqui se obtiene el valor de la compra
                        jugadores[player]["Propiedades"] = {} #Se vacía el diccionario correspondiente a Propiedades
                        actualizarHistorial(f"  {player.capitalize()} ha vendido sus propiedades al banco por {valorTotal}")
                else:
                    actualizarHistorial(f"  No tienes propiedades para vender")
            #Se venden propiedaes a un jugador      
            elif eleccion == "9":
                if len(jugadores[player]["Propiedades"]) > 0: #Se comprueba que el jugador tenga propiedaes
                    jugadoresNoTurno = [] #Se crea lista para almacenar los jugadores que no se encuentran en su turno
                    for videojugador in jugadores: #Por cada jugador, si "Torn" = False, no esta en su turno, se añaden a la lista
                        if jugadores[videojugador]["Torn"] == False:
                            jugadoresNoTurno.append(videojugador)
                    valorTotal = 0
                    for propiedad in jugadores[player]["Propiedades"]: #Se recorren las propiedades del jugador
                        for calle in calles:
                            if calle["Nombre"] == propiedad: #Se comprueba cada calle en propiedad del jugador
                                for construccion in jugadores[player]["Propiedades"][propiedad].keys():
                                    if construccion == "Casas":
                                        valorInd = calle["CmpCasa"] * jugadores[player]["Propiedades"][propiedad][construccion] #Precio por las casas
                                    if construccion == "Hoteles":
                                        valorInd = calle["CmpHotel"] * jugadores[player]["Propiedades"][propiedad][construccion] #Precio por los hoteles
                                    valorTotal += valorInd
                    valorTotal = (valorTotal * 90) // 100
                    while True:
                        print(f"A quién quieres venderle?: " + ", ".join(jugadoresNoTurno))
                        comprador = input()
                        comprador = comprador.lower()
                        if comprador in jugadoresNoTurno:
                            break #Se termina el bucle cuando se selecciona a un jugador valido de la lista que no se encuentra en su turno
                    if comprador in jugadoresNoTurno:
                        if jugadores[comprador]["Diners"] >= valorTotal:
                            if input(f"Estás segur@ que quieres vender tus propiedades a {comprador.capitalize()} por {valorTotal}? (s/n)").lower() == "s":
                                #Se actualiza "Diners" i "Propiedades", del jugador actual i del comprador de las propiedades
                                jugadores[comprador]["Diners"] -= valorTotal
                                jugadores[player]["Diners"] += valorTotal
                                propiedadesJugador = jugadores[player]["Propiedades"].items()
                                jugadores[comprador]["Propiedades"].update(propiedadesJugador)
                                jugadores[player]["Propiedades"] = {}
                                actualizarHistorial(f"  '{player.capitalize()}' ha vendido sus propiedades a {comprador.capitalize()} por {valorTotal}")
            
                
                else:
                     actualizarHistorial(f"  No tienes propiedades para vender")
            elif eleccion == "trucs":
                trucs()
    else:
        if nuevaCalle["Nombre"] == "Sort2" or nuevaCalle["Nombre"] == "Sort":
            cartaSort(player)

        elif nuevaCalle["Nombre"] == "Caixa" or nuevaCalle["Nombre"] == "Caixa2":
            cartaCaixa(player)
       
        elif nuevaCalle["Nombre"] == "Anr pró":
            directoPrision(player)

        

        imprimir_tablero(calles)
    
#Funcion que tira los dados
def tirarDados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6) 

    resultadoDados = dado1 + dado2
    return dado1, dado2, resultadoDados

#Funcion que muestra la información
def mostrarInformacion():
    #Se almacena en una lista para poder mostrarse en el latera derecho del tablero
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
    global banca
    while True:
        clearScreen()
        imprimir_tablero(calles)
        #Si no es una casilla de evento, se crea un diccionario para almacenar casas i hoteles
        if calle != "Parking" and calle != "Sort" and calle != "Anr pró" and calle != "Caixa" and calle != "Caixa2" and calle != "Sort2" and calle != "Presó":
            dic = {
                "Casas" : 0,
                "Hoteles" : 0
            }

            key = jugador
            
            for street in calles:
                if calle in street.values():
                    dicCalle = street
            #Compobamos que el jugador que está jugando no pueda comprar la propiedad de otro jugador
            for player in jugadores.keys():
                dicComprobar = jugadores[player]["Propiedades"]
                
                if calle in dicComprobar and player != jugador:
                    actualizarHistorial(f"  Error al comprar '{calle}': La casilla pertenece a '{player.capitalize()}'")
                    return None
            #Comprobamos que el numero de casa no sea superior a 4 (límite)
            if calle in jugadores[key]["Propiedades"].keys():
                if jugadores[key]["Propiedades"][calle]["Casas"] >= 4:
                    actualizarHistorial(f"  Error: Se pueden tener cómo máximo 4 casas, compra un hotel.")
                    return None
        
                elif jugadores[key]["Diners"] >= dicCalle["CmpCasa"]: #Si tiene dinero suficiente para comprar una casa.
                    jugadores[key]["Propiedades"][calle]["Casas"] += 1
                    jugadores[key]["Diners"] -= dicCalle["CmpCasa"] #Resta el dinero de la casa al dinero del jugador
                    banca += dicCalle["CmpCasa"]

                    actualizarHistorial(f"  '{jugador.capitalize()}' compra una casa en '{calle}'")
                    return None
                else:
                    actualizarHistorial(f"  Error: Una casa cuesta {dicCalle['CmpCasa']} y tienes {jugadores[key]['Diners']}")
                    return None
            else:
                #print(jugadores[key]["Diners"])
                #print(dicCalle["CmpTrrny"])
                if jugadores[key]["Diners"] >= dicCalle["CmpTrrny"]:
                    jugadores[key]["Propiedades"][calle] = dic
                    actualizarHistorial(f"  '{jugador.capitalize()}' ha comprado el terreno '{calle}'")
                    jugadores[key]["Diners"] -= dicCalle["CmpTrrny"] #Resta el dinero de la casilla al dinero del jugador
                    banca += dicCalle["CmpTrrny"] #Se actualiza el dinero de la banca 
                    imprimir_tablero(calles)
                    return None
                else:
                    actualizarHistorial(f"  Error: La casilla cuesta {dicCalle['CmpTrrny']} y tienes {jugadores[key]['Diners']}")
                    print(f"Error: La casilla cuesta {dicCalle['CmpTrrny']} y tienes {jugadores[key]['Diners']}")
                    return None

        else:
            actualizarHistorial(f"  Error: '{calle}' no se puede comprar.")
            return None
#Para comprar o añadir Hoteles
def anadirHotel(jugador, calle):
    global banca
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
                    if jugadores[key]["Diners"] >= dicCalle["CmpHotel"]: #Se comprueba que el jugador pueda pagar el hotel
                        jugadores[key]["Propiedades"][calle]["Casas"] -= 2 #Se actualizan las casas
                        jugadores[key]["Propiedades"][calle]["Hoteles"] += 1 #Se actualizan los hoteles
                        jugadores[key]["Diners"] -= dicCalle["CmpHotel"] #Se actualiza el dinero gastado del jugador
                        banca += dicCalle["CmpHotel"] #Se le suma a banca el dinero obtenido por la compra del hotel
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



def bancaRota(rendirse = False, videojugador=""): #Rendirse por defecto esta en False, i has de seleccionar el nombre del jugador
    global banca
    global jugadoresEnBancarrota

    for jugador in jugadores.keys():
        if (jugadores[jugador]["Diners"] <= 0 and jugador not in jugadoresEnBancarrota and jugadores[jugador]["Torn"] == True) or videojugador in jugadores.keys():

            if videojugador in jugadores.keys(): #ESTO ES PARA QUE EN LA FUNCION DE PAGAR ALQUILER SE PUEDA LLAMAR A ESTA FUNCION AUNQUE EL DINERO NO SEA 0
                jugador = videojugador

            actualizarHistorial(f"+ '{jugador.capitalize()}' está en bancarrota")
            imprimir_tablero(calles)
            #Este bucle muestra las opciones una vez te declaras en bancarrota
            while True:
                eleccion = ""
                if rendirse == False:
                    eleccion = input("1. Vender al banco 2. Vender a otro jugador 3. Darse en bancarrota\n")
                ValorAlVender = 0
                #Vender al banco
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
                    banca -= ValorAlVender #Se actualiza el dinero de la banca
                    #print(jugadores[jugador]["Diners"])
                    jugadores[jugador]["Diners"] += ValorAlVender #Se suma el dinero al jugador por vender sus propiedades a la banca
                    actualizarHistorial(f"  {jugador.capitalize()} ha vendido sus propiedades a la banca por {ValorAlVender}")
                    #Si despues de la venta sigues teniendo menos que 0 se te elimina de igual forma
                    if jugadores[jugador]["Diners"] < 0:
                            jugadores[jugador]["Propiedades"] = {}
                            jugadoresEnBancarrota.append(jugador)
                            actualizarHistorial(f"  '{jugador.capitalize()}' se ha dado en bancarrota, no jugará más")
                    break
                #Vender a otro jugador
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
                    #Se actualiza el dinero del jugador i el comprador
                    if jugadores[comprador]["Diners"] >= ValorAlVender:
                        jugadores[comprador]["Diners"] -= ValorAlVender
                        jugadores[jugador]["Diners"] += ValorAlVender

                        propiedadesJugador = jugadores[jugador]["Propiedades"].items()

                        jugadores[comprador]["Propiedades"].update(propiedadesJugador)
                        jugadores[jugador]["Propiedades"] = {}

                        actualizarHistorial(f"  '{jugador.capitalize()}' ha vendido sus propiedades a '{comprador.capitalize()}' por '{ValorAlVender}'")

                        if jugadores[jugador]["Diners"] < 0:
                            jugadores[jugador]["Propiedades"] = {}
                            jugadoresEnBancarrota.append(jugador)
                            actualizarHistorial(f"  '{jugador.capitalize()}' se ha dado en bancarrota, no jugará más")
                        break
                    else:
                        print(f"'{comprador.capitalize()}' no tiene dinero")
                        actualizarHistorial(f"  '{comprador.capitalize()}' no tiene suficiente dinero")

                        if jugadores[jugador]["Diners"] < 0:
                            jugadores[jugador]["Propiedades"] = {}
                            jugadoresEnBancarrota.append(jugador)
                            actualizarHistorial(f"  '{jugador.capitalize()}' se ha dado en bancarrota, no jugará más")
                elif eleccion == "3" or rendirse == True:
                    jugadores[jugador]["Propiedades"] = {}
                    jugadoresEnBancarrota.append(jugador)
                    actualizarHistorial(f"  '{jugador.capitalize()}' se ha dado en bancarrota, no jugará más")
                    return True
            

def actualizarHistorial(info): 
#Esta función es la que usaremos para recoger todos los mensajes, lo malo es que para cada uno de los eventos, 
# se tiene que llamar dentro de las funciones i hacer .append en todas las funciones de evento                       

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
#Esta funcion servira para barajar a los jugadores aleatoriamente
def desordenarDiccionario(dic):
    items = list(dic.items())

    random.shuffle(items)

    dicDesordenado = dict(items)

    return dicDesordenado
#Se inicia la partida
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
        mensajeSalida = f"  '{jugador.capitalize()}' vuelve a la casilla de salida, +200!"
        actualizarHistorial(mensajeSalida)
        jugadores[jugador]["Diners"] += 200

    elif carta == "Anar tres espais enrere":
        #EN ESTÁ, SI ES SORT2 RETROCEDE HASTA LA SALIDA, POR LO QUE NO SÉ SI DEBERÍA GANAR 200 O NO
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

def hayGanador():
    global jugadoresEnBancarrota

    if len(jugadoresEnBancarrota) == 3:
        for jugador in jugadores:
            if jugador not in jugadoresEnBancarrota:
                return jugador
    else:
        return ""
    
def monopoly():
    global banca
    global skipTurnoA
    global jugadoresEnBancarrota

    orden = inicioPartida(jugadores)
    ganador = ""

    while ganador == "":

        for jugador in orden:
            if jugador == "V":
                player = "vermell"
            elif jugador == "B":
                player = "blau"
            elif jugador == "T":
                player = "taronja"
            elif jugador == "G":
                player = "groc"

            
            
            if skipTurnoA != "":
                if skipTurnoA == player:
                    actualizarHistorial(f"- Saltando el turno a: '{player.capitalize()}'")
                    actualizarHistorial("")
                    skipTurnoA = ""
                else:
                    continue

            
            jugadores[player]["Torn"] = True

            if player not in jugadoresEnBancarrota:
                if bancaRota(): 
                    actualizarHistorial("")
                    continue
                
            if player in jugadoresEnBancarrota:
                continue
            
            clearScreen()
            actualizarHistorial(f"> Turno de '{player.capitalize()}':")
            imprimir_tablero(calles)
            moverJugador(jugador)
            actualizarHistorial(f"")

            clearScreen()
            imprimir_tablero(calles)
            input("Aceptar.")
            jugadores[player]["Torn"] = False

            if banca <= 500000:
                banca = 1000000
                actualizarHistorial(f"Banca vuelve a tener 1.000.000")
                actualizarHistorial(f"")

        ganador = hayGanador()

    actualizarHistorial(f"")
    actualizarHistorial(f"Ha ganado {ganador.capitalize()}!".center(40))
    imprimir_tablero(calles)
    
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
]

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

jugadoresEnBancarrota = []

skipTurnoA= ""

# AQUÍ INICIA EL JUEGO

monopoly()

