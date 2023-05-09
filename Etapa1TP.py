import letraPalabra
import letraSignificado

def tablero(palabras,palabras_significado):
    """
    tablero recibe dos diccionarios, el primero  contiene inciales-palabra,
    el segundo contiene la inicial de la palabra con su significado
    """
    jugar="si"
    puntos=0
    while jugar=="si":
        iniciales=[]
        palabra_completa=[]
        respuesta=[]
        valores=[]
        letras=[]
        significado=[]
        for llaves,valor in palabras.items():
            iniciales.append(f"[{llaves}]")
            palabra_completa.append(valor)
            respuesta.append('[ ]')
            valores.append(valor)
        for letters,meaning in palabras_significado.items():
            letras.append(f"[{letters}]")
            significado.append(meaning)

        j=0 
        aciertos=0
        errores=0
        PTO_ACIERTO=10
        PTO_ERROR=-3
        historial=[]
        puntos=turno(iniciales,respuesta,j,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores,historial)
        juego=input('¿Desea continuar jugando? ')
        if juego.lower()=='no':
            jugar="no"
            return (f'su puntuacion final es: {puntos}')

def turno(iniciales,respuesta,j,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores,historial):
    while j<len(iniciales):
        print("".join(iniciales))
        print("".join(respuesta))
        print("                           ")
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        print(f"Turno letra {iniciales[j][1]} -palabra de {len(palabra_completa[j])} letras")
        print(f"Definición: {significado[j]} ")
        pregunta=input('Ingrese una palabra: ')
        
        
        if pregunta ==valores[j]:
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
    lista=""
    for intentos in historial_turno:
        lista+=intentos+"\n"
    return lista    

print(tablero(letraPalabra.letra_palabra(),letraSignificado.letra_sifnificado()))
