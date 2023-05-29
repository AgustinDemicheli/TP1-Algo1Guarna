import letraPalabra

PTO_ACIERTO=10
PTO_ERROR=-3


def tablero( ):
    """
    Dentro de un ciclo,
    tablero recibe dos diccionarios, el primero  contiene inciales-palabra,
    el segundo contiene la palabra con su significado, se desglosan en listas, se realiza un llamado a turnos y 
    al final del tablero si no deseamos continuar jugando nos muestra la puntuacion sino se reinicia el ciclo
    -Agustín Demicheli-
    """

    

    jugar="si"
    puntos=0
    while jugar=="si":
        (palabras, palabras_significado) = letraPalabra.letra_palabra()

        iniciales=[]
        palabra_completa=[]
        respuesta=[]
        letras=[]
        significado=[]
        
        for llaves,valor in palabras.items():
            iniciales.append(f"[{llaves}]")
            palabra_completa.append(valor)
            respuesta.append('[ ]')

        for letters,meaning in palabras_significado.items():
            letras.append(f"[{letters}]")
            significado.append(meaning)

        puntos=turno(iniciales,respuesta,puntos,palabra_completa,significado)
        juego=input('¿Desea continuar jugando? si/no ')
        if juego.lower()=='no':
            jugar="no"
        elif juego.lower()!='si':
            jugar=input('¿Desea continuar jugando? si/no ')
    return (f'su puntuacion final es: {puntos}')

def turno(iniciales,respuesta,puntos,palabra_completa,significado):
    """
    Muestra el tablero como tal, es la funcion encargada de llevar la
    informacion del tablero a cabo, recibe un llamado a listado y devuelve los puntos
    -Agustín Demicheli-
    -Nadeska Millán-
    """
    j=0 
    aciertos=0
    errores=0
    historial=[]
    while j<len(iniciales):
        print("".join(iniciales))
        print("".join(respuesta))
        print("                           ")
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        print(f"Turno letra {iniciales[j][1]} -palabra de {len(palabra_completa[j])} letras")
        print(f"Definición: {significado[j]} ")
        pregunta=input('Ingrese una palabra: ')
        
        
        if pregunta ==palabra_completa[j]:
                respuesta[j]='[a]'
                aciertos+=1
                puntos+=PTO_ACIERTO
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - acierto")
                j+=1
        else:
                respuesta[j]='[e]'
                errores+=1
                puntos+=PTO_ERROR
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - error - palabra correcta: {palabra_completa[j]}")
                j+=1

    print("".join(iniciales))
    print("".join(respuesta))
    print(listado(historial))
    return puntos

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



print( tablero() )
