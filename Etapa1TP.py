import letraPalabra
import Etapa10

PTO_ACIERTO = Etapa10.obtener_puntaje_acierto()
PTO_ERROR= Etapa10.obtener_puntaje_desacierto()
MAXIMO_PARTIDAS = Etapa10.obtener_maximo_partidas()


def tablero(lista_jugadores):
    """

    V.TP2 Recibe una lista de jugadores, y en un bucle mantiene el juego hasta el maximo de partidas
    o hasta que se decida no continuar jugando, devuelve el puntaje final y la cantidad de pasadas que se realizaron
    -Agustin Demicheli
    """
    dicc_puntaje_jugadores={}
    seguir_jugando=True
    jugadas=0
    while (jugadas < MAXIMO_PARTIDAS) and seguir_jugando:
        palabras_significado = letraPalabra.letra_palabra()
        
        iniciales=[]
        lista_numero_participantes=[]
        palabra_completa=[]
        respuesta=[]
        significado=[]
        lista_participantes=[]

        for llaves,valor in palabras_significado.items():
            iniciales.append(f"[{llaves[0]}]")
            palabra_completa.append(llaves)
            respuesta.append('[ ]')
            lista_numero_participantes.append('[ ]')
            significado.append(valor)

        for participantes in lista_jugadores:
             lista_participantes.append(participantes)

        jugar_partida(iniciales,respuesta,lista_numero_participantes,palabra_completa,significado,dicc_puntaje_jugadores,lista_participantes)
        jugadas+=1

        print( f"Puntaje parcial\n{puntaje(dicc_puntaje_jugadores,lista_participantes)}")
        if not validar_partida():
            seguir_jugando=False  
    if jugadas>=MAXIMO_PARTIDAS:
        print('\nAlcanzó el maximo de partidas, el juego finalizó ')
    return f"\nReporte final: \nPartidas jugadas:{jugadas}\n{puntaje(dicc_puntaje_jugadores,lista_participantes)}"
    

def jugar_partida(iniciales,respuesta,lista_numero_participantes,palabra_completa,significado,dicc_puntaje_jugadores,lista_participantes):
    """
    Esta funcion recibe las palabras a verificar en el pasapalabra la cantidad de puntos que lleva cada jugador,
    la lista de participantes y una lista vacia que se rellenara dependiendo del participante que completa la pregunta,y mostrara
    tanto aciertos y errores de los jugadores que se registren,
    muestra los puntajes parciales de cada partida
    -Agustín Demicheli
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
                        dicc_puntaje_jugadores[lista_participantes[k]]=PTO_ACIERTO
                    else:
                        dicc_puntaje_jugadores[lista_participantes[k]]+=PTO_ACIERTO


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
                        dicc_puntaje_jugadores[lista_participantes[k]]=-PTO_ERROR
                    else:
                        dicc_puntaje_jugadores[lista_participantes[k]]-=PTO_ERROR
        

        print("".join(iniciales))
        print("".join(respuesta))
        print(listado(historial))
        print(f"Puntaje de la partida:")
        for nombre in lista_participantes:
            print(f"{nombre}: {dicc_aciertos[nombre]*10-dicc_errores[nombre]*3} ")
        k=len(lista_participantes)
        

def puntaje(dicc_puntaje_jugadores,lista_participantes):
    """
    almacena en una cadena la cantidad de usuarios, junto a su puntuacion y el indice 
    -Agustín Demicheli
    """
    cadena=""
    for nombre,puntos in dicc_puntaje_jugadores.items():
        cadena+=f" {lista_participantes.index(nombre)+1}.{nombre} = {puntos} puntos"+"\n"
    return cadena

def validar_partida():
    """
    Consulta al usuario si decide seguir jugando, 
    devuelve un dato booleano
    -Agustín Demicheli
    """
    jugar=True
    respuesta_valida=False
    while not respuesta_valida:
        juego=input('¿Desea continuar jugando? si/no ')
        if juego.lower()=='si':
            jugar=True
            respuesta_valida=True
        elif juego.lower()=='no':
            jugar=False
            respuesta_valida=True
        else:
            print('Por favor ingrese una respuesta válida')
    return jugar


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
