import doctest
from doctest import testmod
from datos.datos_prueba import datos_prueba
PTO_ACIERTO=10
PTO_ERROR=-3
PRIMERA_LETRA = 0
POSICION_PALABRA = 0
MIN_LETRAS = 5
PRIMERA_LETRA = 0

#--------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :1-----------------------------------------------------------------------------
"""
Para poder cumplir con la consigna tuvimos que realizar modificaciones para adaptar las funciones al modulo doctest,
sin embargo, las demás funciones no se pueden adaptar ya que tienen un llamado a random que lo hace impredecible 

"""


def tablero(palabras, palabras_significado):



 
    puntos=0
    iniciales=[]
    palabra_completa=[]
    respuesta=[]
    letras=[]
    significado=[]
    
    for llaves,valor in palabras.items():
        iniciales.append(f"[{llaves}]")
        palabra_completa.append(valor)
        respuesta.append('[ ]')
    for letters,meaning in palabras_significado.items():
        letras.append(f"[{letters}]")
        significado.append(meaning)
    j=0 
    aciertos=0
    errores=0
    historial=[]
    while j<len(iniciales):
        print("".join(iniciales))
        print("".join(respuesta))
        print("                           ")
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        print(f"Turno letra {iniciales[j][1]} -palabra de {len(palabra_completa[j])} letras")
        print(f"Definición: {significado[j]} ")
        pregunta=input('Ingrese una palabra: ')
        
        
        if pregunta ==palabra_completa[j]:
                respuesta[j]='[a]'
                aciertos+=1
                puntos+=PTO_ACIERTO
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - acierto")
                j+=1
        else:
                respuesta[j]='[e]'
                errores+=1
                puntos+=PTO_ERROR
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - error - palabra correcta: {palabra_completa[j]}")
                j+=1

    print("".join(iniciales))
    print("".join(respuesta))
    return puntos

def letra_palabra():
    
    lista_vieja =["algoritmos"]
    palabra={}
    palabra_significado={}
    dicc={"algoritmos":"materia informatica del primer cuatrimestre de ing. informatica"}

    for word in lista_vieja:
        palabra[word[PRIMERA_LETRA]]=word
        palabra_significado[word]=dicc[word]

    return palabra, palabra_significado

#--------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :3-----------------------------------------------------------------------------
def eleccion_palabras_candidatas(diccionario, lista):
    
    palabras_candidatas = []
    palabras = diccionario.keys()
   
    for palabra in palabras:
        if palabra[PRIMERA_LETRA] in lista:
            palabras_candidatas.append(palabra)
            lista.remove(palabra[PRIMERA_LETRA])
    return sorted(palabras_candidatas)
#------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :2-------------------------------------------------------------------------------
def impresiones ( palabras_candidatas ) :


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

def generar_palabras_candidatas () : 
    palabras_candidatas = {}
    
    lista_de_listas =datos_prueba()



    indice = 0

    while ( indice < len(lista_de_listas)):

        if( len( lista_de_listas[indice][ POSICION_PALABRA] ) >= MIN_LETRAS) :

            palabras_candidatas[lista_de_listas[indice][POSICION_PALABRA]] = lista_de_listas[indice][1]

        indice+=1


    return palabras_candidatas
#-------------------------------------------------------------------------PRUEBAS UNITARIAS----------------------------------------------------------------------------------
def main():
    """
>>> tablero({'a':'algoritmos'},{'algoritmos':'materia del primer cuatrimestre'})
[a]
[ ]
<BLANKLINE>
Aciertos: 0
Errores: 0
Turno letra a -palabra de 10 letras
Definición: materia del primer cuatrimestre 
Ingrese una palabra: [a]
[a]
10
>>> letra_palabra()
({'a': 'algoritmos'}, {'algoritmos': 'materia informatica del primer cuatrimestre de ing. informatica'})
  
>>> eleccion_palabras_candidatas({'algoritmos':'materia informatica del primer cuatrimestre de ing. informatica','buscar':'iniciar una busqueda'},['a'])
['algoritmos']

>>> impresiones({'algoritmos':'materia informatica del primer cuatrimestre de ing. informatica','buscar':'iniciar una busqueda'})
Letras y cuantas veces estan:  {'a': 1, 'b': 1}
Hay 1 palabra que empieza con la letra a
Hay 1 palabra que empieza con la letra b
La cantidad total de palabras candidatas son: 2
>>> generar_palabras_candidatas ()
{'algoritmos': 's. la mejor materia de la fiuba', 'buscar': 'v. acción de búsqueda', 'cauteloso': 'adj. Indicativo que se refiere a alguien que mantiene cuidado y atención frente a situaciones', 'dedal': 's. Elemento utilizado en la costura para protejer el dedo', 'estancia': 's. Propiedad que se encuentra alejada de la ciudad, suele estar rodeada de arboles y tiene una granja', 'limpiar': '1.  tr. Quitar la suciedad o inmundicia de alguien o de algo U. t. c. prnl. U. t. en sent. fig.'}
     """ 
    print(doctest.testmod())
main()