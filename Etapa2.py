from datos import datos


POSICION_PALABRA = 0
MIN_LETRAS = 5
def generar_palabras_candidatas () :  

    """
    El objetivo será generar un diccionario de palabras candidatas a adivinar.
    Las palabras seleccionadas deberán tener un mínimo de 5 letras.
    -Diego Astorga-

    """
    palabras_candidatas = {}
    
    lista_de_listas = datos.obtener_lista_definiciones()



    indice = 0

    while ( indice < len(lista_de_listas)):

        if( len( lista_de_listas[indice][ POSICION_PALABRA] ) >= MIN_LETRAS) :

            palabras_candidatas[lista_de_listas[indice][POSICION_PALABRA]] = lista_de_listas[indice][1]

        indice+=1


    return palabras_candidatas

 #---------------------------------------------------------------------------------------------

def impresiones ( palabras_candidatas ) :

    """
    Una vez generado el diccionario de palabras en la anterior funcion, se debe mostrar por pantalla el total de 
    palabras que hay por cada letra, y el total que hay en el diccionario.
    -Diego Astorga-
    """

    lista = list( palabras_candidatas.keys() )

    palabras_por_letras= {}

    

    
    for i in range(len(lista)) :

        contador_De_letras = 0


        for j in range(len(lista)) :

            
            if ( lista[i][0] == lista[j][0] ) :
 
                contador_De_letras+=1
            
        palabras_por_letras[ lista[i][0] ] = contador_De_letras

    print('Letras y cuantas veces estan: ', palabras_por_letras)

    for elem in palabras_por_letras :


        if ( palabras_por_letras[elem] == 1 ) :
            
            print( 'Hay', palabras_por_letras[elem], 'palabra que empieza con la letra', elem )
        
        else:
            

            print( 'Hay', palabras_por_letras[elem], 'palabras que empiezan con la letra', elem )
   

    print('La cantidad total de palabras candidatas son:', len(palabras_candidatas))

#---------------------------------------------------------------------------------------------------

generar_palabras_candidatas()

impresiones( generar_palabras_candidatas() )