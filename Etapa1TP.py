import letraPalabra
import Etapa10

PTO_ACIERTO = Etapa10.obtener_puntaje_acierto()
PTO_ERROR= Etapa10.obtener_puntaje_desacierto()
MAXIMO_PARTIDAS = Etapa10.obtener_maximo_partidas()


def tablero(lista_jugadores):
    """
    Dentro de un ciclo,
    tablero recibe dos diccionarios, el primero  contiene inciales-palabra,
    el segundo contiene la palabra con su significado, se desglosan en listas, se realiza un llamado a turnos y 
    al final del tablero si no deseamos continuar jugando nos muestra la puntuacion sino se reinicia el ciclo
    -Agustín Demicheli-
    V.TP2 Se altero el flujo de datos para que puedan permanecer los valores tras cada pasada 
    y sumarse, devuelve el puntaje final junto a la cantidad de pasadas realizadas
    """
    dicc_puntaje_jugadores={}
    jugadas=0
    jugar="si"
    while jugar == "si":
        #antes   (palabras, palabras_significado) = letraPalabra.letra_palabra()

        palabras_significado = letraPalabra.letra_palabra()
        
        iniciales=[]
        lista_numero_participantes=[]
        palabra_completa=[]
        respuesta=[]
        letras=[]
        significado=[]
        lista_participantes=[]
        """
         for llaves,valor in palabras.items():
            iniciales.append(f"[{llaves}]")
            palabra_completa.append(valor)
            respuesta.append('[ ]')

        for letters,meaning in palabras_significado.items():
            letras.append(f"[{letters}]")
            significado.append(meaning)
        """
        for llaves,valor in palabras_significado.items():
            iniciales.append(f"[{llaves[0]}]")
            palabra_completa.append(llaves)
            respuesta.append('[ ]')
            lista_numero_participantes.append('[ ]')
            letras.append(f"[{llaves}]")
            significado.append(valor)

        for participantes in lista_jugadores:
             lista_participantes.append(participantes)

        turno(iniciales,respuesta,lista_numero_participantes,palabra_completa,significado,dicc_puntaje_jugadores,lista_participantes)
        jugadas+=1

        if jugadas < MAXIMO_PARTIDAS:
            juego=input('¿Desea continuar jugando? si/no ')
            if juego.lower()=='no':
                jugar="no"
            elif juego.lower()!='si':
                jugar=input('¿Desea continuar jugando? si/no ')
            else:
                palabras_significado = letraPalabra.letra_palabra()

    print( f"Reporte final: \nPartidas jugadas:{jugadas}\n{puntaje(dicc_puntaje_jugadores,lista_participantes)}")
    jugar='no'

def turno(iniciales,respuesta,lista_numero_participantes,palabra_completa,significado,dicc_puntaje_jugadores,lista_participantes):
    """
    Muestra el tablero como tal, es la funcion encargada de llevar la
    informacion del tablero a cabo, recibe un llamado a listado y devuelve los puntos
    -Agustín Demicheli-
    -Nadeska Millán-
    V.TP2: Incluye junto a tablero la lógica que permite jugar de a varios jugadores, recibe listas,
    y diccionarios e imprime tanto historial de partida como el puntaje parcial
    """
    k=0
    j=0 
    aciertos=0
    dicc_errores={}
    dicc_aciertos={}
    for nombre in lista_participantes:
        dicc_errores[nombre]=0
        dicc_aciertos[nombre]=0
    
    errores=0
    historial=[]
    while k < len(lista_participantes):
        while  j < len(iniciales):
            print("".join(iniciales))
            print("".join(lista_numero_participantes))
            print("".join(respuesta))
            print("                           ")
            print("Jugadores")
            for nombre in lista_participantes:
                print(f"{lista_participantes.index(nombre) + 1}.{nombre.capitalize()}- Aciertos: {dicc_aciertos[nombre]}- Errores: {dicc_errores[nombre]}")
            print(f"Turno Jugador {lista_participantes[k]} - letra {iniciales[j][1]} - palabra de {len(palabra_completa[j])} letras")
            print(f"Definición: {significado[j]} ")
            pregunta=input('Ingrese una palabra: ')


            if pregunta ==palabra_completa[j]:
                    respuesta[j]='[a]'
                    lista_numero_participantes[j]=f'[{k+1}]'
                    dicc_aciertos[lista_participantes[k]]+=1
                    aciertos+=1
                    historial.append(f"Turno letra {iniciales[j][1].upper()} -Jugador {k+1} {lista_participantes[k]}- palabra de {len(palabra_completa[j])} letras - acierto")
                    j+=1
                    if lista_participantes[k] not in dicc_puntaje_jugadores:
                        dicc_puntaje_jugadores[lista_participantes[k]]=10
                    else:
                        dicc_puntaje_jugadores[lista_participantes[k]]+=10


            else:
                    respuesta[j]='[e]'
                    lista_numero_participantes[j]=f'[{k+1}]'
                    errores+=1
                    dicc_errores[lista_participantes[k]]+=1
                    historial.append(f"Turno letra {iniciales[j][1].upper()} -Jugador {k+1} {lista_participantes[k]}- palabra de {len(palabra_completa[j])} letras - error - palabra correcta: {palabra_completa[j]}")
                    j+=1
                    k+=1
                    if k==len(lista_participantes):
                        k=0
                    if lista_participantes[k] not in dicc_puntaje_jugadores:
                        dicc_puntaje_jugadores[lista_participantes[k]]=-3
                    else:
                        dicc_puntaje_jugadores[lista_participantes[k]]-=3
        

        print("".join(iniciales))
        print("".join(respuesta))
        print(listado(historial))
        print(f"Puntaje parcial:")
        for nombre in lista_participantes:
            print(f"{nombre}: {dicc_aciertos[nombre]*10-dicc_errores[nombre]*3} ")
        k=len(lista_participantes)
        

def puntaje(dicc_puntaje_jugadores,lista_participantes):
    cadena=""
    for nombre,puntos in dicc_puntaje_jugadores.items():
        cadena+=f" {lista_participantes.index(nombre)+1}.{nombre} = {puntos} puntos"+"\n"
    return cadena



def listado(historial_turno):
    """
    almacena el historial de juego en cada tablero para mostrar al final en formato
    cadena una lista de errores y aciertos
    -Agustín Demicheli-
    """
    lista=""
    for intentos in historial_turno:
        lista+=intentos+"\n"
    return lista    
listita=['alfredo','jorge']
#print(tablero(listita))

