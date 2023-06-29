import Etapa8
import Etapa3

def letra_palabra():
    """
    Recibe las listas y organiza la información en un diccionario con la palabra como clave y el significado como valor
    -Nadeska Millán-
    """
    dicc=Etapa8.obtener_lista_definiciones() #-->DICCIONARIO CON TODAS! LAS PALABRAS Y SU DEFINICION
    lista = Etapa3.eleccion_palabras_candidatas(dicc, Etapa3.eleccion_letras()) #--> LISTA DE LAS PALABRAS CANDIDATAS ORDENADAS. DE LARGO INDICADO
    palabra_significado={}

    for word in lista:
        palabra_significado[word]=dicc[word]
        
    return palabra_significado