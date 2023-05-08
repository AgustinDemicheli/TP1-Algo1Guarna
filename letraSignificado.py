#from datos import datos
from datos import datos_prueba

def letra_sifnificado():
    lista_vieja=datos_prueba.datos_prueba()
    palabra_significado={}
    for i in range(0,len(lista_vieja)):
        palabra_significado[lista_vieja[i][0][0].upper()]=lista_vieja[i][1]
    return (palabra_significado)
