import Etapa2
import Etapa3

def letra_palabra():
    #lista_vieja=datos_prueba.datos_prueba()
    lista_vieja = Etapa3.eleccion_palabras_candidatas( Etapa2.generar_palabras_candidatas(), Etapa3.eleccion_letras() )
    palabra={}
    for word in lista_vieja:
        #palabra[lista_vieja[i][0][0].upper()]=lista_vieja[i][0]
        palabra[word[0]]=word

    palabra_significado={}

    dicc=Etapa2.generar_palabras_candidatas()

    for word in lista_vieja:
        #palabra[lista_vieja[i][0][0].upper()]=lista_vieja[i][0]
        palabra_significado[word]=dicc[word]

        
    return palabra, palabra_significado

letra_palabra()