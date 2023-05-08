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
            iniciales.append("["+llaves+"]")
            palabra_completa.append(valor)
            respuesta.append('[ ]')
            valores.append(valor)
        for letters,meaning in palabras_significado.items():
            letras.append("["+letters+"]")
            significado.append(meaning)

        i=0 
        aciertos=0
        errores=0
        PTO_ACIERTO=10
        PTO_ERROR=-3
        puntos=turno(iniciales,respuesta,i,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores)
        juego=input('¿Desea continuar jugando? ')
        if juego.lower()=='no':
            jugar="no"
            return (f'su puntuacion final es: {puntos}')

def turno(iniciales,respuesta,i,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores):
    while i<len(iniciales):
        print("")
        print("".join(iniciales))
        print("".join(respuesta))
        print("                           ")
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        print(f"Turno letra {iniciales[i][1]} -palabra de {len(palabra_completa[i])} letras")
        print(f"Definición: {significado[i]} ")
        pregunta=input('Ingrese una palabra: ')
        
        if pregunta ==valores[i]:
                respuesta[i]='[a]'
                i+=1
                aciertos+=1
                puntos+=PTO_ACIERTO
        else:
                respuesta[i]='[e]'
                i+=1
                errores+=1
                puntos+=PTO_ERROR
        print("puntos Acumulados:",puntos)  #saber cuanto llevo     
        print("")
    print("".join(iniciales))
    print("".join(respuesta))
    return puntos

print(tablero(letraPalabra.letra_palabra(),letraSignificado.letra_sifnificado()))
