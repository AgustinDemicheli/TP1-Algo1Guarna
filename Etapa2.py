import datos #PORQUE ESTA A LA MISMA ALTURA DE RAIZ



# Ahora el objetivo será generar un diccionario de palabras candidatas a adivinar.
# Para ello se proveerá una función que retorna un texto en formato:
# [
# [“palabra1”, “definición1”],
# [“palabra2”, “definición2”],
# …
# ]
# Se les proveerá de una función que devolverá un texto del cual extraerán las palabras
# con sus definiciones para formar el diccionario. Las palabras seleccionadas deberán tener
# un mínimo de 5 letras.
# Una vez generado el diccionario de palabras, se debe mostrar por pantalla el total de
# palabras que hay por cada letra, y el total que hay en el diccionario.


def generar_palabras_candidatas ( lista_de_listas ) :  #lista_de_listas, es una lista_de_listasa de lista_de_listasas

    """
    El objetivo será generar un diccionario de palabras candidatas a adivinar.
    Las palabras seleccionadas deberán tener un mínimo de 5 letras.
    Una vez generado el diccionario de palabras, se debe mostrar por pantalla el total de 
    palabras que hay por cada letra, y el total que hay en el diccionario.
    """
    palabras_candidatas = {}

    POSICION_PALABRA = 0
    MIN_LETRAS = 5
    CANTIDAD_DE_CANDIDATOS=0
    MAXIMOS_CANDIDATOS_ADMITIDOS = 3

    indice = 0

    while ( CANTIDAD_DE_CANDIDATOS< MAXIMOS_CANDIDATOS_ADMITIDOS  and indice < len (lista_de_listas) ):

        if( len( lista_de_listas[indice][ POSICION_PALABRA] ) >= MIN_LETRAS) :

            palabras_candidatas[lista_de_listas[indice][POSICION_PALABRA]] = lista_de_listas[indice][1]

        indice+=1
        CANTIDAD_DE_CANDIDATOS+=1

    #---------------------------------------------------------------------------------------------

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

    print( lista )





    

    print('La cantidad total de palabras candidatas son:', len(palabras_candidatas))

generar_palabras_candidatas( datos.obtener_lista_definiciones() )