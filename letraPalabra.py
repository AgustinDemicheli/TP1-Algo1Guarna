import Etapa8
import Etapa3

def letra_palabra():
    """
    recibe las listas y organiza la información en un diccionario con la letra como llave y palabra como valor,
    también recibe las listas y organiza la información en un diccionario con la palabra como clave y el significado como valor
    -Nadeska Millán-
  
    
    """
    PRIMERA_LETRA = 0
    dicc=Etapa8.obtener_lista_definiciones()
    lista = Etapa3.eleccion_palabras_candidatas(dicc, Etapa3.eleccion_letras())
    palabra={}
    palabra_significado={}

    for word in lista:
        palabra[word[PRIMERA_LETRA]]=word
        palabra_significado[word]=dicc[word]

    return palabra, palabra_significado

letra_palabra()