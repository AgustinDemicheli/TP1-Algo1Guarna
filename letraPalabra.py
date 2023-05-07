from datos import datos_prueba

def letra_palabra():
    lista_vieja=datos_prueba.datos_prueba()
    palabra={}
    for i in range (0,len(lista_vieja)):
        palabra[lista_vieja[i][0][0].upper()]=lista_vieja[i][0]
    return(palabra)
