def tablero(palabras,palabras_significado):
    """
    tablero recibe dos diccionarios, el primero  contiene inciales-palabra,
    el segundo contiene la inicial de la palabra con su significado
    """
    iniciales=[]
    palabra_completa=[]
    respuesta=[]
    valores=[]
    letras=[]
    significado=[]
    for llaves,valor in palabras.items():
        iniciales.append(llaves)
        palabra_completa.append(valor)
        respuesta.append('[ ]')
        valores.append(valor)
    for letters,meaning in palabras_significado.items():
        letras.append(letters)
        significado.append(meaning)

    i=0 
    aciertos=0
    errores=0
    PTO_ACIERTO=10
    PTO_ERROR=-3
    puntos=0
    turno(iniciales,respuesta,i,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores)
    juego=input('¿Desea continuar jugando? ')
    if juego.lower()=='si':
        turno(iniciales,respuesta,i,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores)
        puntos=puntos+puntos
    else:
        return (f'su puntuacion final es: {puntos}')

def turno(iniciales,respuesta,i,aciertos,errores,PTO_ACIERTO,PTO_ERROR,puntos,palabra_completa,significado,valores):
    while i<len(iniciales):
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
    print("".join(iniciales))
    print("".join(respuesta))
    return puntos

print(tablero({
        "[A]":'algoritmos',
        "[B]":'buscar',
        "[C]":'cauteloso',
        "[D]":'dedal',
        "[E]":'estancia',
    },{
        "[A]":'s. la mejor materia de la fiuba',
        "[B]":'v. acción de búsqueda',
        "[C]":'adj. Indicativo que se refiere a alguien que mantiene cuidado y atención frente a situaciones',
        "[D]":'s. Elemento utilizado en la costura para protejer el dedo',
        "[E]":'s. Propiedad que se encuentra alejada de la ciudad, suele estar rodeada de arboles y tiene una granja',
    }))
