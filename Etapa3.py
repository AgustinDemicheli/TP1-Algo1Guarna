import random
import Etapa8
import Etapa10
CANTIDAD_LETRAS_ROSCO = Etapa10.obtener_cantidad_letras_rosco()
def eleccion_letras():
    """
        El objetivo de esta funcion es devolver una lista de 10 letras del abecedario que serán
    las iniciales de las palabras para el juego
    - Nicolas Cardone
    """
    
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                    'x', 'y', 'z']
    return sorted(random.sample(abecedario,CANTIDAD_LETRAS_ROSCO))
    
def eleccion_palabras_candidatas(diccionario, lista_de_letras):
    """"
        El objetivo de esta funcion es elegir 10 palabras del diccionario formado en la etapa 8
    las cuales deben comenzar con las letras de la anterior funcion
    - Nicolas Cardone
    """
    i = 0
    PRIMERA_LETRA = 0
    palabras_candidatas = []
    palabras = list(diccionario.keys())
    random.shuffle(palabras)

    while i < len(palabras) or len(lista_de_letras) > 0 :
        if palabras[i][PRIMERA_LETRA] in lista_de_letras:
            palabras_candidatas.append(palabras[i])
            lista_de_letras.remove(palabras[i][PRIMERA_LETRA])
        i += 1
    return sorted(palabras_candidatas)
#print(eleccion_palabras_candidatas(Etapa8.obtener_lista_definiciones(), eleccion_letras()))