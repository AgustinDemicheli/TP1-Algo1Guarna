import Etapa2
import Etapa3

def letra_sifnificado():
    """
    recibe las listas y organiza la información en un diccionario con la palabra como clave y el significado como valor
    -Nadeska Millán-
    """
    #lista_vieja=datos_prueba.datos_prueba()
    lista_vieja = Etapa3.eleccion_palabras_candidatas( Etapa2.generar_palabras_candidatas(), Etapa3.eleccion_letras() )

    palabra_significado={}

    dicc=Etapa2.generar_palabras_candidatas()

    for word in lista_vieja:
        #palabra[lista_vieja[i][0][0].upper()]=lista_vieja[i][0]
        palabra_significado[word]=dicc[word]
        
    return (palabra_significado)

letra_sifnificado()