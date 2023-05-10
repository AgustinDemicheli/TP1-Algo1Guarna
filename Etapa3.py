import random
import Etapa2
import datos
def eleccion_letras():
    
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                    'x', 'y', 'z']
    return sorted(random.sample(abecedario,10))
    
def eleccion_palabras_candidatas(diccionario, lista):
    PRIMERA_LETRA = 0
    palabras_candidatas = []
    palabras = diccionario.keys()
   
    for palabra in palabras:
        if palabra[PRIMERA_LETRA] in lista:
            palabras_candidatas.append(palabra)
            lista.remove(palabra[PRIMERA_LETRA])
    print(sorted(palabras_candidatas))
    
letras = eleccion_letras()
eleccion_palabras_candidatas(Etapa2.generar_palabras_candidatas(), letras)