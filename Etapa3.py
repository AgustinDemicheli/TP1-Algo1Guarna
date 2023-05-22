import random
import Etapa2
import datos
def eleccion_letras():
    """
        El objetivo de esta funcion es devolver una lista de 10 letras del abecedario que serán
    las iniciales de las palabras para el juego
    - Nicolas Cardone
    """
    
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                    'x', 'y', 'z']
    return sorted(random.sample(abecedario,10))
    
def eleccion_palabras_candidatas(diccionario, lista):
    """"
        El objetivo de esta funcion es elegir 10 palabras del diccionario formado en la etapa 2
    las cuales deben comenzar con las letras de la anterior funcion
    - Nicolas Cardone
    """
    
    PRIMERA_LETRA = 0
    palabras_candidatas = []
    palabras = diccionario.keys()
   
    for palabra in palabras:
        if palabra[PRIMERA_LETRA] in lista:
            palabras_candidatas.append(palabra)
            lista.remove(palabra[PRIMERA_LETRA])
    return sorted(palabras_candidatas)
    
eleccion_palabras_candidatas( Etapa2.generar_palabras_candidatas(), eleccion_letras() )